# dictionaries

info = {"name":"Nitin",
        "age":"13",
        "gender":"male",
        "condition":"retarted"

}

a = "name"
print(info[a])
print(info.get("name"))
print(info.keys())
print(info.items())
print(info.values())

for key, value in info.items():
    print(key, ":", value)
    print(f"This entity {key} is {value}")

