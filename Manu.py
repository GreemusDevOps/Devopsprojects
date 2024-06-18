person = {
    "name": "Manu",
    "age": 29,
    "city": "Hyderabad"
}
# Print the person's information
print("Person's Information:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")
    # Add a new attribute (occupation) to the dictionary
person["occupation"] = "Devops Engineer"
# Print the updated person's information
print("\nPerson's Information after adding occupation:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")


for i in range(1,11):
    print('7*',i,'=',7*i)

name='manu'
for i in range(1000):
    print(name)



