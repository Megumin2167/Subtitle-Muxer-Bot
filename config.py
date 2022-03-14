
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN', 5224309141:AAEp0pDarnUnn_YDHSLnEkjbF2lSKCaw2j8)
    APP_ID = os.environ.get('APP_ID', 8350415)
    API_HASH = os.environ.get('API_HASH', 71ffbf3da59683b576b9552fca9bd71e)

    #comma seperated user id of users who are allowed to use

    DOWNLOAD_DIR = 'downloads'
    OWNER_ID = int(os.environ.get("OWNER_ID", 2031599474))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", AnimeArchiveXAnimeRequests)  
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", "2031599474"))
    # database session name, example: xurluploader
    SESSION_NAME = os.environ.get("SESSION_NAME", "sub_mixed_bot")
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://s1com:s1com@cluster0.wrrwz.mongodb.net/Cluster0?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001742703524"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
    DOWNLOAD_LOCATION = "./DOWNLOADS"
