import flask
import sys


import glob
import re

list_files=glob.glob(r"C:\t\Seafile\Seafile\p4ne_training\config_files\*.txt")
def hostmane(str):
    test = re.match("^hostname (.+)", str)
    if test:
        ##print (test.group(1))
        return (test.group(1))
    else:
        return False

def ip(str):
    test=re.match("^ ip address (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",str)
    if test:
        return (test.group(1))
    else:
        return False

host_ip={}

for one_file in list_files:
    f= open (one_file)
    lines = f.readlines()
    for one_line in lines:
        host=hostmane(one_line)
        if (host) is not False:

            for oneip_line in lines:
                ip_host = ip(oneip_line)
                if (ip_host) is not False:
                    ##print (host,ip_host)
                    host_ip[host]=ip_host
    f.close()

app = flask.Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return "Если вы это читаете, вы что-то знаете :)"

@app.route('/python')
def python():
    return flask.jsonify(repr(sys.__dict__))

@app.route('/configs')
def configs():
    return flask.jsonify(repr(host_ip.keys()))
    

@app.route('/configs/<name>')
def confighostname(name):
    return flask.jsonify(repr(host_ip[name]))

if __name__ == '__main__':
    app.run(debug=True)