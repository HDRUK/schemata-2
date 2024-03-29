from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *
from .annotations import annotations

an = annotations.accessibility.usage


class Usage(BaseModel):
    class Config:
        extra = "forbid"

    dataUseLimitation: Optional[
        Union[Optional[CommaSeparatedValues], List[DataUseLimitation]]
    ] = Field(None, **an.dataUseLimitation.__dict__)

    dataUseRequirements: Optional[
        Union[Optional[CommaSeparatedValues], List[DataUseRequirements]]
    ] = Field(None, **an.dataUseRequirements.__dict__)

    resourceCreator: Optional[
        Union[Optional[ShortDescription], List[Optional[ShortDescription]]]
    ] = Field(None, **an.resourceCreator.__dict__)

    investigations: Optional[
        Union[Optional[CommaSeparatedValues], List[Optional[Url]]]
    ] = Field(None, **an.investigations.__dict__)

    isReferencedBy: Optional[Union[Optional[Doi], str, List[Optional[Doi]]]] = Field(
        None, **an.isReferencedBy.__dict__
    )
