from hdr_schemata.models.HDRUK.v2_1_2.Organisation import Organisation as BaseOrganisation
from typing import Optional, Union, List
from pydantic import Field

from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.summary.organisation


class Organisation(BaseOrganisation):

    identifier: Optional[Url] = Field(
        None, **an.identifier.__dict__, json_schema_extra={"guidance": an.identifier.guidance}
    )

    name: OneHundredFiftyCharacters = Field(
        ...,
        **an.name.__dict__,
        json_schema_extra={"guidance": an.name.guidance}
    )

    contactPoint: Union[EmailAddress, List[EmailAddress]] = Field(
        ...,
        **an.contactPoint.__dict__
    )
