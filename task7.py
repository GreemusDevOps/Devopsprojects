person = {"name": "swathi","age": 30,"city": "Bangalore"}
print("Person's information:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")
person["occupation"] = "HR"
print("\nPerson's updated information:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")
