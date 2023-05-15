# Open Date Checker with Telegram Alert

This is a small script that checks the availability of open dates on the [mfa.gov.ua](https://registration.mfa.gov.ua/qmaticwebbooking/#/) website and sends an alarm through Telegram if a date is available.

## Dependencies

- Python 3
- Selenium (for checking open dates)
- webdriver_manager (for managing the web driver)
- python-telegram-bot (for sending Telegram alerts)

## Installation

### Using Docker

1. In the `.codesandbox` folder, you can find the Dockerfile, requirements.txt, and main.py files.
2. Build the Docker image and start the container using the provided files.

### Manual Installation

1. Create a virtual environment and activate it:
   ```shell
   python3 -m venv /workspace/venv
   source /workspace/venv/bin/activate
   
 2. Install the key libraries:
    ```shell
    pip install selenium
    pip install webdriver_manager
    pip install python-telegram-bot
  
 3. Create your Telegram bot using [@BotFather](https://t.me/botfather). Make sure to obtain the bot [token](https://core.telegram.org/bots/tutorial#obtain-your-bot-token), which you'll need for your code.

### Configuration
- Modify the code to set the desired location and service to check for open dates. You can use driver.find_element(By.CSS_SELECTOR, "<your CSS selector>") to locate elements on the page.
- Adjust the frequency of script execution with asyncio.sleep(<time in seconds>).
- When running python main.py, connect to your bot and type "/start" in the chat. You should receive a message saying "Bot is running" and then type the next message to start the echo function.
- If the bot finds an open date, it will send you a message and a screenshot of the available date.


