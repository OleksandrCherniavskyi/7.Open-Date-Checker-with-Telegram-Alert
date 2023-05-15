import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import time
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import schedule
import datetime
import asyncio


current_time = datetime.datetime.now()
time_name_2 = current_time.strftime("%Y-%m-%d %H:%M:%S")
time_name = current_time.strftime("%Y%m%d_%H%M%S")
file_name = (f'{time_name}.png')

options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Bot is run")


async def open_date(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    while True:
        driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
        driver.get('https://registration.mfa.gov.ua/qmaticwebbooking/#/')
        driver.add_cookie({"name": "foo", "value": "bar"})
        time.sleep(3)
        driver.refresh()
        time.sleep(3)
        # chose location
        try:
            poland = driver.find_element(By.XPATH, "//button[contains(@class, 'region-expansion-panel')]")
            # poland = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'region-expansion-panel')]"))).click()
            poland.click()
        except NoSuchElementException:
            driver.quit()
        time.sleep(3)
        try:
            # Lublin
            lublin = driver.find_element(By.CSS_SELECTOR,
                                         "#branchGroup1 > div > div > div > div > div > div > div > div > "
                                         "div:nth-child(2) > div")
            lublin.click()
            ## Warszawa
            #warszawa = driver.find_element(By.XPATH, "//div[contains(@class, 'v-input--selection-controls__input')]")
            #warszawa.click()
        except NoSuchElementException:
            driver.quit()
        time.sleep(2)
        
        # chose service
        try:
            # Another
            another = driver.find_element(By.CSS_SELECTOR,
                                          "#step2 > div > div > div > div:nth-child(2) > div > div > div > "
                                          "div.v-input.radio-container.d-flex.hide-border.v-input--hide-details."
                                          "theme--light.v-input--selection-controls.v-input--radio-group.v-input"
                                          "--radio-group--column > div > div > div > div:nth-child(1) > div > "
                                          "div.v-radio.service-name.ma-2.pa-0.me-1.theme--light")
            another.click()
            # Ready_passport
            # ready_passport = driver.find_element(By.CSS_SELECTOR, "#step2 > div > div > div > div:nth-child(2) > div > div > div > div.v-input.radio-container.d-flex.hide-border.v-input--hide-details.theme--light.v-input--selection-controls.v-input--radio-group.v-input--radio-group--column > div > div > div > div:nth-child(1) > div > div.v-radio.service-name.ma-2.pa-0.me-1.theme--light")
            # ready_passport.click()
            ## Create new passport 16+
            #create_new_passport_16 = driver.find_element(By.CSS_SELECTOR, '#step2 > div > div > div > div:nth-child(2)'
            #                                                              ' > div > div > div > div.v-input.radio-'
            #                                                              'container.d-flex.hide-border.v-input--'
            #                                                              'hide-details.theme--light.v-input--selection'
            #                                                              '-controls.v-input--radio-group.v-input--radio'
            #                                                              '-group--column > div > div > div > div:'
            #                                                              'nth-child(5) > div > div.v-radio.service-'
            #                                                              'name.ma-2.pa-0.me-1.theme--light')
            #create_new_passport_16.click()
        except NoSuchElementException:
            driver.quit()
        time.sleep(3)
        
        # Check calendar
        try:
            element = driver.find_element(By.XPATH, "//*[contains(text(), 'На вибрану дату немає вільних місць')]")
            next_month = driver.find_element(By.XPATH, "//button[contains(@id, 'nextMonthID')]")
            next_month.click()
            time.sleep(3)
            element = driver.find_element(By.XPATH, "//*[contains(text(), 'На вибрану дату немає вільних місць')]")
            next_month = driver.find_element(By.XPATH, "//button[contains(@id, 'nextMonthID')]")
            next_month.click()
            time.sleep(2)
            element = driver.find_element(By.XPATH, "//*[contains(text(), 'На вибрану дату немає вільних місць')]")
            # print(f"Not open the date {time_name}")
            with open("log.txt", "a") as file:
                # Write some text to the file
                file.write(f"Not open the date {time_name_2}\n")
        except NoSuchElementException:
            answer = (f"Open date {time_name_2}")
            await update.message.reply_text(answer)
            kontakt = driver.find_element(By.CSS_SELECTOR, "#step3 > div > div > div > div.time-selection-wrapper")
            # Create screnshot
            screen = kontakt.screenshot(file_name)
            if screen:
                await context.bot.send_document(chat_id=update.effective_chat.id, document=open(f'{file_name}', 'rb'))
            os.remove(file_name)
            with open("log.txt", "a") as file:
                # Write some text to the file
                file.write(f"Open the date {time_name_2}\n")
            print("Open the date.")
        driver.quit()
        await asyncio.sleep(90)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

    def error(update, context):
        print(f"Update {update} caused error {context.error}")


async def logfile(update, context):
    await context.bot.send_document(chat_id=update.effective_chat.id, document=open('log.txt', 'rb'))

if __name__ == '__main__':
    application = ApplicationBuilder().token('YOUR_TOKEN').build()
    # Start_command
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    # Echo_command
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, open_date))

    # Custom_command
    logfile = CommandHandler("logfile", logfile)
    application.add_handler(logfile)
    
    # unknown_command
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)


    application.run_polling()
