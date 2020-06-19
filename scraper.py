from bs4 import BeautifulSoup
import requests


class ImageScraper:
    def __init__(self):
        pass

    def get_image(self, keyword):
        page = requests.get(f'https://pixabay.com/images/search/{keyword}/')

        soup = BeautifulSoup(page.content, 'html.parser')


    def save_image(self, image):

        img_data = requests.get(image).content

        with open('image.jpg', mode='wb+') as f:
            f.write(img_data)
