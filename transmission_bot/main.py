import discord
from transmission_rpc import Client, TransmissionError

from discord.ext import tasks
from transmission_rpc.error import TransmissionConnectError, TransmissionTimeoutError

from config import (
    CHANNEL_ID,
    CHECK_INTERVAL,
    IMAGE_CHANNEL_ID,
    BOT_TOKEN,
    TRANSMISSION_CONFIG,
)
from transmission_bot.utils import send_progress

discord_client = discord.Client()
transmission_client = Client(**TRANSMISSION_CONFIG)

current_torrents = {}


@discord_client.event
async def on_ready():
    await discord_client.get_channel(CHANNEL_ID).purge()
    await discord_client.get_channel(IMAGE_CHANNEL_ID).purge()
    check_torrents.start()
    print("Bot ready")


@tasks.loop(seconds=CHECK_INTERVAL)
async def check_torrents():
    torrents = transmission_client.get_torrents()
    for torrent in torrents:
        if msg := current_torrents.get(torrent.id):
            await send_progress(discord_client, torrent, msg=msg)
            if torrent.progress == 100 and torrent.status != "downloading":
                current_torrents.pop(torrent.id)
        elif torrent.progress < 100:
            current_torrents[torrent.id] = await send_progress(discord_client, torrent)


check_torrents.add_exception_type(
    TransmissionError, TransmissionConnectError, TransmissionTimeoutError
)
discord_client.run(BOT_TOKEN)
