import requests
from bs4 import BeautifulSoup
import os


url = "https://www.jeffpippen.com/fungi/mushrooms.htm"
response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

images = soup.find_all('img')
for img in images:
    if 'src' in img.attrs and 'alt' in img.attrs:
        image_url = img['src']
        image_name = img['alt']

        # Sanitize the image name to remove invalid characters
        image_name = image_name.replace(" ", "_").replace("<", "").replace(">", "").replace("/", "_").replace("I", "") + ".jpg"

        full_image_url = url.rsplit('/', 1)[0] + '/' + image_url

        # Ensure the directory exists
        save_path = "dataset/test/"
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # Download and save the image, skip if an error occurs
        try:
            img_data = requests.get(full_image_url).content
            with open(os.path.join(save_path, image_name), 'wb') as handler:
                handler.write(img_data)
        except Exception as e:
            print(f"Skipped {image_name} due to an error: {e}")
