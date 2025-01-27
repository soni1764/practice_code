import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
from requests_oauthlib import OAuth1


# -----------------------Get request--------------------
def get_api_without_auth():
    response = requests.get("https://www.google.com/")
    print(response.status_code)
    assert response.status_code == 200

    if response.status_code == 200:
        print(response.headers)
        print(response.headers['Content-Type'])
        print(response.encoding)
        print(response.text)
        assert 'text/html' in response.headers['Content-Type']
        # data = response.json()
        # print(data)


def get_api_with_auth():
    auth = ('user', 'password')
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.status_code)
    assert response.status_code == 200
    # data = response.json()
    # print(data)


def get_api_with_basicauth():
    user = ''
    password = ''
    response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth(user, password))
    print(response.status_code)
    assert response.status_code == 200
    # data = res.json()
    # print(data)


def get_api_with_digestauth():
    user = ''
    password = ''
    response = requests.get("https://api.github.com/user", auth=HTTPDigestAuth(user, password))
    print(response.status_code)
    assert response.status_code == 200
    # data = res.json()
    # print(data)


def get_api_with_bearer_token():
    url = 'https://api.example.com/data'
    api_key_or_token = ''
    header = {
        'Authorization': f'Bearer {api_key_or_token}'
    }
    response = requests.get(url=url, headers=header)
    print(response.status_code)
    assert response.status_code == 200
    # data = res.json()
    # print(data)


def get_api_with_apikey():
    # using query parameter
    api_key = 'your_api_key'
    url = f'https://api.example.com/data?api_key={api_key}'
    response = requests.get(url)
    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing the response JSON
        data = response.json()
        print(data)
    else:
        print(f"Failed to retrieve data: {response.status_code}")

    # ----------other way-------
    header = {
        'Authorization': f'Api-Key {api_key}'
    }
    response = requests.get(url=url, headers=header)
    if response.status_code == 200:
        # Parsing the response JSON
        data = response.json()
        print(data)
    else:
        print(f"Failed to retrieve data: {response.status_code}")


def get_api_with_oauth1():
    url = 'https://api.example.com/data'
    client_key = 'your_client_key'
    client_secret = 'your_client_secret'
    resource_owner_key = 'your_resource_owner_key'
    resource_owner_secret = 'your_resource_owner_secret'
    auth = OAuth1(client_key, client_secret, resource_owner_key, resource_owner_secret)
    response = requests.get(url=url, auth=auth)
    print(response.status_code)
    assert response.status_code == 200
    # data = response.json()
    # print(data)


def get_api_with_oauth2():
    token_url = 'https://authorization-server.com/token'
    # Your client credentials
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    # The resource you want to access
    resource_url = 'https://api.example.com/data'

    # Data for the token request
    token_data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    # Requesting the access token
    token_response = requests.post(token_url, data=token_data)

    if token_response.status_code == 200:
        access_token = token_response.json().get('access_token')

        # Headers including the authorization token
        header = {
            'Authorization': f'Bearer {access_token}'
        }
        # Sending a GET request with the access token
        response = requests.get(resource_url, headers=header)

        # Checking if the request was successful
        if response.status_code == 200:
            # Parsing the response JSON
            data = response.json()
            print(data)
        else:
            print(f"Failed to retrieve data: {response.status_code}")
    else:
        print(f"Failed to obtain access token: {token_response.status_code}")


def get_api_with_session():
    session = requests.session()
    header = {'content-type': 'application\json'}
    session.headers.update(header)
    response = session.get("url")

    # with basic auth
    auth = ("user", "pass")
    session.auth = auth

    # with http basic auth
    session.auth = HTTPBasicAuth('user', 'password')
    response = session.get('url')

    # with bearer auth
    header = {
        'content-type': 'application\json',
        'Authorization': f'Bearer your_bearer_token'
            }

    session.headers.update(header)
    session.get('url')

    # with access key auth
    header = {
        'content-type': 'application\json',
        'Authorization': f'Bearer your_access_key'
            }

    session.headers.update(header)
    session.get('url')


