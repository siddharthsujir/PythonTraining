def palindromenumber(no: int):
    val = no
    if no < 0:
        return False
    else:
        reverseNo = 0
        sum = 0
        while no >= 1:
            t = int(no) % 10
            sum = (int(sum) * 10) + t
            no = int(no) / int(10)

        #print(sum)
        if sum == val:
            return True
        else:
            return False


print(palindromenumber(101))

