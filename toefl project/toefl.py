from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time
from collections import Counter 
import jieba 
import pandas as pd  
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def skipwait():
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

# 寫入單字
def Install(data):
    with open('data.txt','a',encoding='utf-8')as f:
        f.write(data)


driver = webdriver.Chrome()
# 打開TPO
driver.get('https://toeflv3.kmf.com/exam')

# 爬文章
def get_data(number):
    try:
        time.sleep(2)
        # driver.find_element(By.XPATH, f'//*[@id="js-exam-list"]/div[3]/ul/li[{number}]').click()
        driver.find_element(By.XPATH, f'//*[@data-title="准备模考：TPO-{number}"]').click()
        time.sleep(1)
        # skipwait()
        driver.find_element(By.XPATH, '//*[@id="ui-id-1"]/form/div/div[3]/ul/li/span').click() #只留閱讀題
        driver.find_element(By.XPATH, '//*[@id="ui-id-1"]/form/div/div[5]/ul/li/span').click() #只留閱讀題
        driver.find_element(By.XPATH, '//*[@id="ui-id-1"]/form/div/div[7]/ul/li/span').click() #只留閱讀題
        driver.find_element(By.XPATH, '//*[@id="ui-id-1"]/div[2]/a[1]').click() #開始模考 按鈕
        # time.sleep(2)
        skipwait()
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(1)
        # skipwait()
        driver.find_element(By.XPATH, '//div[@class = "aside"]/ul').click() #continue鈕

        for i in range(3):#閱讀有三個passage
            # time.sleep(2)
            skipwait()
            view_r = driver.find_element(By.XPATH, '//div[@class = "view-text-r"]')
            # view_r.send_keys(Keys.COMMAND + Keys.ARROW_DOWN)
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", view_r) #scroll down
            # time.sleep(1)
            skipwait()
            data = driver.find_element(By.XPATH, '//p[@class = "view-text-r-main view-padding"]').text
            Install(data)
            print(data)
            for i1 in range(15): #每passage有14題
                time.sleep(0.5)
                # skipwait()
                if i1 == 14:
                    driver.find_element(By.XPATH, '//div[@class = "aside"]/ul/li[4]').click()#轉到下一大題
                else:
                    driver.find_element(By.XPATH, '//div[@class = "aside"]/ul/li[3]').click() #next鈕
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except:
        driver.close()# 發生異常就關閉
        driver.switch_to.window(driver.window_handles[0])
# 文章拆解單字
def data_fre():
    with open('data.txt', 'r', encoding='utf-8')as f:
        txt_data = f.read()
        cut_data = jieba.lcut(txt_data)
        word_counter = dict(Counter(cut_data))                          
        Table = pd.DataFrame(columns=['vol', 'freq']) 
        Table['vol'] = list(word_counter.keys())[0:500]     #單字            
        Table['freq'] = list(word_counter.values())[0:500]  #次數           
        Table = Table.sort_values(by=['freq'], ascending=False) 
        Table.to_excel('freq.xlsx', index=False)  

# run getdata
for a in range(40, 50):
    get_data(a)
for b in range(21,35):
    get_data(b)
for c in range(16,21):
    get_data(c)

# 分析
data_fre()