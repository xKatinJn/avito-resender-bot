import requests


token = 'BLQRDV1VQ1OndgG56vkIKwxDfZ4cQHn3F9jD7k6C'

avito_url = 'https://api.avito.ru/messenger/v2/webhook'
ngrok_url = 'http://89.108.88.69:5000/notifications_webhook'

headers = {'Authorization': f'Bearer {token}'}
body = {'url': ngrok_url}

res = requests.post(avito_url, data=body, headers=headers)
print(res)
print(res.text)

# url = 'https://api.avito.ru/token/?grant_type=client_credentials&client_id=BZ1AT8wQnAQ_k1Q7wkDT&client_secret=mIMbN15nyYf-5Qb0UVfC5ST-Qyv0I12q_A8o7qZY'
# resp = requests.get(url)
# print(resp.text)