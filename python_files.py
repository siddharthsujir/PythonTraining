## Exercise 1

# fhandle = open("mbox-txt")
# for line in fhandle:
#     print(line.rstrip().upper())

# Exercise 2

filename = input("Enter the filename!")
if filename == "na na boo boo":
    print("NA NA BOO BOO TO YOU!")
    quit()
try:
    fhand = open(filename)
except:
    print("file Doesnt exist")
    quit()

str_to_search = 'X-DSPAM-Confidence:'
count = 0
confidence = 0.0
for line in fhand:
    if str_to_search in line:
        pos = line.find(":")
        val = line[pos + 1:len(line)]
        # print(val)
        confidence += float(val.strip())
        count += 1

avg_confidence = confidence / count
print("Average spam confidence: " + str(avg_confidence))
