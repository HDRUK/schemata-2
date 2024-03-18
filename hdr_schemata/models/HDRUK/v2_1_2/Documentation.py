from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from hdr_schemata.annotations import annotations

an = annotations.HDRUK.v2p1p2.documentation


class Documentation(BaseModel):
    class Config:
        extra = "forbid"

    description: Optional[Description] = Field(None, **an.description.__dict__)

    associatedMedia: Optional[
        Union[Optional[CommaSeparatedValues], List[Optional[Url]]]
    ] = Field(None, **an.associatedMedia.__dict__)

    isPartOf: Optional[
        Union[
            Optional[CommaSeparatedValues],
            List[Union[Optional[Url], OneHundredFiftyCharacters, IsPartOfEnum]],
        ]
    ] = Field("NOT APPLICABLE", **an.isPartOf.__dict__)
