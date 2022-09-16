import os
import asyncio
from pyppeteer import launch
import telegram

bot_token = os.getenv('MARIIN_BOT_TOKEN')
chat_id = '-702417506'
url = 'https://mariin.ru/forms/onlineappointment'
image = 'status.png'

async def send_status_image():
    browser = await launch({
        executablePath: os.getenv('PUPPETEER_EXEC_PATH')
    })
    page = await browser.newPage()
    await page.setViewport({'width': 800, 'height': 1000})
    await page.goto(url, { "waitUntil": 'load', "timeout": 0 })
    await page.screenshot({'path': image})
    await browser.close()

    bot = telegram.Bot(token=bot_token)
    await bot.send_photo(chat_id=chat_id, photo=open(image, 'rb'))


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(send_status_image())

