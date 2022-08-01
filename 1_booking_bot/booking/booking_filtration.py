# -*- coding: UTF-8 -*-
# 该文件中用于筛选网站信息
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_score(self, *scores):
        star_box = self.driver.find_element(
            By.CSS_SELECTOR,
            'div[data-filters-group="review_score"]'
        )
        # find_elements 查找该类满足条件的全部子类
        star_child_elements = star_box.find_elements(
            By.CSS_SELECTOR, 'div[data-testid="filters-group-label-content"]'
        )
        for score in scores:  # 将多个score选项进行选择
            for ele in star_child_elements:
                # 通过get_attribute()获取相关变量的值，如果是innerHTML则获取全部HTML代码
                if str(ele.get_attribute('innerHTML')).find(str(score)) != -1:
                    ele.click()

    def open_sort_list(self):
        sort_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="sorters-dropdown-trigger"]'
        )
        sort_btn.click()
        sort_list = self.driver.find_element(
            By.CSS_SELECTOR,
            'div[data-testid="sorters-dropdown"]'
        )
        return sort_list

    def low_price(self):
        try:  # 该列表分两种可能，一种是下拉式的
            sort_list = self.open_sort_list()
            low_price_btn = sort_list.find_element(
                By.CSS_SELECTOR,
                'button[data-id="price"]'
            )
            low_price_btn.click()
        except:  # 一种是直接点击的
            low_price_btn = self.driver.find_element(
                By.CSS_SELECTOR,
                '#ajaxsrwrap > div:nth-child(1) > div > div > div.df83b00fbd.fe22db3bd1.bd729caef6 > ul > li:nth-child(3)'
            )
            low_price_btn.click()

