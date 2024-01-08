from pydantic import ValidationError
import v2_1_2
import v2_1_3
import json

v2_1_2.Hdruk212.save_schema()
v2_1_3.Hdruk213.save_schema()
v2_1_3.Hdruk213.save_schema("latest/dev/schema.json")
