# redis dan json 
import json 
import redis 
r = redis.Redis(decode_responses=True)
print(r.ping())

data = {
    'nama':'ramma', 
    'usia': 30,
    'alamat': {
        'kota': 'jakarta barat'
    },
    'bahasa program': ['python','C++','javascript']
}

set_key1 = r.set("data", json.dumps(data))
print(set_key1)
get_key1 = r.get("data")
json_load = json.loads(get_key1)
print(json_load)