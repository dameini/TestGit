
file = open("C:/Users/10291/Desktop/LBCM_PrEP_ForAr_ASWC.c",'r+')
# print(file)

text_lines = file.readlines()
# print(text_lines)
for line in text_lines:
    if '/*' in line:
        if 'I/O' in line:
            print(text_lines.index(line))
            print(line)

file.close()
