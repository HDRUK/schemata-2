from hdr_schemata.models.HDRUK.base import Provenance as BaseProvenance
from .Temporal import Temporal


class Provenance(BaseProvenance):
    temporal: Temporal
