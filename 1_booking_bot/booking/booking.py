# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import booking.constants as const
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReporter


class Booking(webdriver.Chrome):
    def __init__(self, driver_path, teardown=False):
        self.teardown = teardown  # 是否会自动关闭浏览器
        options = webdriver.ChromeOptions()
        # 关闭在cmd中运行所产生的的logs
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(executable_path=driver_path, options=options)
        self.implicitly_wait(5)  # 设置隐式等待时间second
        self.maximize_window()  # 最大化窗口

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:  # 判断是否关闭浏览器
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
        try:  # 解决从国内进入时出现弹窗的问题
            accept_btn = self.find_element(
                By.CSS_SELECTOR,
                'body > div > div > div:nth-child(2) > button'
            )
            accept_btn.click()
            accept_btn = self.find_element(
                By.ID, r"onetrust-accept-btn-handler"
            )
            accept_btn.click()
            stay_btn = self.find_element(
                By.CSS_SELECTOR,
                '#cnSiteSelect > div > p.site_select_btns > button'
            )
            stay_btn.click()
        except: pass

    def change_currency(self, currency):
        currency_btn = self.find_element(
            By.CSS_SELECTOR,
            'button[data-modal-header-async-type="currencyDesktop"]'
        )
        currency_btn.click()
        try:
            choosing_btn = self.find_element(
                By.CSS_SELECTOR,
                f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
            )
            choosing_btn.click()
        except:
            print(f'There is no {currency} currency.')

    def select_place(self, place):
        search_field = self.find_element(By.ID, 'ss')
        search_field.clear()  # 清空搜索栏
        search_field.send_keys(place)
        choose_list = self.find_element(  # 选取列表中的第一个
            By.CSS_SELECTOR,
            'li[data-i="0"]'
        )
        choose_list.click()

    def select_dates(self, check_in_date, check_out_date):
        self.implicitly_wait(5)
        check_in_element = self.find_element(
            By.CSS_SELECTOR,
            f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()
        check_out_element = self.find_element(
            By.CSS_SELECTOR,
            f'td[data-date="{check_out_date}"]'
        )
        check_out_element.click()
        self.implicitly_wait(1)

    def select_members(self, num_adult, num_child=0):
        selection_element = self.find_element(
            By.ID, "xp__guests__toggle"
        )
        selection_element.click()
        adult_elements = (self.find_element(
            By.CSS_SELECTOR,
            'button[aria-label="减少成人数量"]'
        ), self.find_element(
            By.CSS_SELECTOR,
            'button[aria-label="增加成人数量"]'
        ))
        child_elements = (self.find_element(
            By.CSS_SELECTOR,
            'button[aria-label="减少儿童数量"]'
        ), self.find_element(
            By.CSS_SELECTOR,
            'button[aria-label="增加儿童数量"]'
        ))

        def change_to_number(elements, step):
            element = elements[1 if step > 0 else 0]
            for i in range(abs(step)):
                element.click()

        change_to_number(adult_elements, num_adult - 2)
        change_to_number(child_elements, num_child)

    def click_search(self):
        search_btn = self.find_element(
            By.CSS_SELECTOR,
            'button[type="submit"]'
        )
        search_btn.click()

    def apply_filtrations(self):  # 筛选网页
        filtration = BookingFiltration(driver=self)
        filtration.apply_score(9)
        # filtration.low_price()

    def report_result(self):  # 获取酒店信息
        self.implicitly_wait(0.1)
        reporter = BookingReporter(driver=self)
        reporter.report_result()
