Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict = {1: "going", 2: "to", 3: "school"}
print(Dict)
Dict = {'Name': "going", 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)
Dict = {1: "going", 2: "to",
        3: {'A': "say hello", 'B': "To", 'C': "sasi"}}
print(Dict)
Dict[0] = "going"
Dict[1]="to"
Dict[2] = "school"
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)
Dict = {1: "going", 'name': 'to', 3: 'school'}
print("Accessing a element using key:")
print(Dict['name'])
print("Accessing a element using key:")
print(Dict[1])