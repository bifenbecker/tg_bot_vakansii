import os
from typing import Union
from pydantic_settings import BaseSettings
from pydantic import Field, BaseModel
from enum import Enum
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent  # Edit if file move to another dir
PROJECT_DIR = os.path.basename(BASE_DIR)
CONFIG_DIR = os.path.join(BASE_DIR, "../../config")
ENV_DIR = os.path.join(CONFIG_DIR, "environment")


class Env(BaseModel):
    name: Enum
    path: Enum


class EnvNames(str, Enum):
    DEV: str = "DEV"
    TESTING: str = "TESTING"
    PROD: str = "PROD"


class EnvPaths(Enum):
    DEV: Path = Path(os.path.join(ENV_DIR, ".env.development"))
    TESTING: Path = Path(os.path.join(ENV_DIR, ".env.testing"))
    PROD: Path = Path(os.path.join(ENV_DIR, ".env.production"))


class Envs(Enum):
    DEV: Env = Env(name=EnvNames.DEV, path=EnvPaths.DEV)
    TESTING: Env = Env(name=EnvNames.TESTING, path=EnvPaths.TESTING)
    PROD: Env = Env(name=EnvNames.PROD, path=EnvPaths.PROD)


ENV_CONFIG = {
    EnvNames.DEV.value: EnvPaths.DEV.value,
    EnvNames.TESTING.value: EnvPaths.TESTING.value,
    EnvNames.PROD.value: EnvPaths.PROD.value,
}

ENV = os.environ.get("ENV", EnvNames.DEV.value)

is_loaded_env = load_dotenv(ENV_CONFIG[EnvNames(ENV)])
if not is_loaded_env:
    raise Exception("Environment did not load")


class GeneralSettings(BaseSettings):
    ENV: str = Field(env="ENV", default=EnvNames.DEV.value)
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent  # Edit if file move to another dir
    PROJECT_DIR: Path = Path(os.path.basename(BASE_DIR))
    CONFIG_DIR: Path = Path(os.path.join(BASE_DIR, "../../config"))
    ENV_DIR: Path = Path(os.path.join(CONFIG_DIR, "environment"))


class TelegramSettings(BaseSettings):
    TG_TOKEN: str = Field(env="TG_TOKEN")
    SKIP_PENDING: bool = Field(env="SKIP_PENDING")
    MAX_LEN_USER_HISTORY: int = Field(env="MAX_LEN_USER_HISTORY")


class DatabaseSettings(BaseSettings):
    DB_HOST: str = Field(env="DB_HOST")
    DB_PORT: int = Field(env="DB_PORT")
    DB_USER: str = Field(env="DB_USER")
    DB_PASSWORD: str = Field(env="DB_PASSWORD")
    DB_NAME: str = Field(env="DB_NAME")
    DB_DRIVER: str = Field(env="DB_DRIVER")
    LOG_ORM: bool = Field(env="LOG_ORM")


class LoggerSettings(BaseSettings):
    LOG_LEVEL: str = Field(env="LOG_LEVEL", default="INFO")
    LOGURU_DIAGNOSE: bool = Field(env="LOGURU_DIAGNOSE")
    LOGURU_BACKTRACE: bool = Field(env="LOGURU_BACKTRACE")


class BaseConfig(GeneralSettings, TelegramSettings, DatabaseSettings, LoggerSettings):
    class Config:
        env_file = ENV_CONFIG[EnvNames(ENV)]


class DevConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    pass


config = dict(
    DEV=DevConfig,
    TESTING=TestingConfig,
    PROD=ProdConfig,
)
settings: Union[DevConfig, TestingConfig, ProdConfig] = config.get(EnvNames(ENV).value)()
