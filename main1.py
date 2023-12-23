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
            return f"{url} returned status code {response.status_code}."
    except requests.exceptions.RequestException as err:
        return f"Error occurred while checking {url}: {err}"

base_url = "https://172.16.43.202"
http_base_url = "http://172.16.43.202"
alternate_base_url = "https://172.16.43.245"  # Add your alternate host IP here
ports = [44301, 44302, 44303 ,44304,44305,44306,9407,9408,9409,44310,44311,44315,44316,
         44317,44318,44319,44325,44324,44320,15672,44321,44323,44326,44341]  # Add your ports here

for port in ports:
    urls = [f"{base_url}:{port}", f"{http_base_url}:{port}", f"{alternate_base_url}:{port}"]
    results = [check_url(url) for url in urls]
    if not any(result is True for result in results):
        print(f"Error occurred while checking all conditions for port {port}...")
        print("\n".join(str(result) for result in results if result is not True))
