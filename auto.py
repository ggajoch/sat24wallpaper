import uuid
import os
import time

from download import download


def remove_all_jpg():
    # remove all jpg files in this directory
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
            print("removed: " + file)


def remove_file(path):
    os.remove(path)
    print("removed: " + path)


if __name__ == '__main__':
    print("Removing all old files")
    remove_all_jpg()

    old_name = None
    while True:
        name = str(uuid.uuid4()) + '.jpg'
        download(name)
        print("Downloaded: " + name)
        if old_name is not None:
            remove_file(old_name)
        old_name = name

        time.sleep(60)
