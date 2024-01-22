from pyrogram import Client

def main():
    api_id = input("Enter API ID: ")
    api_hash = input("Enter API HASH: ")

    # Create a Pyrogram client
    client = Client("my_account", api_id, api_hash)

    try:
        client.start()
        string_session = client.export_session_string()
        print("Pyrogram String Session:", string_session)

        if input("Are you sure you want to log out? (yes/no): ").lower() == "yes":
            client.stop()
            print("Logged out successfully")
        else:
            print("Logout canceled.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        
        client.stop()

if __name__ == "__main__":
    main()

    #delete my_session file if you want to create new session
