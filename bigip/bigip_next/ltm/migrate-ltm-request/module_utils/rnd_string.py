import random
import string

def rnd_string(length):
    random = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(length)])
    return random
