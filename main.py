# tested on chrome 132.0.6834.84
# сделано с любовью от S (afteroid)
#    _   ___ _____ ___ ___  ___ ___ ___  
#   /_\ | __|_   _| __| _ \/ _ \_ _|   \ 
#  / _ \| _|  | | | _||   / (_) | || |) |
# /_/ \_\_|   |_| |___|_|_\\___/___|___/ 
                                        
import asyncio
from typing import BinaryIO

from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Screenshot import Screenshot
from aiogram.types import FSInputFile
from io import BytesIO
import time
import os
from typing import List
import aiogram
import aiosqlite
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, CallbackQuery
from aiogram.client.default import DefaultBotProperties
from cryptography.fernet import Fernet

from aiogram.enums import ParseMode
bot = Bot("TOKEN", default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-sandbox")

if os.path.exists("pasjdczmsjdhjkashdlksda.key"):
    with open("pasjdczmsjdhjkashdlksda.key", "rb") as key_file:
        key = key_file.read()
else:
    # Генерация и сохранение ключа
    key = Fernet.generate_key()
    with open("pasjdczmsjdhjkashdlksda.key", "wb") as key_file:
        key_file.write(key)

cipher_suite = Fernet(key)


async def handle_task(callback: CallbackQuery, username: str, password: str, action: str):
    await callback.message.answer(f"Выполняю, ожидайте")
    await run_selenium_task(username, password, action, callback)

async def run_selenium_task(username: str, password: str, action: str, callback: CallbackQuery):
    ob = Screenshot.Screenshot()
    service = Service(r"CHROME_DRIVER")
    browser = webdriver.Chrome(service=service, options=options)

    try:
        browser.set_window_size(1050, 1000)
        browser.get("https://elschool.ru/logon/index")

        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "login"))
        )

        entry_wrapper_btn = browser.find_element(By.CSS_SELECTOR, "div.btn.btn-light.col.entry-wrapper-btn")
        browser.execute_script("arguments[0].click();", entry_wrapper_btn)

        find_login = browser.find_element(By.ID, "login")
        browser.execute_script("arguments[0].scrollIntoView();", find_login)
        time.sleep(1)
        find_login.send_keys(username)
        find_password = browser.find_element(By.ID, "password")
        find_password.send_keys(password)
        find_password.send_keys(Keys.RETURN)



        if action == "dz":
            browser.get("https://elschool.ru/users/diaries")
            topnav = browser.find_element(By.CSS_SELECTOR, "p")
            browser.execute_script("arguments[0].setAttribute('style', 'position: absolute; top: 0px;')", topnav)
            topnav2 = browser.find_element(By.CSS_SELECTOR, "div.navbar-cheat")
            browser.execute_script("arguments[0].setAttribute('style', 'position: absolute; top: 0px;')", topnav2)
            topnav3 = browser.find_element(By.CSS_SELECTOR, "nav.fixed-top.justify-content-start")
            browser.execute_script("arguments[0].setAttribute('style', 'position: absolute; top: 0px;')", topnav3)
            topnav4 = browser.find_element(By.CSS_SELECTOR, "div.navigation.d-flex")
            browser.execute_script("arguments[0].setAttribute('style', 'position: absolute; top: 0px;')", topnav4)
        elif action == "dz2":
            browser.get("https://elschool.ru/users/diaries")
            nextweek = browser.find_element(By.CSS_SELECTOR, "i.fa.fa-chevron-right")
            browser.execute_script("arguments[0].click();", nextweek)
            topnav = browser.find_element(By.CSS_SELECTOR, "p")
            browser.execute_script("arguments[0].setAttribute('style', 'position: absolute; top: 0px;')", topnav)
            topnav2 = browser.find_element(By.CSS_SELECTOR, "div.navbar-cheat")
            browser.execute_script("arguments[0].setAttribute('style', 'position: absolute; top: 0px;')", topnav2)
            topnav3 = browser.find_element(By.CSS_SELECTOR, "nav.fixed-top.justify-content-start")
            browser.execute_script("arguments[0].setAttribute('style', 'position: absolute; top: 0px;')", topnav3)
            topnav4 = browser.find_element(By.CSS_SELECTOR, "div.navigation.d-flex")
            browser.execute_script("arguments[0].setAttribute('style', 'position: absolute; top: 0px;')", topnav4)
        elif action == "itog":
            browser.get("https://elschool.ru/users/diaries")
            itog_link = browser.find_element(By.LINK_TEXT, "Итоговые")
            itog_link.click()
            topnav = browser.find_element(By.CSS_SELECTOR, "p")
            browser.execute_script("arguments[0].setAttribute('style', 'position: absolute; top: 0px;')", topnav)
            topnav2 = browser.find_element(By.CSS_SELECTOR, "div.navbar-cheat")
            browser.execute_script("arguments[0].setAttribute('style', 'position: absolute; top: 0px;')", topnav2)
            topnav3 = browser.find_element(By.CSS_SELECTOR, "nav.fixed-top.justify-content-start")
            browser.execute_script("arguments[0].setAttribute('style', 'position: absolute; top: 0px;')", topnav3)
            topnav4 = browser.find_element(By.CSS_SELECTOR, "div.navigation.d-flex")
            browser.execute_script("arguments[0].setAttribute('style', 'position: absolute; top: 0px;')", topnav4)
            browser.set_window_size(1250, 1000)
            blackmode2 = browser.find_elements(By.CSS_SELECTOR, ".DivForResultsTable .ResultsTable .results-mark")
            for element in blackmode2:
                browser.execute_script("arguments[0].setAttribute('style', 'color: #000')", element)

        elif action == "tabel":
            browser.get("https://elschool.ru/users/diaries")
            tab_link = browser.find_element(By.LINK_TEXT, "Табель")
            tab_link.click()
            topnav = browser.find_element(By.CSS_SELECTOR, "div.navigation")
            browser.execute_script("arguments[0].setAttribute('style', 'position: absolute; top: 0px;')", topnav)
            topnav2 = browser.find_element(By.CSS_SELECTOR, "div.navbar-cheat")
            browser.execute_script("arguments[0].setAttribute('style', 'position: absolute; top: 0px;')", topnav2)
            topnav3 = browser.find_element(By.CSS_SELECTOR, "nav.fixed-top.justify-content-start")
            browser.execute_script("arguments[0].setAttribute('style', 'position: absolute; top: 0px;')", topnav3)

        blackmode = browser.find_element(By.CSS_SELECTOR, ":root")
        browser.execute_script("arguments[0].setAttribute('style', '--default-back: #474747; --default-back-second: #474747; --default-border: #000; --default-border-bold: #000; --default-header: #474747; --default-font: #fff;');", blackmode)
        blackmode2 = browser.find_elements(By.CSS_SELECTOR, ".DivForGradesTable .GradesTable .grades-average")
        for element in blackmode2:
            browser.execute_script("arguments[0].setAttribute('style', 'color: #000')", element)

        # Снимок экрана
        img = ob.full_screenshot(browser, save_path='.', image_name='screenshot.png')
        screenshot_image = Image.open('screenshot.png')


        table = browser.find_element(By.CSS_SELECTOR, "main.container-fluid")
        location = table.location
        size = table.size
        left = location['x']
        top = location['y']
        right = left + size['width']
        bottom = top + size['height']
        table_image = screenshot_image.crop((left, top, right, bottom))
        table_image.save('table_screenshot.png')

        await callback.message.answer_photo(photo=FSInputFile('table_screenshot.png'), caption='Ваши данные')

    finally:
        browser.quit()

