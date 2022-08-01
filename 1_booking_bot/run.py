# -*- coding: UTF-8 -*-

from booking.booking import Booking

# 在退出该层后，bot会自动销毁，会调用bot.__exit__()可以将浏览器关闭
with Booking(driver_path=r"D:\SeleniumDriver\chromedriver.exe",
             teardown=False) as bot:
    bot.land_first_page()
    bot.change_currency(currency='CNY')
    bot.select_place(input("去旅游的位置："))
    bot.select_dates(check_in_date='2022-08-05',
                     check_out_date='2022-08-29')
    bot.select_members(int(input("人数：")))
    bot.click_search()
    bot.apply_filtrations()
    bot.refresh()  # 重新获取信息，保证获取信息和当前网页一致
    bot.report_result()
