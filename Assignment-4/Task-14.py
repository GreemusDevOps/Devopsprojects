#sorting tuples
def sortingtuple(tuple):
    tuple.sort(key = lambda x: x[1])
    return tuple
tuple = [("Durga",105), ("Devi",101), ("Pavan",104), ("satya",103)]
print("Sorted tuple :",sortingtuple(tuple))