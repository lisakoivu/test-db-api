#!/usr/bin/env python
from faker import Faker
import json
fake = Faker()

data = {}


for i in range(50):
    data[i] = {}
    data[i]['email'] = fake.ascii_company_email()
    data[i]['address'] = fake.address()
    data[i]['uri'] = fake.uri()
    data[i]['latlng'] = fake.local_latlng(country_code='US')

# data_str = json.dump(data)

with open("db.json" , "w") as outfile:
    json.dump(data, outfile)