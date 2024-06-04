from typing import Optional
from pydantic import RootModel,constr
from enum import Enum

#note: contructed as a string of max_length=100
#      in the future we may want to limit this with Enums
class DatasetType(RootModel):
    root: Optional[constr(min_length=2, max_length=100)]

class DatasetTypeV2(Enum):
    HEALTH_AND_DISEASE = 'Health and disease'
    TREATMENTS_INTERVENTIONS = 'Treatments/Interventions'
    MEASUREMENTS_TESTS = 'Measurements/Tests'
    IMAGING_TYPES = 'Imaging types'
    IMAGING_AREA_OF_THE_BODY = 'Imaging area of the body'
    OMICS = 'Omics'
    SOCIOECONOMIC = 'Socioeconomic'
    LIFESTYLE = 'Lifestyle'
    REGISTRY = 'Registry'
    ENVIRONMENT_AND_ENERGY = 'Environment and energy'
    INFORMATION_AND_COMMUNICATION = 'Information and communication'
    POLITICS = 'Politics'

class DatasetSubType(Enum):
    MENTAL_HEALTH = 'Mental health'
    CARDIOVASCULAR = 'Cardiovascular'
    CANCER = 'Cancer'
    RARE_DISEASES = 'Rare diseases'
    METABOLIC_AND_ENDOCRINE = 'Metabolic and Endocrine'
    NEUROLOGICAL = 'Neurological'
    REPRODUCTIVE = 'Reproductive'
    MATERNITY_AND_NEONATOLOGY = 'Maternity and neonatology'
    RESPIRATORY = 'Respiratory'
    IMMUNITY = 'Immunity'
    MUSCULOSKELETAL = 'Musculoskeletal'
    VISION = 'Vision'
    RENAL_AND_UROGENITAL = 'Renal and urogenital'
    ORAL_AND_GASTROINTESTINAL = 'Oral and Gastrointestinal'
    COGNITIVE_FUNCTION = 'Cognitive Function'
    HEARING = 'Hearing'
    OTHERS = 'Others'
    VACCINES = 'Vaccines'
    PREVENTIVE = 'Preventive'
    THERAPEUTIC = 'Therapeutic'
    # OTHERS = 'Others'
    LABORATORY = 'Laboratory'
    OTHER_DIAGNOSTICS = 'Other diagnostics'
    CT = 'CT'
    MRI = 'MRI'
    PET = 'PET'
    X_RAY = 'X-ray'
    ULTRASOUND = 'Ultrasound'
    PATHOLOGY = 'Pathology'
    # OTHERS = 'Others'
    HEAD = 'Head'
    CHEST = 'Chest'
    ARM = 'Arm'
    ABDOMEN = 'Abdomen'
    LEG = 'Leg'
    # OTHERS = 'Others'
    PROTEOMICS = 'Proteomics'
    TRANSCRIPTOMICS = 'Transcriptomics'
    EPIGENOMICS = 'Epigenomics'
    METABOLOMICS = 'Metabolomics'
    MULTIOMICS = 'Multiomics'
    METAGENOMICS = 'Metagenomics'
    GENOMICS = 'Genomics'
    # OTHERS = 'Others'
    EDUCATION = 'Education'
    CRIME_AND_JUSTICE = 'Crime and Justice'
    ETHNICITY = 'Ethnicity'
    HOUSING_ = 'Housing '
    LABOUR = 'Labour'
    AGEING_ = 'Ageing '
    ECONOMICS = 'Economics'
    MARITAL_STATUS = 'Marital status'
    SOCIAL_SUPPORT = 'Social support'
    DEPRIVATION = 'Deprivation'
    RELIGION = 'Religion'
    OCCUPATION = 'Occupation'
    FINANCES = 'Finances'
    FAMILY_CIRCUMSTANCE = 'Family circumstance'
    # OTHERS = 'Others'
    SMOKING = 'Smoking'
    PHYSICAL_ACTIVITY = 'Physical Activity'
    DIETARY_HABITS = 'Dietary habits'
    ALCOHOL = 'Alcohol'
    # OTHERS = 'Others'
    DISEASE_REGISTRY_RESEARCH = 'Disease Registry (research)'
    NATIONAL_DISEASE_REGISTRIES_AND_AUDITS = 'National Disease Registries and Audits'
    BIRTHS_AND_DEATHS = 'Births and Deaths'
    # OTHERS = 'Others'