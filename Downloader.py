import requests
import os
import logging
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# List to store URLs of MP4 files
file_urls = []

# URL of the page containing links to MP4 files
gUrl = "https://archive.org/download/RecurringDinosaurInfestationFilms"
# Base URL for the MP4 files
base_url = "https://dn790006.ca.archive.org/0/items/RecurringDinosaurInfestationFilms/"

# Send HTTP GET request to the URL and parse the response using BeautifulSoup
response = requests.get(gUrl)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <a> tags (hyperlinks)
for video_tag in soup.find_all('a'):
    video_url = video_tag.get('href')  # Extract the 'href' attribute
    if video_url and video_url.endswith('.mp4'):
        print(f"MP4 URL: {video_url}")
        full_url = base_url + video_url
        file_urls.append(full_url)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)

# Directory where downloaded files will be saved
save_dir = 'c:\\Users\\Lardex\\Videos\\Captures'

# Create the save directory if it does not exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Function to download a single file given its URL
def download_file(url):
    local_filename = url.split('/')[-1]  # Extract the filename from the URL
    local_filepath = os.path.join(save_dir, local_filename)  # Create local filepath
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()  # Raise an error for non-OK status codes
            with open(local_filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)  # Write content in chunks to local file
        logger.info(f"Downloaded: {local_filename}")  # Log successful download
        return local_filepath  # Return local filepath of the downloaded file
    except requests.RequestException as e:
        logger.error(f"Error downloading {local_filename}: {e}")  # Log download error
        return None  # Return None if download fails

# Number of worker threads for parallel downloads
max_workers = 10

# Use ThreadPoolExecutor to download files concurrently
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    executor.map(download_file, file_urls)  # Map download_file function to file_urls

print('All files have been downloaded.')  # Print completion message
