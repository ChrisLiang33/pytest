import requests
databbase = {
    1:'allice',
    2:'bob',
    3:'laja'
}

def get_user_from_db(user_id):
    return databbase.get(user_id)

def get_users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    if response.status_code == 200:
        return response.json()
    raise requests.HTTPError