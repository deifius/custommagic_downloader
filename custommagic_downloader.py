import praw
import requests
import os
import argparse

def download_image(image_url, save_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)

def main(search_term, sort, n, subreddit="custommagic"):
    reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                         client_secret='YOUR_CLIENT_SECRET',
                         user_agent='YOUR_USER_AGENT')

    subreddit = reddit.subreddit(subreddit)
    posts = subreddit.search(search_term, sort=sort, time_filter='year', limit=n)
    
    directory = f"cards/{search_term.replace(' ', '_')}/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    for post in posts:
        if hasattr(post, 'url') and (post.url.endswith('.jpg') or post.url.endswith('.png')):
            file_name = os.path.join(directory, f"{post.id}.jpg")
            download_image(post.url, file_name)
            print(f"Downloaded {file_name}")
   os.system(f'feh -F --on-last-slide quit --zoom max {directory}*')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download images from r/custommagic.')
    parser.add_argument('--sort', type=str, default="relevance")
    parser.add_argument('-n', type=int, default=10)
    parser.add_argument('search_terms', type=str, nargs='+')
    args = parser.parse_args()

    search_term = ' '.join(args.search_terms)
    sort = args.sort.split(':')[-1]  # Expecting input like "hot:pastyear"
    n = args.n

    main(search_term, sort, n)
