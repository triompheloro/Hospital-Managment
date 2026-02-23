from pydantic_settings import BaseSettings, SettingsConfigDict

_base_setting = SettingsConfigDict(
    env_file="./.env",
    env_ignore_empty=True,
    extra="ignore"
) 

class DatabaseSetting(BaseSettings):
    POSTGRESQL_HOST: str
    POSTGRESQL_PORT: int
    POSTGRESQL_USER: str
    POSTGRESQL_PASSWORD: str
    POSTGRESQL_DB: str
    
    model_config = _base_setting
    
    @property
    def POSTGRESQL_URL (self):
        return f"postgresql+asyncpg://{self.POSTGRESQL_USER}:{self.POSTGRESQL_PASSWORD}@{self.POSTGRESQL_HOST}:{self.POSTGRESQL_PORT}/{self.POSTGRESQL_DB}"
    

db_settings = DatabaseSetting()