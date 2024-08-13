from pydantic import BaseModel
from enum import Enum

class AgeBin(Enum):
    DAYS_0_6 = '0-6 days'
    DAYS_7_27 = '7-27 days'
    MONTHS_1_11 = '1-11 months'
    YEARS_1_4 = '1-4 years'
    YEARS_5_9 = '5-9 years'
    YEARS_10_14 = '10-14 years'
    YEARS_15_19 = '15-19 years'
    YEARS_20_14 = '20-14 years'
    YEARS_25_29 = '25-29 years'
    YEARS_30_34 = '30-34 years'
    YEARS_35_39 = '35-39 years'
    YEARS_40_44 = '40-44 years'
    YEARS_45_49 = '45-49 years'
    YEARS_50_54 = '50-54 years'
    YEARS_55_59 = '55-59 years'
    YEARS_60_64 = '60-64 years'
    YEARS_65_69 = '65-69 years'
    YEARS_70_74 = '70-74 years'
    YEARS_75_79 = '75-79 years'
    YEARS_80_84 = '80-84 years'
    YEARS_85_89 = '85-89 years'
    YEARS_90_94 = '90-94 years'
    YEARS_65_99 = '65-99 years'
    YEARS_100_PLUS = '100+ years'

class Age(BaseModel):
    bin: AgeBin
    count: int

