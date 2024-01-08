from hdr_schemata.models.HDRUK.v2_1_2 import Hdruk212
import json
from typing import Optional
from pydantic import Field
from .Provenance import Provenance


class Hdruk213(Hdruk212):
    provenance: Optional[Provenance] = Field(
        None,
        description="Provenance information allows researchers to understand data within the context of its origins and can be an indicator of quality, authenticity and timeliness.",
        title="Provenance",
    )

    @classmethod
    def save_schema(cls, location="./2.1.3/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
