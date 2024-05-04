import requests
import os
from bs4 import BeautifulSoup

gUrl = "https://archive.org/download/RecurringDinosaurInfestationFilms"

response = requests.get(gUrl)

soup = BeautifulSoup(response.content, 'html.parser')

video_tags = soup.find_all('a')

for video_tag in video_tags:
    source_tags = video_tag.find_all('a')
    for source_tag in source_tags:
        video_url = source_tag.get('a')
        if video_url.endswith('.mp4'):
            print(f"MP4 URL: {video_url}")

# file_urls = []

# save_dir = 'c:\Users\Lardex\Videos\Captures'

# if not os.path.exists(save_dir):
#     os.makedirs(save_dir)

# def download_file(url):
#     local_filename = url.split('/')[-1]
#     local_filepath = os.path.join(save_dir, local_filename)
#     with requests.get(url, stream = True) as r:
#         r.raise_for_status()
#         with open(local_filepath, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192):
#                 f.write(chunk)
            
#     return local_filepath
    