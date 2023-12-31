from typing import Optional, Union
from pydantic import AnyUrl, BaseModel, RootModel, Field,  EmailStr

from hdr_schemata.definitions.SchemaOrg import Text

from .Person import Person
from .Organization import Organization

class CreativeWork(BaseModel):

    m_type: Text = Field(
        alias="@type",
        default="CreativeWork"
    )

    name: Optional[Text] = Field(
        None,
        description="The name of the item."
    )

    abstract: Optional[Text] = Field(
        None,
        title='abstract',
        description="An abstract is a short description that summarizes a CreativeWork."
    )

    accessMode: Optional[Text] = Field(
        None,
        title='Access Mode',
        description='The human sensory perceptual system or cognitive faculty through which a person may process or perceive information. Values should be drawn from the approved vocabulary.'
    )

    accessibilitySummary: Optional[Text] = Field(
        None,
        title='Acces Summary',
        description='A human-readable summary of specific accessibility features or deficiencies, consistent with the other accessibility metadata but expressing subtleties such as "short descriptions are present but long descriptions will be needed for non-visual users" or "short descriptions are present and no long descriptions are needed."'
    )
    

    identifier: Optional[Text] = Field(
        None,
        description="The identifier property represents any kind of identifier for any kind of Thing, such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links."
    )


    #creator: Optional[Union[Person,Organization]] = Field(
    creator: Optional[Organization] = Field(
        None,
        title='Creative Work creator',
        description="The creator/author of this CreativeWork. This is the same as the Author property for CreativeWork."
    )

    publisher: Optional[Union[Person,Organization]] = Field(
        None,
        title='Creative Work publisher',
        description="The publisher of the creative work."
    )

    countryOfOrigin: Optional[Text] = Field(
        None,
        title='Country Of Origin',
        description=r'''The country of origin of something, including products as well as creative works such as movie and TV content.

In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of CreativeWork it is difficult to provide fully general guidance, and properties such as contentLocation and locationCreated may be more applicable.

In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.'''
    )

    jurisdiction: Optional[Text] = Field(
        None,
        title='Jurisdiction',
        description="Indicates a legal jurisdiction, e.g. of some legislation, or where some government service is based."
    )

    typicalAgeRange: Optional[Text] = Field(
        None,
        description="The typical expected age range, e.g. '7-9', '11-'."
    )

    temporalCoverage: Optional[Text] = Field(
        None,
        title='temporalCoverage',
        description="The typical expected age range, e.g. '7-9', '11-'."
    )

    inLanguage: Optional[Text] = Field(
        None,
        description="The language of the content or performance or used in an action. Please use one of the language codes from the IETF BCP 47 standard. See also availableLanguage. Supersedes language."
    )

    encodingFormat: Optional[Text] = Field(
        None,
        description=r'''Media type typically expressed using a MIME format (see IANA site and MDN reference), e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc.

In cases where a CreativeWork has several media type representations, encoding can be used to indicate each MediaObject alongside particular encodingFormat information.

Unregistered or niche encoding and file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry. Supersedes fileFormat.'''
    )

