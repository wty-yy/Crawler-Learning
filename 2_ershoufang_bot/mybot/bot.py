# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from mybot.my_requester import Requester
from tqdm import tqdm

class Bot(webdriver.Chrome):
    def __init__(self, driver_path, pg, teardown=False):
        self.pg = pg
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        # 取消log显示
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Bot, self).__init__(service=Service(driver_path), options=options)
        self.implicitly_wait(1)
        self.maximize_window()
        self.requester = Requester(self)  # 创建requester对象

    def load_page(self, num):
        string = '' if num == 1 else 'pg' + str(num)
        url = f'https://xa.ke.com/ershoufang/{string}co41tt9/'
        self.execute_script(f'window.open("{url}")')  # 直接打开一个新网页
        self.switch_to.window(self.window_handles[1])  # 切换句柄
        print(f'开始获取第{num}页信息...')
        sell_list_ele = self.find_element(By.CLASS_NAME, 'sellListContent')
        houses_ele = sell_list_ele.find_elements(By.CSS_SELECTOR, 'li[class="clear"]')
        for house in tqdm(houses_ele):
            fig = house.find_element(By.CSS_SELECTOR, 'li > a')
            fig.click()
            self.switch_to.window(self.window_handles[-1])  # 一定要切换当前网页句柄
            self.requester.get_info()
            self.close()
            self.switch_to.window(self.window_handles[1])
        self.requester.save_data(f'result{self.pg[0]}~{num}.csv')
        self.close()
        self.switch_to.window(self.window_handles[0])