async def start_create():
    async with aiosqlite.connect('users.db') as db:
        await db.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        tg_id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
                    )
                ''')
        await db.commit()

@dp.message(Command("change"))
async def change_user_info(message: types.Message):
    try:
        _, username, password = message.text.split()
        tg_id = int(message.from_user.id)
        encrypted_username = cipher_suite.encrypt(username.encode()).decode()
        encrypted_password = cipher_suite.encrypt(password.encode()).decode()

        async with aiosqlite.connect('users.db') as db:
            await db.execute('''
                        CREATE TABLE IF NOT EXISTS users (
                            tg_id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL,
                            password TEXT NOT NULL
                        )
                    ''')
            await db.execute('''
                INSERT INTO users (tg_id, username, password)
                VALUES (?, ?, ?)
            ''', (tg_id, encrypted_username, encrypted_password))
            await db.commit()
        await message.reply("Информация успешно обновлена!")
    except ValueError:
        await message.reply("Неверный формат команды.")
    except Exception as e:
        await message.reply(f"Можно использовать только 1 аккаунт! {e}")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

@dp.message(Command('start'))
async def start(message: types.Message):
    catalog = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Табель', callback_data='tabel')],
        [InlineKeyboardButton(text='Итоговые', callback_data='itog')],
        [InlineKeyboardButton(text='Д/З', callback_data='dz'), InlineKeyboardButton(text='След. Д/З', callback_data='dz2')],
        [InlineKeyboardButton(text='Настройки', callback_data='settings')],
        [InlineKeyboardButton(text='Открытый исходный код', url='https://github.com/Afteroid/elschool/')]])
    await message.answer("Выберите что хотите узнать\n\n(если бот не отвечает долгое время значит вы стоите в очереди, в скорем времени бот ответит вам)", reply_markup=catalog)

@dp.callback_query(F.data.in_({"dz", "dz2", "itog", "tabel"}))
async def handle_callback(callback: CallbackQuery):
    async with aiosqlite.connect('users.db') as db:
        async with db.execute('SELECT username, password FROM users WHERE tg_id = ?',
                              (callback.from_user.id,)) as cursor:
            user = await cursor.fetchone()
            if user:
                encrypted_username, encrypted_password = user

                decrypted_username = cipher_suite.decrypt(encrypted_username.encode()).decode()
                decrypted_password = cipher_suite.decrypt(encrypted_password.encode()).decode()

                action = callback.data

                asyncio.create_task(handle_task(callback, decrypted_username, decrypted_password, action))
            else:
                await callback.message.reply("Пользователь не найден. Пожалуйста, используйте команду /change для регистрации.\n(пример: /change логин пароль")

@dp.callback_query(F.data == "settings")
async def settings(callback: CallbackQuery):
    catalog = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Удалить профиль', callback_data='del')],
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ])
    await callback.message.answer("Настройки:", reply_markup=catalog)
    await callback.message.delete()

@dp.callback_query(F.data == "del")
async def delete(callback: CallbackQuery):
    tg_id = int(callback.from_user.id)
    async with aiosqlite.connect('users.db') as db:
        await db.execute('''DELETE FROM users WHERE tg_id = ?''', (tg_id,))
        await db.commit()
    await callback.message.answer("Профиль успешно удален! Используйте /start для дальнейшого использования")
    await callback.message.delete()

async def main():
    await start_create()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
