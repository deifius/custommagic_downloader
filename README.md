# CustomMagic Card Downloader

This script is designed to download images from the r/custommagic subreddit based on specific search terms and sorting criteria. It uses the Reddit API to fetch posts that match the search terms and downloads any images linked in these posts to a local directory.

## Getting Started

### Prerequisites

You will need Python 3.6 or later and pip to run this script. Additionally, you must have a Reddit account and register an application to obtain the necessary API credentials (`client_id`, `client_secret`) and create a `user_agent`.

### Installation

1. Clone this repository or download the ZIP file and extract it to a local directory.
2. Navigate to the script's directory and install the required Python libraries:
   ```bash
   pip install praw requests
