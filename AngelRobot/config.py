class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 24523897
    API_HASH = "e581880ff82e201ce3dd007f06384074"

    CASH_API_KEY = "LL8FCEIOIE1JVVWD"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://iammumvx:WT32xkFzDjPMaFhafklp_DefVOMGu9tv@tiny.db.elephantsql.com/iammumvx"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001605285063)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://shivam0:shivam098@shivam0.yu9flzq.mongodb.net/?retryWrites=true&w=majority&appName=shivam0"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/581cbe3c457ff23e8baaa.jpg"

    SUPPORT_CHAT = "Earn_without_investment01"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "7012180643:AAH8d4Sul-hsfYZtT2d4EABUUQrHiBRHNhM"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "66TUPG5O3HRW"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6371766534  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
