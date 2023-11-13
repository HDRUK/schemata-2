from pydantic import ValidationError
from v1_0 import Gwdm10
from v1_1 import Gwdm11
import json

Gwdm10.save_schema('1.0/schema.json')
Gwdm11.save_schema('1.1/schema.json')
Gwdm11.save_schema('latest/schema.json')


