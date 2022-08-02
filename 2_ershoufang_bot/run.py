# -*- coding: UTF-8 -*-

from mybot.bot import Bot

if __name__ == '__main__':
    st = int(input('起始页：'))
    en = int(input('终止页：'))
    with Bot(driver_path=r'D:\SeleniumDriver\chromedriver.exe',
             pg=(st, en), teardown=False) as bot:
        for i in range(st, en+1):
            bot.load_page(i)
