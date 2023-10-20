import requests
from bs4 import BeautifulSoup
import zipfile
import os
import shutil

def get_latest_chromedriver_version():
    url = 'https://googlechromelabs.github.io/chrome-for-testing/'
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        version_element = soup.select_one('#stable > p:nth-child(2) > code:nth-child(1)')
        if version_element:
            return version_element.text.strip()
    except requests.RequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

def download_file(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, 'wb') as file:
            file.write(response.content)
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return False
    return True

def unzip_file(zip_filepath, extract_to):
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def move_file(src, dest):
    shutil.move(src, dest)

def main():
    latest_version = get_latest_chromedriver_version()
    if latest_version:
        print(f"Latest ChromeDriver version: {latest_version}")
        zip_url = f"https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{latest_version}/win64/chromedriver-win64.zip"
        zip_file_path = 'chromedriver.zip'
        extracted_folder_path = 'extracted'
        target_folder_path = 'C:/Users/read/Desktop/python_script/web_driver/webdriver'
        target_file_path = os.path.join(target_folder_path, 'chromedriver.exe')
        webdriver_exe_path = os.path.join(extracted_folder_path, 'chromedriver-win64', 'chromedriver.exe')

        if download_file(zip_url, zip_file_path):
            unzip_file(zip_file_path, extracted_folder_path)
            move_file(webdriver_exe_path, target_file_path)
        else:
            print("Failed to download the zip file.")

if __name__ == "__main__":
    main()
