from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import re


results = []


options = Options()
options.add_argument('--headless')

# chromeのwebdriverオブジェクトを作成
driver = webdriver.Chrome(options=options)

# 近畿の運行情報の画面を開く
driver.get('https://transit.yahoo.co.jp/traininfo/area/6/')

result_url = driver.find_element_by_xpath(
    '//*[@id="mdStatusTroubleLine"]/div[2]')

print(result_url.text)
driver.quit()
