import yaml

data = {
    "name": "Venky",
    "age": 21,
    "course": "Python"
}

# write yaml file
with open("student.yaml","w") as f:
    yaml.dump(data,f)

print("YAML file created")

# read yaml file
with open("student.yaml","r") as f:
    d = yaml.safe_load(f)

print("YAML data:",d)
print("Name:",d["name"])
print("Course:",d["course"])