# (c) @AbirHasan2005

from bot.get_cfg import get_config

class Config(object):
    # You can keep this default
    SESSION_NAME = get_config("SESSION_NAME", "AHCompressorBot")
    # Put MongoDB URL
    DATABASE_URL = get_config("DATABASE_URL", "mongodb+srv://lavanya143111443:wJ4EhAF0jCUOm35Z@cluster0.llqwyeo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    # get a token from @BotFather
    TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", "")
    # The Telegram API things
    APP_ID = int(get_config("APP_ID", 22554523))
    API_HASH = get_config("API_HASH", "d3cd72e44e4160ce1ee0b7947e8f2d89")
    LOG_CHANNEL = get_config("LOG_CHANNEL")
    UPDATES_CHANNEL = get_config("UPDATES_CHANNEL", None) # Without `@` LOL
     # Get these values from my.telegram.org
    # array to store the channel ID who are authorized to use the bot
    AUTH_USERS = set(
        int(x) for x in get_config(
            "AUTH_USERS",
            should_prompt=True
        ).split()
    )
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = get_config("DOWNLOAD_LOCATION", "/app/downloads")
    # Telegram maximum file upload size
    BOT_USERNAME = get_config("BOT_USERNAME", "Compressor_reBot")
    MAX_FILE_SIZE = 2097152000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 2097152000
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = get_config("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = get_config("HTTP_PROXY", None)
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = get_config("FINISHED_PROGRESS_STR", "▓")
    UN_FINISHED_PROGRESS_STR = get_config("UN_FINISHED_PROGRESS_STR", "░")
    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "Log.txt")
      # because, https://t.me/c/1494623325/5603
    SHOULD_USE_BUTTONS = get_config("SHOULD_USE_BUTTONS", False)
