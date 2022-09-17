import os
import asyncio
from pyppeteer import launch
import telegram

bot_token = os.getenv('MARIIN_BOT_TOKEN')
chat_id = os.getenv('MARIIN_CHAT_ID')
url = 'https://mariin.ru/forms/onlineappointment'
image = 'status.png'

async def send_status_image():
    print('[INFO] Enter script')

    browser = await launch(
        # executablePath': os.getenv('CHROMIUM_EXEC_PATH')
    )
    page = await browser.newPage()
    await page.setViewport({'width': 800, 'height': 1000})
    await page.goto(url, { "waitUntil": 'load', "timeout": 0 })
    await page.screenshot({'path': image})
    await browser.close()

    bot = telegram.Bot(token=bot_token)
    try:
        await bot.send_photo(chat_id=chat_id, photo=open(image, 'rb'))
    except TypeError: # ToDo: Fix this
        pass

    print('[INFO] Exit script')

if __name__ == '__main__':
    print('[INFO] Run script')
    asyncio.get_event_loop().run_until_complete(send_status_image())

