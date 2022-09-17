import os
import asyncio
from pyppeteer import launch
import telegram

bot_token = os.getenv('MARIIN_BOT_TOKEN')
chat_id = os.getenv('MARIIN_CHAT_ID')
url = 'https://mariin.ru/forms/onlineappointment'
image = 'status.png'

print('!!!!!!!')
print(os.getenv('CHROMIUM_EXEC_PATH'))

def send_status_image():
    print('[INFO] Enter script')

    browser = launch(
        headless=True,
        executablePath=os.getenv('CHROMIUM_EXEC_PATH')
    )
    page = browser.newPage()
    page.setViewport({'width': 800, 'height': 1000})
    page.goto(url, { "waitUntil": 'load', "timeout": 0 })
    page.screenshot({'path': image})
    browser.close()

    bot = telegram.Bot(token=bot_token)
    bot.send_photo(chat_id=chat_id, photo=open(image, 'rb'))
    
    print('[INFO] Exit script')

if __name__ == '__main__':
    print('[INFO] Run script')
    # asyncio.run(send_status_image())
    send_status_image()

