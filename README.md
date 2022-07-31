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
### Required
| Name  | Description |
| --- | --- |
| BOT_TOKEN | The Discord's bot token |
| CHANNEL_ID | ID of the Discord channel where the bot will post torrent updates |
| IMAGE_CHANNEL_ID | ID of the Discord channel where the bot will post torrent updates |

### Optionnal
| Name | Default | Description |
| --- | --- | --- |
| DELETE_AFTER | 3600 | Time in seconds before deleting the bot's messages |
| CHECK_INTERVAL | 5 | Time interval in seconds for which the bot checks the status of torrents |
| COMPLETE_COLOR | ![#32a852](https://via.placeholder.com/15/32a852/32a852.png) `#32a852` | Color used when the torrent download is complete |
| DOWNLOADING_COLOR | ![#fca503](https://via.placeholder.com/15/fca503/fca503.png) `#fca503` | Color used when the torrent is downloading |
| ERROR_COLOR | ![#eb3c15](https://via.placeholder.com/15/eb3c15/eb3c15.png) `#eb3c15` | Color used when the torrent download is stopped |
| TRANSMISSION_HOST | localhost | Transmission's host |
| TRANSMISSION_PORT | 9091 | Transmission's port |
| TRANSMISSION_USERNAME |  | Transmission's username |
| TRANSMISSION_PASSWORD |  | Transmission's password |
| TRANSMISSION_PATH | /transmission/ | Transmission's path |
| TRANSMISSION_PROTOCOL | http | Transmission's protocol |
