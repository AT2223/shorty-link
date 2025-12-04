fake_db = {}

def save_link(code, data):
    fake_db[code] = data

def get_link(code):
    return fake_db.get(code)