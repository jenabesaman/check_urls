import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def check_url(url):
    try:
        response = requests.get(url, verify=False)
        if response.status_code in [403, 404]:
            response = requests.get(url + "/swagger", verify=False)
        if response.status_code == 200:
            return True
        else:
            return response.status_code
    except requests.exceptions.RequestException as err:
        return "disabled"

base_url = "https://172.16.43.202"
http_base_url = "http://172.16.43.202"
alternate_base_url = "https://172.16.43.245"  # Add your alternate host IP here
ports = [44349]  # Add your ports here

def check_ports():
    output = {}  # Dictionary to store all outputs
    for port in ports:
        urls = [f"{base_url}:{port}", f"{http_base_url}:{port}", f"{alternate_base_url}:{port}"]
        results = [check_url(url) for url in urls]
        if not any(result is True for result in results):
            output[port] = results
    return output

print(check_ports())
