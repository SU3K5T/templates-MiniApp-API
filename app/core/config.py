from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    S3_ENDPOINT: str
    
    S3_EMPTY_TEMPLATES_BUCKET: str
    S3_FORMAT_TEMPLATES_BUCKET: str

    S3_ACCESS_KEY: str
    S3_SECRET_KEY: str
    S3_CERT_PATH: str

    @property
    def GET_DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
