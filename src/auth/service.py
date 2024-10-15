from .schemas import UserCreateModel, UserSignInModel
import requests
from src.config import Config


class UserService:

    async def create_user(self, user_data: UserCreateModel):
        url = f"{Config.NHOST_AUTH_URL}/signup/email-password"

        payload = {
            "email": f"{user_data.email}",
            "password": f"{user_data.password}",
            "options": {
                "allowedRoles": ["me", "user"],
                "defaultRole": "user",
                "displayName": f"{user_data.first_name} {user_data.last_name}",
                "locale": "en",
                "metadata": {
                    "firstName": f"{user_data.first_name}",
                    "lastName": f"{user_data.last_name}"
                }
            }
        }
        headers = {"Content-Type": "application/json"}

        response = requests.post(url, json=payload, headers=headers)

        return response

    async def login_user(self, user_data: UserSignInModel):
        url = f"{Config.NHOST_AUTH_URL}/signin/email-password"

        payload = {
            "email": f"{user_data.email}",
            "password": f"{user_data.password}"
        }
        headers = {"Content-Type": "application/json"}

        response = requests.post(url, json=payload, headers=headers)

        return response



