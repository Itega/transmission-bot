import os

from discord import Colour, Color
from dotenv import load_dotenv

load_dotenv()


def parse_hex_number(argument: str) -> Colour:
    arg = argument[1:]
    arg = "".join(i * 2 for i in arg) if len(arg) == 3 else arg
    try:
        value = int(arg, base=16)
        if not (0 <= value <= 0xFFFFFF):
            raise ValueError("hex number out of range for 24-bit colour")
    except ValueError:
        raise ValueError("invalid hex digit given") from None
    else:
        return Color(value=value)


BOT_TOKEN = os.environ.get("BOT_TOKEN")
DELETE_AFTER = int(os.environ.get("DELETE_AFTER", 60 * 60))
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
IMAGE_CHANNEL_ID = int(os.environ.get("IMAGE_CHANNEL_ID"))

CHECK_INTERVAL = int(os.environ.get("CHECK_INTERVAL", 5))

COMPLETE_COLOR = parse_hex_number(os.environ.get("COMPLETE_COLOR", "#32a852"))
DOWNLOADING_COLOR = parse_hex_number(os.environ.get("DOWNLOADING_COLOR", "#fca503"))
ERROR_COLOR = parse_hex_number(os.environ.get("ERROR_COLOR", "#eb3c15"))

TRANSMISSION_PATH = os.environ.get("TRANSMISSION_PATH", "/transmission/")
TRANSMISSION_PROTOCOL = os.environ.get("TRANSMISSION_PROTOCOL", "http")
TRANSMISSION_HOST = os.environ.get("TRANSMISSION_HOST", "localhost")
TRANSMISSION_PORT = int(os.environ.get("TRANSMISSION_PORT", 9091))
TRANSMISSION_USERNAME = os.environ.get("TRANSMISSION_USERNAME")
TRANSMISSION_PASSWORD = os.environ.get("TRANSMISSION_PASSWORD")

TRANSMISSION_CONFIG = {
    "host": TRANSMISSION_HOST,
    "port": TRANSMISSION_PORT,
    "username": TRANSMISSION_USERNAME,
    "password": TRANSMISSION_PASSWORD,
    "path": TRANSMISSION_PATH,
    "protocol": TRANSMISSION_PROTOCOL,
}
