import requests


token = 'CoTZgWn6TlieNiUxNyzrJQNWmZXgiAGH6TdUNha6'

avito_url = 'https://api.avito.ru/messenger/v2/webhook'
ngrok_url = 'http://790ede86485c.ngrok.io/'

headers = {'Authorization': f'Bearer {token}'}
body = {'url': ngrok_url}

res = requests.post(avito_url, data=body, headers=headers)
print(res)
print(res.text)

# url = 'https://api.avito.ru/token/?grant_type=client_credentials&client_id=BZ1AT8wQnAQ_k1Q7wkDT&client_secret=mIMbN15nyYf-5Qb0UVfC5ST-Qyv0I12q_A8o7qZY'
# resp = requests.get(url)
# print(resp.text)