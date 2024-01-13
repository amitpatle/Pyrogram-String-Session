from pyrogram import Client

api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"

# Create a Pyrogram client 
with Client("my_account", api_id, api_hash) as client:
    # Get the string session
    string_session = client.export_session_string()
    print("Pyrogram String Session:", string_session)
