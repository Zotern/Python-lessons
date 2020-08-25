import json
import pickle
import urllib.request

# объект
json_obj = '''
{"a1": 1, "b": "text"}
'''

json_array = '''[1, 2, "text"]'''

json_str = '''"text"'''

json_compl_obj = '''
{
    "a": {"b": [1,2,3]},
    "d": "text",
    "e": 0
}
'''

objects = [json_obj, json_array, json_str, json_compl_obj]
for json_obj in objects:
    py_obj = json.loads(json_obj)
    print("json_obj", json_obj)
    print("py_obj", type(py_obj), py_obj)
    print("new_json_obj", json.dumps(py_obj))


r = urllib.request.urlopen("https://zpool.ca/site/api")
print(r.headers)

print(r.read())
d = json.load(r)
print(d)
