from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time
from collections import Counter 
import jieba 
import pandas as pd  
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def data_fre():
    with open('data.txt', 'r', encoding='utf-8')as f:
        txt_data = f.read()
        cut_data = jieba.lcut(txt_data)
        word_counter = dict(Counter(cut_data))                          
        Table = pd.DataFrame(columns=['vol', 'freq']) 
        Table['vol'] = list(word_counter.keys())[0:500]                 
        Table['freq'] = list(word_counter.values())[0:500]              
        Table = Table.sort_values(by=['freq'], ascending=False) 
        Table.to_excel('freq.xlsx', index=False)

data_fre()