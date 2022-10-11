import re
import sys



Zpattern = r'Z[0-9]*[.,]?\D?[0-9]*[.,]?[0-9]'
floatpattern = r'[0-9]*[.,]?[0-9]'
index = 0

with open(sys.argv[1], 'r') as file:
    Lines = file.readlines()
    file.close()

print(f'Increase Z position in {sys.argv[2]} points:')
for line in Lines:
    Zbuf=re.search(Zpattern,line)
    if Zbuf is not None:
        num = re.search(floatpattern,Zbuf[0])
        print(f"{Zbuf[0]} num = {num[0]}")
        try:
            str_num = int(num[0])
        except:
            str_num = float(num[0])
        try:
            str_num += int(sys.argv[2])
        except:
            str_num = round(str_num + float(sys.argv[2]),2)
        tmp = Zbuf[0]
        tmp = tmp.replace(num[0], str(str_num))
        print(f"Old str = {Zbuf[0]} new num = {str_num} new str = {tmp}")

        Lines[index] = line.replace(Zbuf[0], tmp)
        print(Lines[index])
    index += 1

with open(sys.argv[1], 'w') as file:
    # Writing the replaced data in our
    # text file
    file.writelines(Lines)
    file.close()
