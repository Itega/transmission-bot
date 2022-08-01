import math
from datetime import datetime, timezone
from io import BytesIO

import discord
from PIL import Image, ImageFont, ImageDraw
from transmission_rpc import Torrent

from config import (
    DELETE_AFTER,
    CHANNEL_ID,
    IMAGE_CHANNEL_ID,
    COMPLETE_COLOR,
    DOWNLOADING_COLOR,
    ERROR_COLOR,
)

STATUS_COLOR = {
    "complete": COMPLETE_COLOR,
    "seeding": COMPLETE_COLOR,
    "seed pending": COMPLETE_COLOR,
    "download pending": DOWNLOADING_COLOR,
    "downloading": DOWNLOADING_COLOR,
    "stopped": ERROR_COLOR,
    "check pending": ERROR_COLOR,
    "checking": ERROR_COLOR,
}


def create_progress_bar(progress, color):
    x = 0
    y = 0
    w = 300
    h = 30
    bg = (220, 220, 220)

    msg = f"{math.floor(progress)} %"

    out = Image.new("RGBA", (w + h + 1, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(out)

    draw.ellipse((x + w, y, x + h + w, y + h), fill=bg)
    draw.ellipse((x, y, x + h, y + h), fill=bg)
    draw.rectangle((x + (h / 2), y, x + w + (h / 2), y + h), fill=bg)

    wp = w
    wp *= progress / 100
    draw.ellipse((x + wp, y, x + h + wp, y + h), fill=color)
    draw.ellipse((x, y, x + h, y + h), fill=color)
    draw.rectangle((x + (h / 2), y, x + wp + (h / 2), y + h), fill=color)

    font = ImageFont.truetype("./SourceSansPro-Bold.ttf", 22)
    draw.text((170, 15), msg, anchor="mm", font=font, fill=(50, 50, 50))

    f = BytesIO()
    out.save(f, "png")
    f.seek(0)
    return f


async def send_progress(
    client: discord.Client, torrent: Torrent, msg: discord.Message = None
):
    img_name = "progress.png"
    status = torrent.status
    if torrent.status != "downloading" and torrent.progress == 100:
        status = "complete"
    color: discord.Colour = STATUS_COLOR[status]
    channel: discord.TextChannel = client.get_channel(CHANNEL_ID)

    f = create_progress_bar(torrent.progress, color=color.to_rgb())
    img = discord.File(f, filename=img_name)

    embed = discord.Embed(title=torrent.name, colour=color)
    embed.add_field(
        name="Status",
        value=status,
        inline=False,
    )
    embed.add_field(
        name="Size", value=f"{torrent.total_size // 1000000}MB", inline=False
    )

    if torrent.status == "downloading":
        embed.add_field(
            name="Download started at",
            value=torrent.date_started.strftime("%Y-%m-%d %H:%M:%S"),
            inline=False,
        )
        try:
            embed.add_field(name="ETA", value=str(torrent.eta), inline=False)
        except ValueError:
            pass
    elif torrent.progress == 100:
        embed.add_field(
            name="Download duration",
            value=str(datetime.now(timezone.utc) - torrent.date_started).split(".")[0],
            inline=False,
        )
    image_channel = client.get_channel(IMAGE_CHANNEL_ID)
    attachment = (
        await image_channel.send(file=img, delete_after=DELETE_AFTER)
    ).attachments[0]

    embed.set_image(url=attachment.url)

    if msg is None:
        return await channel.send(embed=embed)
    return await msg.edit(
        embed=embed,
        delete_after=DELETE_AFTER
        if status == "complete"
        else None,
    )
