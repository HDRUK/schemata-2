from pydantic import Field
from hdr_schemata.definitions.HDRUK import Periodicity
from hdr_schemata.models.HDRUK.base.Temporal import Temporal as BaseTemporal
from pydantic import BaseModel, Field
from hdr_schemata.models import remove_fields_from_cls


class Temporal(BaseTemporal):
    publishingFrequency: Periodicity = Field(
        ...,
        title="Publishing Frequency",
        description="Please indicate the frequency of distribution release. If a dataset is distributed regularly please choose a distribution release periodicity from the constrained list and indicate the next release date. When the release date becomes historical, a new release date will be calculated based on the publishing periodicity. If a dataset has been published and will remain static please indicate that it is static and indicated when it was released. If a dataset is released on an irregular basis or “on-demand” please indicate that it is Irregular and leave release date as null. If a dataset can be published in real-time or near-real-time please indicate that it is continuous and leave release date as null. Notes: see https://www.dublincore.org/specifications/dublin-core/collection-description/frequency/",
    )


remove_fields_from_cls(Temporal, ["accrualPeriodicity"])
