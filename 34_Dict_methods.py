# Dictionary Methods
# The update() method updates the value of the key provided to it 

user_data ={"name":"Nitin",
        "age":"13",
        "gender":"male",
        "condition":"retarted"

}
print(user_data)

user_data.update({"age":"23"})
user_data.update({'status':"Unknown"})
print(user_data)

# clear()
# user_data.clear()
# print(user_data)

# pop()
user_data.pop('status')
print(user_data)

# popitem() pop the last item from dictionary
user_data.popitem()
print(user_data)

# del()
del user_data['name']
print(user_data)

del user_data
print(user_data)
# deletes the whole dict