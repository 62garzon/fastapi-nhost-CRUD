import logging
from datetime import timedelta
from itsdangerous import URLSafeTimedSerializer

import jwt
from passlib.context import CryptContext

from src.config import Config

passwd_context = CryptContext(schemes=["bcrypt"])

ACCESS_TOKEN_EXPIRY = 900


def generate_passwd_hash(password: str) -> str:
    hash = passwd_context.hash(password)

    return hash


def verify_password(password: str, hash: str) -> bool:
    return passwd_context.verify(password, hash)


def create_access_token(
        user_data: dict, expiry: timedelta = None, refresh: bool = False
):
    pass


def encode_token(payload):
    token = jwt.encode(
        payload=payload, key=Config.JWT_SECRET, algorithm=Config.JWT_ALGORITHM
    )

    return token


def decode_token(token: str) -> dict:
    try:
        token_data = jwt.decode(
            jwt=token, key=Config.JWT_SECRET, algorithms=[Config.JWT_ALGORITHM]
        )

        return token_data

    except jwt.PyJWTError as e:
        logging.exception(e)
        return None


serializer = URLSafeTimedSerializer(
    secret_key=Config.JWT_SECRET, salt="email-configuration"
)


def create_url_safe_token(data: dict):
    token = serializer.dumps(data)

    return token


def decode_url_safe_token(token: str):
    try:
        token_data = serializer.loads(token)

        return token_data

    except Exception as e:
        logging.error(str(e))
