def reverseInteger(x: int) -> int:
    sum1 = 0
    if not isinstance(x, int):
        return 0
    negFlag = False
    if x > 0:
        negFlag = False
    else:
        negFlag = True
        x = x * -1;
    while x >= 1:
        t = int(x) % 10
        #print("Mod" + str(t))
        sum1 = (sum1 * 10) + t
        x = int(x)/int(10)

    if sum1 > 2147483647 or sum1 < -2147483647:
        return 0

    if negFlag:
        return sum1 * -1
    else:
        return sum1

#9646324351
#2147483647
print(reverseInteger(1534236469))
