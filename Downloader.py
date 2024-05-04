import requests
import os

file_urls = []

save_dir = 'c:\Users\Lardex\Videos\Captures'

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

def download_file(url):
    local_filename = url.split('/')[-1]
    local_filepath = os.path.join(save_dir, local_filename)
    with requests.get(url, stream = True) as r:
        r.raise_for_status()
        with open(local_filepath, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
            
    return local_filepath
    