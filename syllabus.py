from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import re


results = []

options = Options()
options.add_argument('--headless')

#chromeのwebdriverオブジェクトを作成
driver = webdriver.Chrome(options=options)

#シラバスのトップ画面を開く
driver.get('https://syllabus.doshisha.ac.jp')

#検索欄の指定
subject_input_elem = driver.find_element_by_name('keyword')

search_word = input('検索語>')
#検索語の入力
subject_input_elem.send_keys(search_word)
#検索ボタンのクリック
subject_input_elem.submit()

i=1
count = 0

while driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/form[2]/input[" + str(i) + "]") != None:
    count = count + 1
    #検索結果の取得
    result_url = driver.find_elements_by_class_name('link03')

    for a in result_url:
        results.append({
            'url':a.get_attribute('href'),
            'title':re.sub("○|△|　|\n.*", "", a.text)
        })
        
    if(count != 1):
        i = 2
    #1ページ目のボタン..i=1 2ページ目以降..i=2
    next_button_elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/form[2]/input[" + str(i) + "]")
    if(next_button_elem.get_attribute("value") != "次結果一覧/Next"):
        break;
    next_button_elem.click()
    


driver.quit()

# for i in range(len(results)):
#     print(results[i]) 



