import json

data = {}

data['user'] = []
data['user'].append({
    'email': 'sadfas',
    'pass': 'asdfas',
    'uid': ''
})

with open('login.txt', 'w') as file:
    json.dump(data, file)

with open('login.txt') as json_file:
    data = json.load(json_file)
    for p in data['user']:
        if p['email'] == "":
            print('email is empty')
        if p['pass'] == "":
            print('pass is empty')
