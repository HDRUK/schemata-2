from typing import List, Optional
from pydantic import AnyUrl, BaseModel, EmailStr, Field
from hdr_schemata.definitions.HDRUK import (
    TwoHundredFiftyFiveCharacters,
    ShortTitle,
    Doi,
    LongAbstractText,
    CommaSeparatedValues,
    DatasetType,
    LongDescription
)

from .Publisher import Publisher

class Summary(BaseModel):

    title: TwoHundredFiftyFiveCharacters = Field(
        ...,
        description='The main title of the dataset',
        example="Publications that mention HDR-UK (or any variant thereof) in Acknowledgements or Author Affiliations",
        title='Title'
    )

    shortTitle: Optional[ShortTitle] = Field(
        ...,
        description='A shorter descriptive title of the dataset',
        example="ONS 2011 Census Wales (CENW)",
        title='Shorttitle'
    )

    doiName: Optional[Doi] = Field(
        ...,
        description="DOI associated to this dataset",
        example="10.1093/ije/dyx196",
        title='Doiname'
    )
    
    abstract: LongAbstractText = Field(
        ...,
        description="Longer abstract detailing the dataset.",
        example="COVID-19 Key Worker Testing Results data is required by NHS Digital to support COVID-19 requests for linkage, analysis and dissemination to other organisations who require the data in a timely manner.",
        title='Abstract'
    )
    
    keywords: Optional[CommaSeparatedValues] = Field(
        ...,
        description="Comma separated key words associated to this dataset.",
        example="Preprints,Papers,HDR UK",
        title='Keywords'
    )

    #note: do we want to limit these values by Enums?
    controlledKeywords: Optional[CommaSeparatedValues] = Field(
        ...,
        description="Keywords that have been filtered and limited",
        title='Controlled Keywords'
    )

    contactPoint: Optional[EmailStr] = Field(
        ...,
        description='email of a person who can be the main contact point of this dataset',
        example="susheel.varma@hdruk.ac.uk",
        title='Contact Point'
    )

    #note: new addition added by Damon.. may need to revisit what this should be?
    #      should be Enums?
    datasetType: Optional[DatasetType] = Field(
        ...,
        description="What type of dataset is this?",
        title='Dataset type'
    )
    
    description: Optional[LongDescription] = Field(
        ...,
        description="Longer description of the dataset in detail",
        example="Publications that mention HDR-UK (or any variant thereof) in Acknowledgements or Author Affiliations\n\nThis will include:\n- Papers\n- COVID-19 Papers\n- COVID-19 Preprint",
        title='Description'
    )
    
    publisher: Optional[Publisher] = Field(
        ...,
        description="Link to details about the publisher of this dataset",
        title='Publisher',
    )

