import redis 
r = redis.Redis(decode_responses=True)
print(r.ping())
#melakukan set key dan get key 
r.set("ramma1", "hallo ramma")
print(r.get("ramma1"))
#melakukan multiple set dan get
data = {
    "ramma1": "hallo ramma1",
    "ramma2": "hallo ramma2"
}
r.mset(data)
print("1.", r.get("ramma1"), "2.", r.get("ramma2"), "3.", r.mget("ramma1", "ramma2"))