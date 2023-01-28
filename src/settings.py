# import os


import i18n
from dotenv import load_dotenv, find_dotenv


def setup():
    load_dotenv("res/config/.env")
    #
    # print("here")
    # print("Your text:", i18n.t("tr.default_reply")) # Hello world !

# Usage:
# my_secret_key = os.getenv("SECRET_KEY")
