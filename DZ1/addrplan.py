import glob
import re
import ipaddress

def r_str(x):
    # ip address 10.12.234.114 255.255.255.128
    #ip = re.match("^ ip address (.+?) (.+?$)", x)
    ip = re.match("^ ip address (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", x)
    if ip:
        return (str(ip.group(1)), str(ip.group(2)))
    else:
        return False
list_2address={}
list_files=glob.glob(r"C:\t\Seafile\Seafile\p4ne_training\config_files\*.txt")
for one_file in list_files:
    f= open (one_file)
    lines = f.readlines()
    for one_line in lines:
        ret_str=r_str(one_line)
        if ret_str is not False: list_2address[ret_str[0]] = ret_str[1]
    f.close()
list_for_remove=list_2address
print ("IPADDRESS\t\t\t\tMASK\t\t\tGATAWAY")
for one_2address in list_2address.keys():
    etalon_netmask = "%s/%s" % (one_2address, list_2address[one_2address])
    for one_for_remove in list_for_remove.keys():
        check_netmask= "%s/%s" % (one_for_remove, list_for_remove[one_for_remove])
        if ipaddress.ip_address(one_for_remove) in ipaddress.ip_network(etalon_netmask,strict=False):
            print ("%s\t\t\t%s\t\t\t%s" % (one_2address, list_2address[one_2address], one_for_remove))
            print("%s\t\t\t%s\t\t\t%s" % (one_for_remove, list_for_remove[one_for_remove], one_2address))
            break



