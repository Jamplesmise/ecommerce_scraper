import requests
import random
import time
import logging
from config.settings import HEADERS


def get_content(page, search_name):
    try:
        random_number = random.randint(1, 2)
        time.sleep(random_number)
        url = (
            f'https://b2b.baidu.com/s/a?ajax=1&csrf_token=41df759e58ad17df389cd94e900a8401&logid=502191419308248609&fid=0%2C1715909477185&_=1715910571680&q={search_name}'
            f'&from=search&pi=b2b.s.search...5440980814110092&o=0&p={page}'
            '&mk=%E5%85%A8%E9%83%A8%E7%BB%93%E6%9E%9C&f=[]&s=30&adn=0&resType=product&fn=%7B%22brand_name%22:%22%E5%93%81%E7%89%8C%22,%22select_param6%22:%22%E5%B7%A5%E8%89%BA%22,%22select_param5%22:%22%E7%94%A8%E9%80%94%22,%22select_param1%22:%22%E7%B1%BB%E5%9E%8B%22,%22select_param4%22:%22%E8%AE%A1%E9%87%8F%E5%8D%95%E4%BD%8D%22,%22select_param2%22:%22%E7%99%BD%E5%BA%A6%22,%22select_param3%22:%22%E5%B9%B3%E6%9D%BF%E8%A7%84%E6%A0%BC%22%7D'
        )
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        print(url)
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Request error: {e}")
        return "continue"
    except ValueError as e:
        logging.error(f"JSON decoding error: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None
