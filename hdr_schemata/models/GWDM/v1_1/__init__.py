from hdr_schemata.models.GWDM import Gwdm10
from .Coverage import Coverage 
from .Accessibility import Accessibility
from .Required import Required
from .Summary import Summary
from typing import Optional
from pydantic import Field, BaseModel, constr


class Gwdm11(Gwdm10):

    summary: Summary = Field(
        ...,
        description='Summary of metadata describing key pieces of information.',
        title='Summary',
    )

    
    required: Required = Field(
        ...,
        description='required metadata needed for the GWDM',
        title='Required'
    )
    
    #overload Coverage with an updated version of it.. 
    coverage: Optional[Coverage] = Field(
        None,
        description='Observational, Spatial and Temporal coverage',
        title='Coverage',
    )

    #modifying Accessibility --> modifying Usage
    accessibility: Accessibility = Field(
        None,
        description='Accessibility information.',
        title='Accessibility',
    )
    
