keys = ["car", "bike", "aeroplane"]
values = [1, 2, 3]
res = {}
for key in keys:
	for value in values:
		res[key] = value
		values.remove(value)
		break
print("Resultant dictionary is : " ,res)