# -*- coding: UTF-8 -*-
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import pandas as pd
import re


class BookingReporter:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def report_result(self):
        hotel_boxes = self.driver.find_element(
            By.ID,
            'search_results_table'
        )
        hotels = hotel_boxes.find_elements(
            By.CSS_SELECTOR,
            'div[data-testid="property-card"]'
        )
        print(f'找到{len(hotels)}个酒店')
        info_table = []
        for hotel in hotels:
            name = hotel.find_element(
                By.CSS_SELECTOR,
                'div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()
            price = hotel.find_element(
                By.CSS_SELECTOR,
                'div[data-testid="price-and-discounted-price"]'
            ).find_elements(By.CSS_SELECTOR, '*')[-1] \
                .get_attribute('innerHTML').strip()
            score = None
            try:
                score = hotel.find_element(By.CSS_SELECTOR, r'div[aria-label*="评分"]') \
                    .get_attribute('innerHTML').strip()
            except:
                try:
                    score = hotel.find_element(By.CLASS_NAME, r'b5cd09854e.f0d4d6a2f5.e46e88563a') \
                        .get_attribute('innerHTML').strip()
                    score = re.findall(r'\d*\.?\d*', score)
                    score = ''.join(score)
                except: pass
            info_table.append([name, price, score])
        df = pd.DataFrame(info_table, columns=['name', 'price', 'score'])
        df.to_csv('result.csv', index=False)
        print(df)
        print('已保存到result.csv文件中')
