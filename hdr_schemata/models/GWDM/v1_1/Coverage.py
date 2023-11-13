from hdr_schemata.models import remove_fields_from_cls
from hdr_schemata.models.GWDM.v1_0 import Coverage as BaseCoverage
import re
from typing import Optional,List
from pydantic import Field, RootModel, constr


def get_pattern(allowed_phrases):
    return r'\b(?:' + '|'.join(allowed_phrases) + r')(?:,(?:' + '|'.join(allowed_phrases) + r'))*\b'


class Anthropometric(RootModel):
    root: Optional[constr(pattern=get_pattern(
        [
            'Blood Pressure',
            'Hip Circumference',
            'Height',
            'Waist Circumference',
            'Weight',
        ]))]

class BiologicalSamples(RootModel):
    root: Optional[constr(pattern=get_pattern(
        [
            'Blood',
            'Other',
            'Urine',
            'Saliva'
        ]))]
    
class Physical(RootModel):
    root: Optional[constr(pattern=get_pattern(
        [
            'Respiratory',
            'Vision',
            'Hearing',
            'Musculoskeletal',
            'Cardiovascular',
            'Reproductive'
        ]))]

class Psychological(RootModel):
    root: Optional[constr(pattern=get_pattern(
        [
            'Cognitive Function',
            'Mental Health'
        ]))]
    
class Lifestyles(RootModel):
    root: Optional[constr(pattern=get_pattern(
        [
            'Smoking',
            'Dietary Habits',
            'Physical Activity',
            'Alcohol'
        ]))]

class Gender(RootModel):
    root: Optional[constr(pattern=get_pattern(
        [
            'Male',
            'Female',
            'Other'
        ]))]

class SocioEconomic(RootModel):
    root: Optional[constr(pattern=get_pattern(
        [
            'Finances',
            'Family Circumstances',
            'Housing',
            'Education',
            'Marital Status',
            'Occupation',
            'Ethnic Group',
            'Social Support'
        ]))]
    

class Coverage(BaseCoverage):

    class Config:
        extra = 'forbid'

    
    gender: Optional[Gender] = Field(
        None,
        title='Gender',
        description='Male, Female, Other'
    )

    biologicalsamples: Optional[BiologicalSamples] = Field(
        None,
        title='Biological Samples',
        description='Blood, Saliva, Urine, Other'
    )

    psychological: Optional[Psychological] = Field(
        None,
        title='Psychological',
        description='Mental health, Cognitive function'
    )

    physical: Optional[Physical] = Field(
        None,
        title='Physical',
        description='Cardiovascular, Respiratory, Musculoskeletal, Hearing and Vision, Reproductive'
    )

    anthropometric: Optional[Anthropometric] = Field(
        None,
        title='Anthropometric',
        description='Height, Weight, Waist circumference, Hip circumference, Blood pressure'
    )
        
    lifestyle: Optional[Lifestyles] = Field(
        None,
        title='Lifestyle',
        description='Cohort lifestyle habits: Smoking, Physical activity, Dietary habits, Alcohol'
    )
    

    socioeconomic: Optional[SocioEconomic] = Field(
        None,
        title='Socio-economic',
        description='Occupation, Family circumstances, Housing, Education, Ethnic group, Martial status, Social support'
    )

#inherited physicalSampleAvailability but this has now been replaced by biologicalsamples
remove_fields_from_cls(Coverage,['physicalSampleAvailability'])
