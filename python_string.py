str = 'X-DSPAM-Confidence:0.8475'
pos = str.find(':')
stripped_string = str[pos+1:len(str)]
print(stripped_string)
float_num = float(stripped_string)
print(float_num)
