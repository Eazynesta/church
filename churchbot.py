import tweepy
import requests
import random
import time
import keys  # Make sure you have a keys.py file with your credentials

# Initialize the Twitter client
client = tweepy.Client(keys.BEARER_TOKEN, keys.API_KEY, keys.API_SECRET_KEY, keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)

# List of Bible books and their chapters (partial example, you can expand this list)
bible_books = {
    "Deuteronomy": 34,
    "Psalms": 150,
    "Proverbs": 31,
    "Ecclesiastes": 12,
    "Isaiah": 66,
    "Malachi": 4,
    "Matthew": 28,
    "Mark": 16,
    "Luke": 24,
    "John": 21,
    "Acts": 28,
    "Hebrews": 13,
    "Revelation": 22
}

# Function to get a random scripture
def get_random_scripture():
    book = random.choice(list(bible_books.keys()))
    chapter = random.randint(1, bible_books[book])
    verse = random.randint(1, 20)  # Assuming a maximum of 20 verses per chapter for simplicity

    url = f"https://bible-api.com/{book}+{chapter}:{verse}"
    response = requests.get(url)
    data = response.json()
    if 'text' in data:
        scripture = f"{data['text']} - {data['reference']}"
        return scripture
    return "Could not fetch scripture. Please try again."

# Function to tweet a random scripture
def tweet_scripture():
    scripture = get_random_scripture()
    try:
        client.create_tweet(text=scripture)
        print(f"Tweeted: {scripture}")
    except Exception as e:
        print(f"Failed to tweet: {e}")

# Schedule to tweet 45 times a day (every 32 minutes)
while True:
    tweet_scripture()
    time.sleep(32 * 60)  # Sleep for 32 minutes
