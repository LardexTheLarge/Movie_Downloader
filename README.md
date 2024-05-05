# Movie Downloader

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to our MP4 File Downloader project! This script enables you to download MP4 files from a webpage by extracting links using BeautifulSoup and then downloading the files concurrently using ThreadPoolExecutor. The script also includes logging functionalities to track the download process.

## Features

- **Web Scraping with BeautifulSoup:** Extract MP4 file links from a webpage using BeautifulSoup.
- **Concurrent File Download:** Utilize ThreadPoolExecutor to download multiple files concurrently, enhancing download speed.
- **Logging:** Implement logging to record download progress and any encountered errors.

## Getting Started

### Prerequisites

- Python 3.x
- Requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)

### Installation

1. **Clone the repository to your local machine:**

   ```bash
   git clone git@github.com:LardexTheLarge/Movie_Downloader.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd Movie_Downloader
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Update Script Variables:**

   - Set the `gUrl` variable to the URL of the webpage containing MP4 file links.
   - Set the `base_url` variable to the base URL for the MP4 files.

2. **Run the Script:**

   ```bash
   python Movie_Downloader.py
   ```

   This will initiate the download process and save the MP4 files to the specified directory.

## Documentation

The code is documented within the script itself to explain its functionality. Inline comments provide detailed descriptions of each step in the MP4 file download process.

## Contributing

Contributions are not allowed for this project.

## License

This project is licensed under the MIT License.
