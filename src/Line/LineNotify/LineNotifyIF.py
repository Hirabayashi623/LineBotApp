import requests

# 発行したトークンを指定
line_notify_token = 'KjRlCxnU73OC8bv8xo5bke8WHcbQrvsShuRX2dVVQad'

# LINE通知APIのパスを指定
line_notify_api = 'https://notify-api.line.me/api/notify'

def notify(message):
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)

def sendPicture(targetPath):
    payload = {'imageFile': targetPath, 'message': '写真'}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)
