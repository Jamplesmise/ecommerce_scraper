import logging

# Logging configuration
logging.basicConfig(filename=r'.\logs\crawler_errors.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Headers for requests
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Database configuration
DATABASE_URI = "mysql+pymysql://xx:xx@xxx:xx/historydatacenter"
ENGINE_OPTIONS = {
    'pool_size': 10,
    'max_overflow': 20,
    'pool_timeout': 30,
    'pool_recycle': 3600,
    'pool_pre_ping': True
}

# General settings
PAGE_NUM = 100
INTERVAL = 3600 * 12
