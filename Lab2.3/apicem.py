import requests, json, pprint
import flask

def new_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser","password": "Cisco123!"}
    header = {"content-type": "application/json"}
    response = requests.post(url, data=json.dumps(payload),headers=header, verify=False)
    return response.json()['response']['serviceTicket']

if __name__ == '__main__':
    ticket = new_ticket()
    controller = "devnetapi.cisco.com/sandbox/apic_em"
    url_hosts = "https://" + controller + "/api/v1/host"
    header = {"content-type": "application/json","X-Auth-Token":ticket}
    responce_test = requests.get(url_hosts, headers=header, verify=False)
    ##print("Hosts = ")
    ##pprint.pprint(json.dumps(responce_test.json()))
    url_network_device = "https://" + controller + "/api/v1/network-device"
    responce_network_device = requests.get(url_network_device, headers=header, verify=False)
    ##print("network_devices = ")
    ##pprint.pprint(json.dumps(responce_network_device.json()))

    url_physical_topology = "https://" + controller + "/api/v1/topology/physical-topology"
    responce_physical_topology = requests.get(url_physical_topology, headers=header, verify=False)
    ##print("physical_topology = ")
    ##pprint.pprint(json.dumps(responce_physical_topology.json()))

app = flask.Flask(__name__)
@app.route("/")
def index():
    return flask.render_template("topology.html")

@app.route('/api/topology')
def response():
    return flask.jsonify(responce_physical_topology.json()['response'])

if __name__ == '__main__':
    app.run(debug=True)