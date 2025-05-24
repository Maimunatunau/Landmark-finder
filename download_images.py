# download_images.py
# Bulk-download “lazy” landmark images using Google Image Crawler (icrawler).
# Usage:
#   1. pip install icrawler
#   2. python download_images.py

import os
from icrawler.builtin import GoogleImageCrawler

# Define your download tasks
tasks = [
    {
        'keyword': 'Eiffel Tower blurry low light',
        'dir': 'data/raw/eiffel_tower',
        'max_num': 200,
    },
    {
        'keyword': 'Statue of Liberty blurry low light',
        'dir': 'data/raw/statue_of_liberty',
        'max_num': 200,
    },
]

for task in tasks:
    save_dir = task['dir']
    os.makedirs(save_dir, exist_ok=True)
    crawler = GoogleImageCrawler(storage={'root_dir': save_dir})
    print(f"Starting crawl for '{task['keyword']}' into {save_dir} ({task['max_num']} images)...")
    crawler.crawl(
        keyword=task['keyword'],
        max_num=task['max_num'],
        min_size=(200, 200),  # filter out very small images
        max_size=None,
    )
    print(f"Finished crawling {save_dir}\n")

print("All downloads complete. Check data/raw/ for your images.")
