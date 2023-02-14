import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("6050390903:AAE0G1nyiOOd0eTtgVfG00qOKQdw4GBKNt8", "")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("28293790", ""))

    # Get from my.telegram.org
    API_HASH = os.environ.get("9bc15ceaed13bf8ffcf4e0e3ff8ee858", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
