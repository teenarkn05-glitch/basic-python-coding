lst = [4,5,5,3,5,6,7,4,3,6]
non_rep = [x for x in lst if lst.count(x) == 1]
print(non_rep)
