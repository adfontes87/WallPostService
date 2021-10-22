# pip install vk
# pip install facebook-sdk

import vk
import facebook
import sys

msg = input("Введите сообщение: ")
msg = msg[:140]

# Параметры доступа к ВКонтакте
vk_app_id, vk_login, vk_password = 'vk_app_id', 'vk_login', 'vk_password'

try:
    session = vk.AuthSession(vk_app_id, vk_login, vk_password, scope='wall, message')
except vk.exceptions.VkAuthError:
    print("Ошибка авторизации во ВКонтакте!")
else:
    print("Неизвестная ошибка при авторизации во ВКонтакте!")
finally:
    sys.exit()
    
vk_api = vk.API(session, v='5.131')

try:
    vk_api.wall.post(message=msg)
except vk.exceptions.VkApiError:
    print("Ошибка отправки сообщения на стену ВКонтакте!")
else:
    print("Неизвестная ошибка отправки сообщения на стену ВКонтакте!")
finally:
    sys.exit()

print("Cообщение на стену ВКонтакте отправлено успешно!")

# Параметры доступа к Facebook
fb_access_token = 'fb_access_token'

graph = facebook.GraphAPI(access_token=fb_access_token)

try:
    graph.put_object("me", "feed", message=msg)
except GraphAPIError:
    print("Ошибка отправки сообщения на стену Facebook!")
else:
    print("Неизвестная ошибка отправки сообщения на стену Facebook!")
finally:
    sys.exit()

print("Cообщение на стену Facebook отправлено успешно!")
