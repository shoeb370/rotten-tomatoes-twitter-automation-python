# Rotten Tomatoes Twitter Automation with Python

This project automates the posting of Rotten Tomatoes movie data on Twitter using Python scripts. It fetches the latest upcoming movies from the Rotten Tomatoes website and posts tweets with movie details, ratings, and poster images.

## Features

- Fetches the latest movie data from Rotten Tomatoes using web scraping
- Posts tweets with movie details, ratings, and poster images
- Checks for previously posted movies to avoid duplicate tweets
- Saves data of posted movies to avoid reposting in the future

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/rotten-tomatoes-twitter-automation-python.git
   ```

2. Install the required packages:

   ```bash
   pip install requests pandas beautifulsoup4
   ```

3. Set up Twitter API keys in `post_tweet_v2.py`

4. Run the script:

   ```bash
   python main.py
   ```

## Usage

- Customize the tweet content or frequency of posting in `main.py`
- Ensure `already_posted_movie.csv` is present for tracking posted movies

## Twitter API Setup

1. Create a Twitter developer account at [Twitter Developer](https://developer.twitter.com/en).
2. Create a new app and note down the API key, API secret key, access token, and access token secret.
3. Create a `config_tweet.ini` file in the project directory with the following format:

   ```ini
   [Twitter]
   api_key = YOUR_API_KEY
   api_secret = YOUR_API_SECRET
   acess_token = YOUR_ACCESS_TOKEN
   acess_secret_token = YOUR_ACCESS_SECRET_TOKEN
   bearer_token = YOUR_BEARER_TOKEN

4. Update the auth_cred() function in post_tweet_v2.py to read these credentials from config_tweet.ini

## Authentication and Tweet Posting

The `auth_cred()` function reads the Twitter API credentials from `config_tweet.ini` and authenticates the API client using `tweepy.Client` and `tweepy.OAuth1UserHandler`.

The `post_tweet(tweet, file_name)` function in `post_tweet_v2.py` posts a tweet with the provided tweet content and an optional image (`file_name`).

## Usage

1. Ensure `config_tweet.ini` is correctly configured with your Twitter API credentials.
2. Run the `main.py` script to fetch the latest movies from Rotten Tomatoes and post tweets about them on Twitter.


## Contributors

- [Shoeb Ahmed](https://github.com/shoeb370)
