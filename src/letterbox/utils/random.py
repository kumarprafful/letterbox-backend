import base64
import random
import string
import uuid


def generate_random_id(prefix=""):
    encoded = base64.urlsafe_b64encode(uuid.uuid4().bytes)
    return prefix + encoded.rstrip(b"=").decode('ascii')


def random_alpha_id(count=8):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(count))
