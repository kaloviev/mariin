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

    print('[INFO] Create a browser')
    browser = await launch({
        'headless': True,
        'args': ['--proxy-server="direct://"', '--proxy-bypass-list=*']
    })

    print('[INFO] Create a page')
    page = await browser.newPage()

    print('[INFO] Set user agent')
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
    
    print('[INFO] Set viewport size')
    await page.setViewport({ 'width': 800, 'height': 1000 })

    print('[INFO] Go to a page')
    await page.goto(url, { 'waitUntil': 'load', 'timeout': 0 })

    print('[INFO] Take a screenshot')
    await page.screenshot({ 'path': image })

    print('[INFO] Close the browser')
    await browser.close()

    print('[INFO] Send the screenshot')
    bot = telegram.Bot(token=bot_token)
    try:
        await bot.send_photo(chat_id=chat_id, photo=open(image, 'rb'))
    except TypeError: # ToDo: Fix this
        pass

    print('[INFO] Exit script')

if __name__ == '__main__':
    print('[INFO] Run script')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(send_status_image())

