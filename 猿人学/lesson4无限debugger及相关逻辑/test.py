import base64

for page in range(1, 5):
    token = base64.b64encode(str(page).encode()).decode()
    data = {'page': page,
            'token': token
            }
    print(data)