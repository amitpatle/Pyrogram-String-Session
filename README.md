

---

# Pyrogram String Session Generator

This Python script demonstrates how to use the Pyrogram library to generate a string session for your Telegram account. The string session is required for authentication when working with the Telegram API using Pyrogram.

## Prerequisites

- Python 3.x
- Pyrogram library (`pip install pyrogram`)
- Telegram API credentials (API ID and API Hash)

## Getting Started

1. Clone this repository or download the script.

```bash
git clone https://github.com/amitpatle/pyrogram-string-session.git
cd pyrogram-string-session
```

2. Install the required dependencies.

```bash
pip install pyrogram

```

3. Replace the placeholder values in the script with your own Telegram API credentials.

```python
api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"
```
  ❗ Replace "YOUR_API_ID" and "YOUR_API_HASH" with your own values. To obtain API credentials,<br>
  you need to create an application on the Telegram website: https://my.telegram.org/auth

4. Run the script.

```bash
python get_string_session.py
```

5. Follow the on-screen instructions to enter your phone number and login code.

6. After successful authentication, the script will print your Pyrogram string session.

## Important Note

Keep your API credentials and string session secure. It is recommended to use environment variables to store sensitive information.
