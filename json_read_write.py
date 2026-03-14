import json

# data
data = {
    "name": "Venky",
    "age": 21,
    "course": "Python"
}

# write json file
with open("student.json","w") as f:
    json.dump(data,f)

print("JSON file created")

# read json file
with open("student.json","r") as f:
    d = json.load(f)

print("JSON data:",d)
print("Name:",d["name"])
print("Course:",d["course"])