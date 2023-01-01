req = __import__("requests")
async def app(scope,receive,send):
    res = req.get("https://58yr01.deta.dev"+scope["path"]+"?"+scope["query_string"].decode(),cookies={i[0]:i[1] for i in [i.split("=") for i in [i[1] for i in scope["headers"] if i[0] == b"cookie"][0].decode().split(";")]})
    await send({'type': 'http.response.start','status': res.status_code,'headers': [(b'content-type', res.headers['content-type'].encode()),(b'content-length', str(len(res.content)).encode()),]})
    await send({'type': 'http.response.body','body': res.content})
