from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .DatasetLinkage import DatasetLinkage

from .annotations import annotations

an = annotations.linkage


class Linkage(BaseModel):
    class Config:
        extra = "forbid"

    isGeneratedUsing: Optional[CommaSeparatedValues] = Field(
        None, **an.isGeneratedUsing.__dict__
    )

    associatedMedia: Optional[CommaSeparatedValues] = Field(
        None, **an.associatedMedia.__dict__
    )

    dataUses: Optional[CommaSeparatedValues] = Field(None, **an.dataUses.__dict__)

    isReferenceIn: Optional[CommaSeparatedValues] = Field(
        None, **an.isReferenceIn.__dict__
    )

    tools: Optional[CommaSeparatedValues] = Field(None, **an.tools.__dict__)

    datasetLinkage: Optional[DatasetLinkage] = Field(None, **an.datasetLinkage.__dict__)

    investigations: Optional[CommaSeparatedValues] = Field(
        None, **an.investigations.__dict__
    )

    syntheticDataWebLink: Optional[CommaSeparatedValues] = Field(
        None, **an.syntheticDataWebLink.__dict__
    )

    publicationAboutDataset: Optional[List[Doi]
    ] = Field(None, **an.publicationAboutDataset.__dict__)

    publicationUsingDataset: Optional[List[Doi]
    ] = Field(None, **an.publicationUsingDataset.__dict__)
