from telethon import TelegramClient
import csv
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables once
env_path = Path('.env')  # Set path to .env file
load_dotenv(dotenv_path=env_path)  # Explicitly load from the path

api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
phone = os.getenv('phone') 

# Debugging - Check if environment variables are being loaded
print(f"API ID: {api_id}")
print(f"API Hash: {api_hash}")
print(f"Phone: {phone}")

# Function to scrape data from a single channel
async def scrape_channel(client, channel_username, writer, media_dir):
    entity = await client.get_entity(channel_username)
    channel_title = entity.title  # Extract the channel's title
    
    async for message in client.iter_messages(entity):  # Remove limit to get all messages
        media_path = None
        
        # Extract media if available (photos, videos, etc.)
        if message.media and hasattr(message.media, 'photo'):
            filename = f"{channel_username}_{message.id}.jpg"
            media_path = os.path.join(media_dir, filename)
            await client.download_media(message.media, media_path)

        # Extract additional information
        sender = message.sender_id if message.sender_id else "Unknown"  # Sender ID (could add sender name with another API call)
        views = message.views if message.views else 0  # Views count (if available)
        forwards = message.forwards if message.forwards else 0  # Forwards count
        reply_to_msg_id = message.reply_to_msg_id if message.reply_to_msg_id else "None"  # Reply to message ID (if it's a reply)
        
        # Reactions can be extracted (for recent versions of Telethon)
        reactions = message.reactions.results if message.reactions else "None"
        reply_count = message.replies.replies if message.replies else 0
        
        # Write the channel title along with all extracted information
        writer.writerow([
            channel_title, channel_username, message.id, message.message,
            message.date, media_path, sender, views, forwards, reply_to_msg_id, reactions, reply_count
        ])

# Initialize the client once
client = TelegramClient('scraping_session', api_id, api_hash)

async def main():
    await client.start()
    
    # Create a directory for media files
    media_dir = 'photos'
    os.makedirs(media_dir, exist_ok=True)

    # Open the CSV file and prepare the writer
    with open('modern_Data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            'Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path',
            'Sender ID', 'Views', 'Forwards', 'Reply To Message ID', 'Reactions', 'Reply Count'
        ])  # Add new fields to the header

        # List of channels to scrape
        channels = [
            '@modernshoppingcenter',  # Existing channel
                 # You can add more channels here
        ]
        
        # Iterate over channels and scrape data into the single CSV file
        for channel in channels:
            await scrape_channel(client, channel, writer, media_dir)
            print(f"Scraped data from {channel}")

with client:
    client.loop.run_until_complete(main())
