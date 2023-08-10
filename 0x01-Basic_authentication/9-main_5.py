#!/usr/bin/python3
""" Check response
"""

if __name__ == "__main__":
    from api.v1.auth.basic_auth import BasicAuth
    from models.user import User

    """ Create a user test """
    user_email = "u2@gmail.com"
    user_clear_pwd = "pwd2"
    user = User()
    user.email = user_email
    user.password = user_clear_pwd
    user.save()

    ba = BasicAuth()
    res = ba.user_object_from_credentials(user_email, "pwd")
    if res is not None:
        print("user_object_from_credentials must return None if 'user_pwd' is not the right password for an existing password")
        exit(1)
    
    print("OK", end="")
