# Database Settings
SECRET_KEY = "fajderfoDGSnGSbvsKKNoabooSegeue"
SQLALCHEMY_TRACK_MODIFICATIONS = True
DATABASE_NAME = "yokinearchers$yokine"
DB_USERNAME = "yokinearchers"
DB_PASSWORD = "VGKKpxGXoCrXyHTRYcFN"
SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://%s:%s@yokinearchers.mysql.pythonanywhere-services.com/%s" % (DB_USERNAME, DB_PASSWORD, DATABASE_NAME)
SQLALCHEMY_POOL_RECYCLE = 280
SQLALCHEMY_POOL_TIMEOUT = 20

# Mail Settings
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = "465"
MAIL_DEBUG = True
MAIL_DEFAULT_SENDER = 'yokinearcheryclub@gmail.com'
MAIL_USERNAME = "yokinearcheryclub@gmail.com" #os.environ.get('MAIL_USERNAME'), #'callum.ingley@live.com'
MAIL_PASSWORD = "R0bert1ngley" #os.environ.get('MAIL_PASSWORD')
MAIL_USE_TLS = False
MAIL_USE_SSL = True

NEWS_LIMIT = 5