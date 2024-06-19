person = {
    "name": "Sasi",
    "age": 27,
    "city": "Hyderabad"
}
# Print the person's information
print("Person's Information:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")
    # Add a new attribute (occupation) to the dictionary
person["occupation"] = "Engineer"
# Print the updated person's information
print("\nPerson's Information after adding occupation:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")