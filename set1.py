set={'kumar',20,"hyderabad"}
set1={'sasi',28,"tirupati"}
print(set)
set1.update(set1)
print(set)

set={1,2,3,4}
set1={4,5,6,7}
union_set=set|set1
print("union_set:",union_set)

set={1,2,3,4}
set1={4,5,6,7}
intersection_set=set&set1
print("intersection_set:",intersection_set)