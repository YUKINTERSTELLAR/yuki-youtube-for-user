import requests
url = requests.get(r'https://raw.githubusercontent.com/mochidukiyukimi/yuki-youtube-instance/main/instance.txt')
async def app(scope,receive,send):
    global url
    if (cookies := [i[1] for i in scope["headers"] if i[0] == b"cookie"]) and "yuki=True" in cookies[0].decode():
        res = requests.get("url"+scope["path"]+"?"+scope["query_string"].decode(),cookies={i[0]:i[1] for i in [i.split("=") for i in [i[1] for i in scope["headers"] if i[0] == b"cookie"][0].decode().split(";")]})
    else:
        res = requests.get("url"+scope["path"]+"?"+scope["query_string"].decode())
    await send({'type': 'http.response.start','status': res.status_code,'headers': [(i[0].encode(),i[1].encode()) for i in res.headers.items()]})
    await send({'type': 'http.response.body','body': res.content})