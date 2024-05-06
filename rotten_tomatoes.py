
# Importing packages
import requests
import pandas as pd
from bs4 import BeautifulSoup
import json
import os
import re
import datetime
from post_tweet_v2 import post_tweet

def getlatestmovie():
    # Getting the latest upcoming movies
    url = "https://www.rottentomatoes.com/browse/movies_in_theaters/sort:newest"
    headers = {
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'accept-language': 'en-US,en;q=0.9',
      'cache-control': 'max-age=0',
      'if-none-match': 'W/"36b54-bbGBb7fQggc47+SIcSRszWV1AOM"',
      'priority': 'u=0, i',
      'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    
    # Get response from URLs
    response = requests.request("GET", url, headers=headers)
    html_data = response.text
    # Get the current date
    current_date = datetime.datetime.now()
    # Get the current month
    current_month = current_date.strftime("%B%Y")

    # Converting HTML Data into soup version
    soup = BeautifulSoup(html_data, 'html.parser')
    # Extracting JSON based data
    raw_json = soup.find('script',{'type':'application/ld+json'}).text.strip()
    # Converting string JSON data into JSON format
    json_data = json.loads(raw_json)
    # Converting JSON data into pandas DataFrame
    df = pd.DataFrame(json_data['itemListElement']['itemListElement'])
    # Reading previously posted movies
    prev_movies_df = pd.read_csv('already_posted_movie.csv')
    # Converting the previously posted movies link into list
    prev_links = prev_movies_df['Links'].tolist()
    # Iterating the extracted movies DataFrame
    for i in range(len(df)):
        try:
            # Check the URL to prev_links, that means if this movie details are already posted or not
            if df['url'].iloc[i] not in prev_links:
                # Collecting movie name
                movie_name = df['name'].iloc[i]
                # Collecting poster URL
                poster_link = df['image'].iloc[i]
                url = poster_link
                # Downloading the content of poster links
                response = requests.get(url, stream=True)
                file_name = 'twitter_download.jpg'
                # Saving the URL content i.e. file data
                with open(file_name, 'wb') as out_file:
                    for chunk in response.iter_content(chunk_size=128):
                        out_file.write(chunk)
                
                # Creating a tweet
                source = "Rotten Tomatoes"        
                tweet = f"🎬 Exciting news for movie buffs! Check out the poster for '{movie_name}' 🔥"
                if pd.isna(df['aggregateRating'].iloc[i]) != True:
                    ratings  = df['aggregateRating'].iloc[i]['ratingValue']
                    reviews_count = df['aggregateRating'].iloc[i]['reviewCount']        
                    tweet += f", rated {ratings} with {reviews_count} reviews on {source}!"
                tweet += f" Can't wait to see it! #{movie_name.replace(' ','')} #UpcomingMovies{current_month} 🍿🎥"
                print(tweet)
                # file_name = "Not Available"
                # Calling a twitter posting function
                post_tweet(tweet, file_name)
                os.remove(file_name)
                test_df = pd.DataFrame({'Links': [df['url'].iloc[i]]})
                prev_movies_df = pd.concat([prev_movies_df, test_df], ignore_index=False)
            else:
                pass
        except:
            pass
    # Storing the newly posted movies data, in future these movies will not be posted on Twitter
    prev_movies_df = prev_movies_df.head(200)
    prev_movies_df.to_csv('already_posted_movie.csv', index=False)
    return True
        
if __name__=="__main__":
    print("Rotten Tomatoes Twitter Posting Status: ",getlatestmovie())
