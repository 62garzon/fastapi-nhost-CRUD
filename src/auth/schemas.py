from pydantic import BaseModel, Field


class UserCreateModel(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: str = Field(max_length=40)
    password: str = Field(min_length=9)

    model_config = {
        "json_schema_extra": {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@gmail.com",
                "password": "123456789",
            }
        }
    }


class UserSignInModel(BaseModel):
    email: str = Field(max_length=40)
    password: str = Field(min_length=8)

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "john.doe@gmail.com",
                "password": "123456789",
            }
        }
    }