# x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
# y = x.items()
# print(y)


f_handle = open("mbox-txt")
dict_from = {}
for line in f_handle:
    if "From:" in line:
        words = line.split()
        # print(words)
        dict_from[words[1]] = dict_from.get(words[1], 0) + 1
list_tuple = []
for k, v in dict_from.items():
    list_tuple.append((v, k))

list_tuple.sort(reverse= True)
print(list_tuple)