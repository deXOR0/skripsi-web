import json

content = []
with open('location_data.json') as f:
    content = f.read()

data = json.loads(content)

print(data)

from .models import *

# seeder.add_entity(City, 1, {
#     'city_name': ''
# })

# inserted_pks = seeder.execute()