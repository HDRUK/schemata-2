# from hdr_schemata.models.GWDM.v1_0 import Gwdm10 as Model
# from hdr_schemata.models.HDRUK.base import Observation as Model
# from hdr_schemata.models.HDRUK import Hdruk220 as Model
from hdr_schemata.models.GWDM.v1_1 import Gwdm11 as Model

from pydantic._internal._model_construction import ModelMetaclass
from pydantic import BaseModel, RootModel
import pandas as pd
import json
import typing
import enum

from hdr_schemata.models.HDRUK.v2_1_2.Observations import Observation

_type1 = typing.List[Observation]
_type2 = typing.Optional[Observation]
_type3 = typing.Union[Observation, str]


def extract_type_info(type_hint):
    is_list = False
    is_optional = False
    inner_types = None
    if getattr(type_hint, "__origin__", None) is list:
        is_list = True
        inner_types = type_hint.__args__
    elif getattr(type_hint, "__origin__", None) is typing.Union:
        inner_types = type_hint.__args__
        inner_types_not_none = [
            _type for _type in inner_types if not _type is type(None)
        ]
        is_optional = len(inner_types_not_none) < len(inner_types)

        inner_types = inner_types_not_none
        if is_optional:
            inner_types += ["null"]

        inner_type = inner_types[0]
        is_list = getattr(inner_type, "__origin__", None) is list
        if hasattr(inner_type, "__args__"):
            inner_types = inner_type.__args__

    else:
        inner_types = [type_hint]

    type_names = []
    for _type in inner_types:
        type_name = getattr(_type, "__name__", str(_type))

        try:
            if _type and issubclass(_type, RootModel):
                info = _type.model_json_schema()
                title = info.pop("title")
                type_name += "[" + json.dumps(info).replace('"', "'") + "]"
                # type_name = {title: info}
        except TypeError:
            ...

        if type(_type) == enum.EnumMeta:
            type_name += (
                "["
                + ",".join(
                    [
                        "'" + member.value + "'" if member.value else "null"
                        for member in _type
                    ]
                )
                + "]"
            )

        type_names.append(type_name)

    return is_list, is_optional, type_names


def get_fields(structure, model: type[BaseModel]):
    model_hints = typing.get_type_hints(model)
    for name, field in model.model_fields.items():
        if name == "root":
            continue
        # if name != "structuralMetadata":
        #    continue

        t = field.annotation

        _type = model_hints[name]

        is_list, is_optional, type_names = extract_type_info(_type)

        value = {
            "name": name,
            "required": field.is_required(),
            "title": field.title,
            "description": field.description,
            "title": field.title,
            "examples": field.examples,
            "type": type_names,
            "is_list": is_list,
            "is_optional": is_optional,
        }

        if hasattr(t, "__args__"):
            t = t.__args__[0]

        if isinstance(t, type) and issubclass(t, BaseModel):
            subItems = []
            get_fields(subItems, t)
            value["subItems"] = subItems

        structure.append(value)


def json_to_markdown(structure, level=2):
    md = ""
    for field in structure:
        name = field.pop("name")
        subItems = field.pop("subItems", None)
        description = field.pop("description")
        examples = field.pop("examples")
        if examples:
            examples = "\n".join(["  * " + str(x) for x in examples])
            examples = "Examples: \n\n " + examples
        else:
            examples = ""

        table = ""
        if not subItems:
            table = pd.Series(field).sort_index().to_frame().T.set_index("title")
            table = table.to_markdown()

        heading = "#" * level
        md += rf"""
{heading} {name}

{description}
        
{table}

{examples}

"""

        if subItems:
            md += json_to_markdown(subItems, level=level + 1)

    return md


structure = []
get_fields(structure, Model)
# get_fields(structure,Hdruk212)

with open("temp.json", "w") as f:
    print(json.dumps(structure, indent=6))
    json.dump(structure, f, indent=6)

md = json_to_markdown(structure)

with open("temp.md", "w") as f:
    f.write(md)
