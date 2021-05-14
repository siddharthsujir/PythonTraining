# Excerise 1
# file_handle = open("romeo")
# unique_list = []
# for line in file_handle:
#     line = line.strip()
#     line_list = line.split()
#     for word in line_list:
#         if word not in unique_list:
#             unique_list.append(word)
#
# unique_list.sort()
#
# for item in unique_list:
#     print(item)

## Exercise 2

# file_handle = open("mbox-txt")
# for line in file_handle:
#     if "From" in line:
#         list_name = line.split()
#         print(list_name[1])

## Exercise 3
list_no = []
while 1 == 1:
    input_no = input("Enter a number. Press 'done' to end")
    if input_no == 'done':
        break
    list_no.append(int(input_no))

list_no.sort()

print("Minimum - "+str(list_no[0]))
print("Maximum - "+str(list_no[len(list_no)-1]))



