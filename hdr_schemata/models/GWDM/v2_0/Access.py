from typing import Optional, List, Union
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.accessibility.access


class Access(BaseModel):
    class Config:
        extra = "forbid"

    accessRights: Optional[CommaSeparatedValues] = Field(
        ..., **an.accessRights.__dict__
    )

    accessService: Optional[LongDescription] = Field(None, **an.accessService.__dict__)

    accessRequestCost: Optional[LongDescription] = Field(
        None, **an.accessRequestCost.__dict__
    )

    deliveryLeadTime: Optional[DeliveryLeadTime] = Field(
        None, **an.deliveryLeadTime.__dict__
    )

    jurisdiction: Optional[CommaSeparatedValues] = Field(
        ..., **an.jurisdiction.__dict__
    )

    dataController: Optional[LongDescription] = Field(..., **an.dataController.__dict__)

    dataProcessor: Optional[LongDescription] = Field(None, **an.dataProcessor.__dict__)

    accessServiceCategory: Optional[CommaSeparatedValues] = Field(
        None, **an.accessServiceCategory.__dict__
    )

    accessMode: Optional[AccessMode] = Field(
        "New project", **an.accessMode.__dict__
    )