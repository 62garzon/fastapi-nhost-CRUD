from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    NHOST_GRAPHQL_URL: str
    NHOST_HASURA_URL: str
    X_HASURA_ADMIN_SECRET: str
    NHOST_AUTH_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = Settings()
