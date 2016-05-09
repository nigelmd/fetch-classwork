import os
import urllib
import requests
import re
from bs4 import BeautifulSoup 

# Create the default save directory if it doesn't exist
DEFAULT_SAVE_DIR = 'classwork'

def make_dir():
    if not os.path.exists(DEFAULT_SAVE_DIR):
        os.makedirs(DEFAULT_SAVE_DIR)

# Check if the url is valid for our use
def is_valid_class_url(href):
    return href and re.compile("/csc438/2016/.*").search(href)

def get_files(href):
    data = requests.get(href)
    html = BeautifulSoup(data.text, 'html.parser') 
    
    links = html.find_all(href=is_valid_class_url)

    for link in links:
        parts = link['href'].split('2016/')
        parts[0] = parts[0].lstrip('/')

        # Ignore the temp files
        if '%7E' in parts[1]:
            continue

        # If it has preview, means it's a file
        if 'preview' in parts[0]:
            download_link = href.replace('index', 'get')
            filename = parts[1].split("?")[0].split("/")[-1]

            # Including the 1 for the '/' in the url
            file_name_length = 1 + len(filename)
            save_path = DEFAULT_SAVE_DIR + '/' + parts[1][:-file_name_length]

            print download_link + filename

            if os.path.exists(save_path):
                pass
            else:
                os.makedirs(save_path)    

            # Retrieve the file
            urllib.urlretrieve(download_link + filename, save_path + '/' + filename)
        else:
            folder_name = parts[1].split("?")[0].split("/")[-1]
            # Recursively get the subdirectory
            get_files(href + folder_name + '/')

def main():
    make_dir()
    get_files('http://mdp.cti.depaul.edu/classwork/default/index/csc438/2016/')

if __name__ == '__main__':
    main()
