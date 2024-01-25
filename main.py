import requests
from requests.auth import HTTPProxyAuth

url = 'https://ipinfo.io/json'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# ==== PROXIES ====
proxy_list = [
    {'proxy': 'http://34.27.71.134:3128',
        'username': "developer", 'password': "test123"},
    # Add more proxies with their respective usernames and passwords
    # {'proxy': 'http://example_proxy:port', 'username': 'example_username', 'password': 'example_password'},
]
# =================


def test_proxy(proxy_info):
    proxy = proxy_info['proxy']
    username = proxy_info['username']
    password = proxy_info['password']

    proxies = {'http': proxy, 'https': proxy}
    auth = None

    # Check if username and password are provided
    if username and password:
        auth = HTTPProxyAuth(username, password)
        proxy = proxy.replace("http://", "")
        proxies = {'http': f'http://{username}:{password}@{proxy}',
                   'https': f'http://{username}:{password}@{proxy}'}
    else:
        auth = None

    print(proxies)
    try:
        response = requests.get(url, proxies=proxies,
                                headers=headers, auth=auth, timeout=5)
        if response.status_code == 200:
            print(f"Proxy {proxy} - IP Detected: {response.json()}")
        else:
            print(
                f"Proxy {proxy} - Request failed with status code {response.status_code}")
    except Exception as e:
        print(f"Proxy {proxy} - Error: {e}")


def main():
    # Current IP
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            print(f"Current IP Detected: {response.json()}")
        else:
            print(
                f"Current - Request failed with status code {response.status_code}")
    except Exception as e:
        print(f"Current - Error: {e}")

    for proxy_info in proxy_list:
        print("----------")
        test_proxy(proxy_info)


if __name__ == "__main__":
    main()
