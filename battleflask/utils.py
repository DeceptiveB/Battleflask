from battleflask.auth import users

def get_user_by_username(username):
    for u in users:
        if u.name == username:
            return user
