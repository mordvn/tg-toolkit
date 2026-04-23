# TG Toolkit Bot

<div align="center">
<img src="media/icon.png" alt="Icon" width="450">
</div>
<p align="center">A Telegram bot for technical chat data: chat IDs, user IDs, and compact metadata for integrations and debugging.</p>

## Features

- **Get Chat ID**: Returns the current chat ID via `/get_chat_id`
- **Get User ID**: Returns your Telegram user ID via `/get_user_id`
- **Get My ID Alias**: Alias command `/get_my_id`
- **Chat Metadata**: Compact technical info with `/chat_info`
- **Quick Help**: Built-in command list via `/help`

## Setup

### Prerequisites

- Python 3
- `uv`
- Telegram bot token from [@BotFather](https://t.me/BotFather)

### Installation

1. Install dependencies:

```bash
uv sync
```

1. Create a `.env` file in the project root:

```plaintext
BOT_TOKEN=123456:your_bot_token_here
```

Alternatively, you can export the token directly:

```bash
export BOT_TOKEN="123456:your_bot_token_here"
```

## Usage

Start the bot:

```bash
uv run python app/main.py
```

Or run with Docker Compose:

```bash
cp .env.example .env
# set BOT_TOKEN in .env
docker compose up --build -d
```

### Available Commands

- `/start` - Bot status and short intro
- `/help` - List all technical commands
- `/get_chat_id` - Current chat ID
- `/get_user_id` - Sender user ID
- `/get_my_id` - Alias for `/get_user_id`
- `/chat_info` - Chat type + user metadata

## License

[MIT](https://choosealicense.com/licenses/mit/)
