# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

class Requester:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.df = pd.DataFrame()

    def get_info(self):
        community_name = self.driver.find_element(
            By.CSS_SELECTOR,
            'div[class="communityName"] > a'
        ).get_attribute('innerHTML')
        area = self.driver.find_element(
            By.CSS_SELECTOR,
            'div[class="areaName"] > span.info > a'
        ).get_attribute('innerHTML')
        unit_price = self.driver.find_element(
            By.CSS_SELECTOR,
            'span[class="unitPriceValue"]'
        ).get_attribute('innerHTML')
        room = self.driver.find_element(
            By.CSS_SELECTOR,
            'div[class="room"] > div[class="mainInfo"]'
        ).get_attribute('innerHTML')
        size = self.driver.find_element(
            By.CSS_SELECTOR,
            'div[class="area"] > div[class="mainInfo"]'
        ).get_attribute('innerHTML')
        info_table = [community_name, area, unit_price, room, size]
        box_ele = self.driver.find_element(
            By.CSS_SELECTOR,
            'div[class="tabBox"]'
        )
        select_btn = box_ele.find_elements(
            By.CSS_SELECTOR,
            'li[class*="LOGCLICK"]'
        )
        idxes = [['subway', 'bus'],
                 ['kindergarten', 'primary-school'],
                 ['hospital'],
                 ['supermarket'],
                 [],
                 ['park']]
        for i, btn in enumerate(select_btn):
            if i == 4: continue
            btn.click()
            sleep(0.2)
            for j, idx in enumerate(idxes[i]):
                item_btn = box_ele.find_element(
                    By.CSS_SELECTOR,
                    f'div[data-bl="{idx}"]'
                )
                if j > 0 or idx == 'supermarket':
                    item_btn.click()
                    sleep(0.2)
                value = None
                try:
                    value = box_ele.find_element(
                        By.CSS_SELECTOR,
                        'ul[class="itemBox"] span[class="itemText itemdistance"]'
                    ).get_attribute('innerHTML')
                except: pass
                info_table.append(value)
        cols = ['community_name', 'area', 'unit_price', 'room', 'size'] +\
               [item for sublist in idxes for item in sublist]
        df = pd.DataFrame([info_table], columns=cols)
        self.df = self.df.append(df)
        #print(df)

    def save_data(self, fname):
        #self.df.reset_index()
        #print(self.df)
        self.df.to_csv(fname, index=False)
