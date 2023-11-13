from typing import Optional
from pydantic import Field
from .Usage import Usage
from hdr_schemata.models.GWDM.v1_0 import Accessibility as BaseAccessibility


class Accessibility(BaseAccessibility):

    usage: Optional[Usage] = Field(
        None,
        description='This section includes information about how the data can be used and how it is currently being used',
        title='Usage',
    )
