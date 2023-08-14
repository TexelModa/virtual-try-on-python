import requests
import shutil
from config import RAPID_API_KEY, AVATAR_URI, LOOK_URI

def virtual_try_on():
    params = {
        'clothing_image_url': LOOK_URI,
        'avatar_image_url': AVATAR_URI
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-RapidAPI-Key': RAPID_API_KEY,
        'X-RapidAPI-Host': 'texel-virtual-try-on.p.rapidapi.com'
    }

    try:
        response = requests.post(
            'https://texel-virtual-try-on.p.rapidapi.com/try-on-url',
            headers=headers,
            data=params
        )
        with open('result.jpg', 'wb') as output_file:
            output_file.write(response.content)
    except requests.exceptions.RequestException as error:
        print('Error:', error)

if __name__ == "__main__":
    virtual_try_on()
