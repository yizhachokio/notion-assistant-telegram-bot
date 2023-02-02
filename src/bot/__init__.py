from bot.controller import Controller
from dotenv import load_dotenv

def startTelegramBot():
    load_dotenv("res/config/.env")
    controller = Controller()
