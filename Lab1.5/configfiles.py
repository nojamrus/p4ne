import glob

list_files=glob.glob(r"C:\t\Seafile\Seafile\p4ne_training\config_files\*.txt")

res_list=[]
for one_file in list_files:
    f= open (one_file)
    lines = f.readlines()
    for one_line in lines:
        ret=str.find(one_line,'ip address ')
        if ret!=-1 and ret==1:
            one_line = str.strip(one_line)
            res_list.append(one_line)
    f.close()

unique_res=sorted(list(set(res_list)))
for one_res in unique_res:
    print (one_res)
