import pickle

data = {
    "name": "Venky",
    "age": 21,
    "course": "Python"
}

# write object to file
with open("data.pkl","wb") as f:
    pickle.dump(data,f)

print("Object stored in file")

# read object from file
with open("data.pkl","rb") as f:
    d = pickle.load(f)

print("Object from file:",d)
print("Name:",d["name"])
print("Course:",d["course"])