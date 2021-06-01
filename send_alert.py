#!/usr/bin/env python

from datetime import datetime
import getpass
import requests
from take_picture import take_picture

# Private data
from keys import BOT_CHATID, BOT_TOKEN
from config import IMG_PATH, PC_NAME


def telegram_bot_msg(to_send_msg):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': {BOT_CHATID}, 'text': {to_send_msg}}
    requests.post(url, data).json()


def telegram_bot_image(image_path):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto'
    image = {'photo': open(image_path, 'rb')}
    data = {'chat_id': {BOT_CHATID}}
    requests.post(url, files=image, data=data)


def main():
    # Get the time
    crnt_time = datetime.now()
    msg_formatted_time = crnt_time.strftime('%d/%m/%y - %H:%M')
    # Get the user
    user = getpass.getuser()
    # Take and save the picture
    capture = take_picture(crnt_time, IMG_PATH)
    # Send the messages
    telegram_bot_msg(f'New Access to {PC_NAME}: {user}, {msg_formatted_time}')
    telegram_bot_image(capture)


if __name__ == '__main__':
    main()
