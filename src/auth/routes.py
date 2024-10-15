from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .schemas import UserCreateModel, UserSignInModel
from .service import UserService

from fastapi.exceptions import HTTPException

auth_router = APIRouter()
user_service = UserService()


@auth_router.post("/signup/email-password")
async def create_user_account(user_data: UserCreateModel):
    response = await user_service.create_user(user_data)
    if response.status_code == 200:
        return await prepare_ok_response(response, "Register successful", user_data.email)

    else:
        print(f"Error: {response.json()['message']}")
        raise HTTPException(
            detail=f"{response.json()['message']}", status_code=response.status_code
        )


@auth_router.post("/signin/email-password")
async def login_user_account(user_data: UserSignInModel):
    response = await user_service.login_user(user_data)

    if response.status_code == 200:
        return await prepare_ok_response(response, "Login successful", user_data.email)

    else:
        print(f"Error: {response.json()['message']}")
        raise HTTPException(
            detail=f"{response.json()['message']}", status_code=response.status_code
        )
        # raise InvalidCredentials()


async def prepare_ok_response(response, message, email):
    session_data = response.json()
    access_token = session_data['session']['accessToken']
    refresh_token = session_data['session']['refreshToken']
    expires_in = session_data['session']['accessTokenExpiresIn']

    return JSONResponse(
        content={
            "message": f"{message}",
            "access_token": access_token,
            "refresh_token": refresh_token,
            "expires_in": expires_in,
            "user": {"email": email},
        }
    )
