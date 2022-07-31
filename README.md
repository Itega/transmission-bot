# Transmission Bot
A self-hosted Discord bot that sends updates on current downloads in Transmission.

## Installation
- [Create a Discord bot](https://discordpy.readthedocs.io/en/stable/discord.html) with these permissions :
  - Send messages
  - Manage messages
  - Attach file
  - Read message history
- Edit environment variables in docker-compose.production.yml
- Start it !

## Environment variables
- BOT_TOKEN : The Discord's bot token
- CHANNEL_ID : ID of the Discord channel where the bot will post torrent updates
- IMAGE_CHANNEL_ID : ID of the discord channel used by the bot to post temporary images

- DELETE_AFTER (default: 3600) : Time in seconds before deleting the bot's messages
- CHECK_INTERVAL (default: 5) : Time interval in seconds for which the bot checks the status of torrents


- COMPLETE_COLOR (default: #32a852) : Color used when the torrent download is complete
- DOWNLOADING_COLOR (default: #fca503) : Color used when the torrent is downloading
- ERROR_COLOR (default: #eb3c15) : Color used when the torrent download is stopped


- TRANSMISSION_HOST (default: localhost) : Transmission's host
- TRANSMISSION_PORT (default: 9091) : Transmission's port
- TRANSMISSION_USERNAME : Transmission's username
- TRANSMISSION_PASSWORD : Transmission's password
- TRANSMISSION_PATH (default: /transmission/) : Transmission's path
- TRANSMISSION_PROTOCOL (default: http) = Transmission's protocol
