import openai
from environs import Env


def openai_init() -> None:
    env = Env()
    env.read_env()

    openai.api_key: str = env("OPENAI_TOKEN")
