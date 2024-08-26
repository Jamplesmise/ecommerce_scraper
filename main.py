from crawler.scheduler import run_crawler
from utils.countdown import countdown
from utils.file_ops import copy_files_with_suffix
from config.settings import PAGE_NUM, INTERVAL

source_folder_path = 'D:/Data_Pool/Update_Pool'
target_folder_path = 'D:/Data_Pool/Static_Pool'

while True:
    run_crawler(PAGE_NUM)
    copy_files_with_suffix(source_folder_path, target_folder_path)
    countdown(INTERVAL)

# textName,
# flowCode,
# businessNo,
# provincesValue,
# date,
# number1,
# billNumber,
# sell_name,
# sell_TaxId,
# sell_address,
# buy_name,
# buy_TaxId,
# buy_address,
# money,
# taxDeduction,
# tax_total
#
#
#
#
# textName,
# flowCode,
# businessNo,
# provincesValue,
# date,
# number1,
# billNumber,
# buy_name,
# buy_TaxId,
# buy_address,
# money,
# taxDeduction,
# tax_total
#
#
#
# textName,
# flowCode,
# businessNo,
# provincesValue,
# date,
# number1,
# billNumber,
# sell_name,
# sell_TaxId,
# sell_address,
# money,
# taxDeduction,
# tax_total