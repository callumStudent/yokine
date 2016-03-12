import os

MAIL_SERVER = "smtp.live.com"
MAIL_PORT = "587"
MAIL_DEBUG = True
MAIL_DEFAULT_SENDER = 'callum.ingley@live.com'
MAIL_USERNAME = os.environ.get('MAIL_USERNAME'), #'callum.ingley@live.com'
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_USE_TLS = True
MAIL_USE_SSL = True