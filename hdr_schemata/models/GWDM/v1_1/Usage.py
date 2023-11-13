from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.models.GWDM.v1_0 import Usage as BaseUsage

from .Organisation import Organisation 


class Usage(BaseUsage):
    resourceCreator: Optional[Organisation] = Field(
        None,
        description='Who has created this resource',
        title='Resource Creator',
    )
