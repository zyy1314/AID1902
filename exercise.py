import re,sys
data = input()
f = open('1.txt', 'r')
conntent = f.read()
pattern = r'\n\n'
obj = re.split(pattern, conntent)
for i in obj:
    pattern = r"\S+"
    data1 = re.match(pattern, i).group()
    if data == data1:
        pattern = r"address is .+|Unknown"
        value = re.findall(pattern, i)
        print("address is:", value[0], '\n', "Internet ", value[1])
        break
    else:
        print('meiyous')

f.close()
ni mei
