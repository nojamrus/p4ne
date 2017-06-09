import glob
import re

list_files=glob.glob(r"C:\t\Seafile\Seafile\p4ne_training\config_files\*.txt")

def classified(str):
    #(“IP”, адрес, маска) — для строк вида ip address 192.168.1.1 255.255.255.0
    test=re.match("^ip address (.+?) (.+)",str)
    if test:
        return ("IP", test.group(1,2))
    test = re.match("^interface (.+)",str)
    # (“INT”, имя) — для строк вида interface GigabitEthernet0
    if test:
        return ("INT", test.group(1))
    # (“HOST”, имя) — для строк вида hostname xxx
    test = re.match("^hostname (.+)", str)
    if test:
        return ("HOST", test.group(1))
    else:
        return ("UNCLASSIFIED",)


res_list=[]
for one_file in list_files:
    f= open (one_file)
    lines = f.readlines()
    for one_line in lines:
        print (classified(one_line))
    f.close()

