from my_auth.models import User
CHARS_CUONTITY = 8

def make_randome_str():
    import string
    import random

    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits

    return ''.join(random.choice(chars) for _ in range(CHARS_CUONTITY))

def check_user(strategy, details, response, user, *args, **kwargs):
    email = details['email']

    if User.objects.filter(user_mail=email).exists():
        pass
    else:
        new_user = User(
            user_mail = email,
            username = details['fullname'],
            password = make_randome_str(),
        )
        new_user.save()

    return kwargs
