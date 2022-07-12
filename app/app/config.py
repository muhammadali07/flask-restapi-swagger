from typing import Dict, Any, Optional
from pydantic import (
    BaseSettings,
    validator,
)
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    MYSQL_DB_SERVER: str = os.getenv('MYSQL_DB_SERVER')
    MYSQL_DB_API_USER: str = os.getenv('MYSQL_DB_API_USER')
    MYSQL_DB_API_PASSWORD: str = os.getenv('MYSQL_DB_API_PASSWORD')
    MYSQL_DB_API: str = os.getenv('MYSQL_DB_API')

    SQLALCHEMY_DATABASE_URI: Optional[str] = None
    
    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def mysql_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(v, str):
            return v

        # dialect[+driver]://user:password@host/dbname[?key=value..]
        scheme = "mysql"
        driver = "asyncmy"
        user = values.get("MYSQL_DB_API_USER")
        password = values.get("MYSQL_DB_API_PASSWORD")
        host = values.get("MYSQL_DB_SERVER")
        database = values.get("MYSQL_DB_API")
        return "{}+{}://{}:{}@{}/{}".format(scheme, driver, user, password, host, database)
        # conn = f'{scheme}+{driver}://{user}:{password}@{host}/{database}'
        # print(conn)
        # return conn


settings = Settings()