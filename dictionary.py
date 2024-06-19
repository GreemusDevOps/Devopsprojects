person = {
    "name": "Sasi",
    "age": 27,
    "city": "Hyderabad"
}
print("Person's Information:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")
person["occupation"] = "Engineer"
print("\nPerson's Information after adding occupation:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")
