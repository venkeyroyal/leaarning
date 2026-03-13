import yaml

with open("config.yaml","r") as f:
    data = yaml.safe_load(f)

print(data)
print(data["application"]["name"])
print(data["database"]["type"])