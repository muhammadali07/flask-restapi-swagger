from typing import Dict, Any, Optional
from pydantic import (
    BaseSettings,
    validator,
)
import os

class Settings(BaseSettings):

    MYSQL_DB_SERVER: str = "db"
    MYSQL_DB_API_USER: str = "flaskusr"
    MYSQL_DB_API_PASSWORD: str = "flaskpass"
    MYSQL_DB_API: str = "flaskdb"
    
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
        port = "3306"
        conmy = "{}+{}://{}:{}@{}/{}?charset=utf8mb4".format(scheme,driver, user,password,host, database)
        print(conmy)
        return conmy
    print(f"connect:{SQLALCHEMY_DATABASE_URI}")

settings = Settings()