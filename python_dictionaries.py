# Exercise 1
# f_handle = open("mbox-txt")
# dict_days = {}
# for line in f_handle:
#     if "From " in line:
#         print(line)
#         words = line.split()
#         dict_days[words[2]] = dict_days.get(words[2], 0) + 1
#
# print(dict_days)

#Exercise 2

f_handle = open("mbox-txt")
dict_from = {}
for line in f_handle:
    if "From:" in line:
        words = line.split()
        # print(words)
        dict_from[words[1]] = dict_from.get(words[1], 0) + 1

print(dict_from)