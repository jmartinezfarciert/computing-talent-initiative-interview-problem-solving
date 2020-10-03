# Author : Johnny Martinez
# Desc : taking a tedious computer architecture quiz that must be submitted if __name__ == '__main__':
# plain text. Had a table format boolean expression table that i had to convert
# from a long string to neatly formatted with break points.
# Open a file
fo = open("lab.txt", "r+") #r+ opens for reading and writing
str = fo.read()
print ("Read String is : ", str)
a = str.split()
print(a)

n = 5
a = [str[i:i+n] for i in range(0, len(str), n)]
print(a)
for s in a :
    fo.write(s + "\n")
fo.close()
