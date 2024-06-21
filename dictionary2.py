dictionary = {}
print("empty dictionary: ")
print(dictionary)
dictionary = {1: 'going', 2: 'to', 3: 'school'}
print("\ndictionary with the use of integer keys: ")
print(dictionary)
dictionary1 = {'name': 'sasi', 1: [1, 2, 3, 4]}
print("\ndictionary with the use of mixed keys: ")
print(dictionary1)
dictionary2 = dict({1: 'going ', 2: 'to', 3: 'school'})
print("\ndictionary with the use of dict():dictionary2 ")
print(dictionary2)
dictionary3 = dict([(1, 'Geeks'), (2, 'For')])
print("\ndictionary with each item as a pair:dictionary3 ")
print(dictionary3)
dictionary4= {1: 'going', 2: 'to',
        3: {'A': 'say hello', 'B': 'to', 'C': 'world'}}
print("\ndictionary with multi level keys:dictionary4 ")
print(dictionary4)
dictionary5={}
print("empty dictionary:dictionary5")
print(dictionary5)
dictionary5[0] = 'hello'
dictionary5[1]='to'
dictionary5[2] = 'world'
dictionary5[3] = 1
print("\ndictionary after adding 3 elements:dictionary5 ")
print(dictionary5)
dictionary5['Value_set'] = 2, 3, 4
print("\ndictionary after adding 3 elements:dictionary5 ")
print(dictionary5)
dictionary5[2] = 'thanks'
print("\nupdated key value: dictionary5")
print(dictionary5)
dictionary5[5] = {'nested': {'1': 'love', '2': 'life'}}
print("\nadding a nested key:dictionary5 ")
print(dictionary5)
dictionary6= {1: 'going', 'name': 'to', 3: 'school'}
print("accessing a element using key:dictionary6")
print(dictionary6['name'])
print("accessing a element using key:dictionary6")
print(dictionary6[3])
dictionary7= {1: 'abc', 'name': 'rides', 3: 'bike'}
print("accessing a element using get:dictionary7")
print(dictionary7.get(3))
dictionary8 = {'dictionary8.1': {1: 'rides'},
        'dictionary8.2': {'Name': 'bike'}}
print(dictionary8['dictionary8.1'])
print(dictionary8['dictionary8.1'][1])
print(dictionary8['dictionary8.2']['Name'])
dictionary9= {1: 'elephant', 'name': 'rides', 3: 'bike'}

print("dictionary 9=")
print(dictionary9)
del (dictionary9[1])
print("data after deletion dictionary=dictionary9")
print(dictionary9)
dictionary10 = {1: "car", 2: "bike", 3: "scooty", 4: "taxi"}
dictionary11 = dictionary10.copy()
print(dictionary11)
dictionary10.clear()
print(dictionary10)
print(dictionary11.get(1))
print(dictionary11.items())
print(dictionary11.keys())
dictionary11.pop(4)
print(dictionary11)
dictionary11.popitem()
print(dictionary11)
dictionary11.update({3: "taxi"})
print(dictionary11)
print(dictionary11.values())
