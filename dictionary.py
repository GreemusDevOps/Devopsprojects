person={
    'name':'manu',
    'age':28,
    'city':'anantapur'
           }
for values in person:
    print(values)
person["occupation"]="devops"
print('afteradding occupation')
for values in person:
    print(values)

person={
    'name':'manu',
    'mail':'manu@greemus',
    'age':28,
}
for key,value in person.items():
    print(f"{key.capitalize()}: {value}")

 