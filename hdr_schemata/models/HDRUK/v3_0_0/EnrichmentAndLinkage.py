from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .DatasetDescriptor import DatasetDescriptor

from .annotations import annotations

an = annotations.enrichmentAndLinkage


class EnrichmentAndLinkage(BaseModel):
    class Config:
        extra = "forbid"

    derivedFrom: Optional[
        Union[
            Optional[CommaSeparatedValues], 
            List[Optional[AbstractText]], 
            List[DatasetDescriptor]
        ]
    ] = Field(None, **an.derivedFrom.__dict__)

    isPartOf: Optional[
        Union[
            Optional[CommaSeparatedValues],
            List[Union[Url, OneHundredFiftyCharacters]],
            List[DatasetDescriptor]
        ]
    ] = Field(None, **an.isPartOf.__dict__)

    linkableDatasets: Optional[
        Union[
            Optional[CommaSeparatedValues],
            List[Union[Optional[Url], OneHundredFiftyCharacters]],
            List[DatasetDescriptor]
        ]
    ] = Field(None, **an.linkableDatasets.__dict__)

    similarToDatasets: Optional[
        Union[
            Optional[CommaSeparatedValues],
            List[Union[Optional[Url], OneHundredFiftyCharacters]],
            List[DatasetDescriptor]
        ]
    ] = Field(None, **an.linkableDatasets.__dict__)

    investigations: Optional[List[Url]] = Field(None, **an.investigations.__dict__)
    
    tools: Optional[List[Url]] = Field(
        None, **an.tools.__dict__
    )
    
    syntheticDataWebLink: Optional[List[Url]] = Field(
        None, **an.syntheticDataWebLink.__dict__
    )

    publicationAboutDataset: Optional[List[Doi]
    ] = Field(None, **an.publicationAboutDataset.__dict__)

    publicationUsingDataset: Optional[List[Doi]
    ] = Field(None, **an.publicationUsingDataset.__dict__)

