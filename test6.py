def Dictionary_Comprehension(keys, values):
    return {keys[i]: values[i] for i in range(len(keys))}
keys = ["sn", "id", "pin"]
values = [1, 222, 515701]
result = Dictionary_Comprehension(keys, values)
print (result)

