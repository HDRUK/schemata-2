from enum import Enum

class StatisticalPopulationConstrained(Enum):
    PERSONS = 'PERSONS'
    EVENTS = 'EVENTS'
    FINDINGS = 'FINDINGS'

class StatisticalPopulationConstrainedV2(Enum):
    PERSONS = 'Persons'
    EVENTS = 'Events'
    FINDINGS = 'Findings'
    NUMBER_OF_SCANS_PER_MODALITY = 'Number of scans per modality'
