from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    log_level: str = "INFO"
    db_echo: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",

        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "src": {"handlers": ["default"], "level": settings.log_level},
    },
}
