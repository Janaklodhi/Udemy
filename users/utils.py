import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import User

# Get the secret key from settings
SECRET_KEY = settings.SECRET_KEY

def create_jwt_token(user):
    """
    Create JWT token for a given user.
    """
    payload = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'exp': datetime.utcnow() + timedelta(hours=24),  # Token expiration
        'iat': datetime.utcnow(),  # Issued at
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def decode_jwt_token(token):
    """
    Decode JWT token to verify its validity and extract the payload.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}
