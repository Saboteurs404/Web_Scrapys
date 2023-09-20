import requests
import json


def main():

    api_key = ''
    secret_key = ''
    token_url = ''

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=B0e0VCFqQUrFWXAtXKfdfsnb&client_secret=rhaNNFhGWrLqVSQfD3stPzUzRoo8rG5G"

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    main()