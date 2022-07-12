from typing import Dict, Any, Optional
from pydantic import (
    BaseSettings,
    validator,
)
import os

class Settings(BaseSettings):

    SQLALCHEMY_WITH_DRIVER_URI: Optional[str] = None
    # 'mysql+asyncmy://someuser:asswd1234@localhost/app_db'
    # 'mysql+asyncmy://scott:tiger@localhost/db'

    @validator("SQLALCHEMY_WITH_DRIVER_URI", pre=True)
    def mysql_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(v, str):
            return v

        # dialect[+driver]://user:password@host/dbname[?key=value..]
        scheme = "mysql"
        driver = "asyncmy"
        user = "user"
        password = "password"
        host = "localhost"
        database = "db"
        return "{}+{}://{}:{}@{}/{}".format(scheme, driver, user, password, host, database)


settings = Settings()