import random
import time
from crawler.request_handler import get_content
from crawler.data_storage import save_data_to_db, save_data_to_excel, COLUMNS
import pandas as pd
from config.settings import PAGE_NUM

dfs = pd.read_excel('E:/中转站/搜索列表.xlsx', sheet_name='修订增强1')

def run_crawler(page_num):
    for pice, yl_name in zip(dfs['增强搜索名'], dfs['名称']):
        stop_num = 0
        df = pd.DataFrame(columns=COLUMNS)
        for page in range(1, page_num):
            content = get_content(page, pice)
            if content == "continue":
                stop_num += 1
                if stop_num % 3 == 0:
                    time.sleep(random.randint(20, 30))
                continue
            elif len(content['data']['productList']) != 0:
                for row in content['data']['productList']:
                    if 'id' in row:
                        # df = df.append({
                        #     'name': row['fullName'],
                        #     'price': row['price'],
                        #     'jumpUrl': row['jumpUrl'],
                        #     'unit': row['unit'],
                        #     'pCurrency': row['pCurrency'],
                        #     'location': row['location'],
                        #     'category': row['category'],
                        #     'fromsource': row['from'],
                        #     'minValue': row['minValue'],
                        #     'fullProviderName': row['fullProviderName'],
                        #     'dataclass': '商品外页',
                        #     'datasource': '百度爱采购',
                        #     'keyname': pice,
                        #     'createdAt': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        # }, ignore_index=True)
                        new_row = pd.DataFrame({
                            'name': [row['fullName']],
                            'price': [row['price']],
                            'jumpUrl': [row['jumpUrl']],
                            'unit': [row['unit']],
                            'pCurrency': [row['pCurrency']],
                            'location': [row['location']],
                            'category': [row['category']],
                            'fromsource': [row['from']],
                            'minValue': [row['minValue']],
                            'fullProviderName': [row['fullProviderName']],
                            'dataclass': ['商品外页'],
                            'datasource': ['百度爱采购'],
                            'keyname': [yl_name],
                            'createdAt': [time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())]
                        })

                        df = pd.concat([df, new_row], ignore_index=True)
            else:
                break
        save_data_to_db(df)
        save_data_to_excel(df, f'D:/Data_Pool/Update_Pool/{yl_name}更新.xlsx')
