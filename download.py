import shutil
import requests

url = 'https://pl.sat24.com/image?type=visual5HDComplete&region=eu'


def download(path):
    r = requests.get(url, stream=True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully Downloaded: ', path)
    else:
        print('Image Couldn\'t be retreived')


if __name__ == '__main__':
    download()
