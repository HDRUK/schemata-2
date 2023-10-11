from pydantic import ValidationError
import v2_1_2
import json

v2_1_2.Hdruk212.save_schema()


metadata = json.load(open('2.1.2/example.json'))

try:
    v2_1_2.Hdruk212(**metadata)
except ValidationError as e:
    print(e)


