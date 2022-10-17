
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN', '5611453552:AAHlth_HGJ9bYrT5R-ynENsYGfMCu15z3aM')
    APP_ID = os.environ.get('APP_ID', '11727095')
    API_HASH = os.environ.get('API_HASH', '6f36129da1a6050ee10ece4fa99db6f0')

    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','105831105').split(',')]

    DOWNLOAD_DIR = 'downloads'
