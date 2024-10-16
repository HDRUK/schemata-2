from typing import Optional
from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import Semver, UrlV2

from .annotations import annotations

an = annotations.revisions


class Revision(BaseModel):
    class Config:
        extra = "forbid"

    version: Semver = Field(..., **an.version.__dict__)
    url: Optional[UrlV2] = Field(None, **an.url.__dict__)
