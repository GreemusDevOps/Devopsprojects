string = "elephantridesabike"
res = {x: string.count(x) for x in set(string)}
print("/n occurrence of all characters in elephant rides a bike is : " , str(res))
