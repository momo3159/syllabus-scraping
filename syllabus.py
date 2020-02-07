from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

results = []

options = Options()
options.add_argument('--headless')

#chromeのwebdriverオブジェクトを作成
driver = webdriver.Chrome(options=options)

#同志社大学のシラバスのトップ画面を開く
driver.get('https://syllabus.doshisha.ac.jp')

#検索欄の指定
subject_input_elem = driver.find_element_by_name('keyword')
#検索語の入力
subject_input_elem.send_keys('言語')
#検索ボタンのクリック
subject_input_elem.submit()

#検索結果の取得
#result = driver.find_element_by_class_name('result__table')
result_url = driver.find_elements_by_class_name('link03')

for a in result_url:
    results.append({
        'url':a.get_attribute('href'),
        'title':a.text
    })
    
for i in range(len(results)):
    print(results[i]) 

# #スクリーンショット（結果の確認のため）
# driver.save_screenshot('python.png')
# driver.quit()