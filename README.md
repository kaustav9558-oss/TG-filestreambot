# Telegram File Stream Bot
This bot will give you stream links for Telegram files without waiting for them to download.

---

[Demo Bot »](https://telegram.dog/DirectLinkGenerator_Bot)  
[Report a Bug](https://github.com/DeekshithSH/FileStreamBot/issues) |
[Request Feature](https://github.com/DeekshithSH/FileStreamBot/issues)

---

### Original Repository
[TG-FileStreamBot](https://github.com/SpringsFern/TG-FileStreamBot) is a modified version of [TG-FileStreamBot](https://github.com/EverythingSuckz/TG-FileStreamBot) by [EverythingSuckz](https://github.com/EverythingSuckz)

The main logic was taken from [Tulir Asokan](https://github.com/tulir)'s [tg filestream](https://github.com/tulir/TGFileStream) project.

## How to make your own

<details>
<summary>[Show Me More 🔽]</summary>

### 🚀 Deploy on Heroku

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Then go to the [variables tab](#environment-variables) for info on setting up environment variables.



### 🖥 Host on VPS / Locally

```sh
git clone https://github.com/SpringsFern/TG-FileStreamBot
cd TG-FileStreamBot
python3 -m venv ./venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 -m WebStreamer
```

To stop the bot, press <kbd>CTRL</kbd>+<kbd>C</kbd>

To keep it running 24/7 on VPS:

```sh
sudo apt install tmux -y
tmux
python3 -m WebStreamer
```

You can now close the terminal and the bot will keep running.

</details>

## Environment Variables

<details>
<summary>[Show Me More 🔽]</summary>

If you're on Heroku, add these as Config Vars.  
If hosting locally, create a `.env` file in the root directory and add them there.

---

### 🔒 Mandatory

<details>
<summary>[Show Me More 🔽]</summary>

- `API_ID` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.
- `API_HASH` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.
- `BOT_TOKEN` : Get the bot token from [@BotFather](https://telegram.dog/BotFather)
- `BIN_CHANNEL` : Create a new channel (private/public), post something in your channel. Forward that post to [@missrose_bot](https://telegram.dog/MissRose_bot) and **reply** `/id`. Now copy paste the forwarded channel ID in this field. 

</details>

---

### 🧩 Optional

<details>
<summary>[Show Me More 🔽]</summary>

- `ALLOWED_USERS`:  A list of user IDs separated by comma (,). If this is set, only the users in this list will be able to use the bot.
> **Note**
> Leave this field empty and anyone will be able to use your bot instance.
- `CACHE_SIZE` (default: 128) — Maximum number of file info entries cached per client. Each client (including those using MULTI_TOKEN) gets its own separate cache of this size
- `CHUNK_SIZE`: Size of the chunk to request from Telegram server when streaming a file [See more](https://core.telegram.org/api/files#downloading-files)
- `CONNECTION_LIMIT`:  (default 20) - The maximum number of connections to a single Telegram datacenter.
- `FQDN` :  A Fully Qualified Domain Name if present. Defaults to `WEB_SERVER_BIND_ADDRESS`
- `HAS_SSL` : (can be either `True` or `False`) If you want the generated links in https format.
- `HASH_LENGTH`: This is the custom hash length for generated URLs. The hash length must be greater than 5 and less than 64.
- `KEEP_ALIVE` : If you want to make the server ping itself every
- `NO_PORT` : (can be either `True` or `False`) If you don't want your port to be displayed. You should point your `PORT` to `80` (http) or `443` (https) for the links to work. Ignore this if you're on Heroku.
- `NO_UPDATE` if set to `true` bot won't respond to any messages
- `PING_INTERVAL` : The time in seconds you want the servers to be pinged each time to avoid sleeping (Only for Heroku). Defaults to `600` or 10 minutes.
- `PORT` : The port that you want your webapp to be listened to. Defaults to `8080`
- `REQUEST_LIMIT`: (default 5) - The maximum number of requests a single IP can have active at a time
- `SLEEP_THRESHOLD` : Set a sleep threshold for flood wait exceptions happening globally in this telegram bot instance, below which any request that raises a flood wait will be automatically invoked again after sleeping for the required amount of time. Flood wait exceptions requiring higher waiting times will be raised. Defaults to 60 seconds.
- `TRUST_HEADERS`: (defaults to true) - Whether or not to trust X-Forwarded-For headers when logging requests.
- `WEB_SERVER_BIND_ADDRESS` : Your server bind address. Defauls to `0.0.0.0`

</details>

---

### 🤖 Multi-Client Tokens

<details>
<summary>[Show Me More 🔽]</summary>

Use for adding multiple bots:
- `MULTI_TOKEN1`
- `MULTI_TOKEN2`
- `MULTI_TOKEN3`, etc.

</details>

</details>

## How to use the bot

<details>
<summary>[Show Me More 🔽]</summary>

:warning: Make sure all bots are added to the `BIN_CHANNEL` as **admins**.

- `/start` — Check if the bot is alive  
- Forward any media to get an instant stream link.

</details>

## FAQ

<details>
<summary>[Show Me More 🔽]</summary>

**Q: Do the stream links expire?**  
A: They are valid as long as your bot is alive and the log channel isn’t deleted.

</details>

## Contributing

Feel free to open issues or PRs with improvements or suggestions.

## Contact

Join the [Telegram Group](https://xn--r1a.click/AWeirdString) or [Channel](https://xn--r1a.click/SpringsFern) for updates.

## Credits

- [Me](https://github.com/DeekshithSH)
- [EverythingSuckz](https://github.com/EverythingSuckz) for his [TG-FileStreamBot](https://github.com/EverythingSuckz/TG-FileStreamBot)
- [Tulir Asokan](https://github.com/tulir) for his [tg filestream](bit.ly/tg-stream)
- [eyaadh](https://github.com/eyaadh) for his awesome [Megatron Bot](https://github.com/eyaadh/megadlbot_oss).
- [BlackStone](https://github.com/eyMarv) for adding multi-client support.
- [Lonami](https://github.com/Lonami) for his [Telethon Library](https://github.com/LonamiWebs/Telethon)
