# Crawler-Learning

该项目保存基于Selenium的爬虫项目

1. [入门项目](./1_booking_bot)，制作在booking.com网站上查找并筛选酒店的机器人，并且将酒店的相关信息保存到表格中. 参考教程: [Selenium Course for Beginners - Web Scraping Bots, Browser Automation, Testing (Tutorial)

  ](https://www.youtube.com/watch?v=j7VZsCCnptM&t=1020s)，视频下载（中文字幕）: [阿里云 - 1080p](https://www.aliyundrive.com/s/czAXhrjaHVN).

  - 在命令行中直接运行 `python run.py` 即可，输入想去的地方和人数.

2. [西安二手房信息获取](./2_ershoufang_bot)，制作在[贝壳二手房（西安）](https://xa.ke.com/ershoufang/)上在“必看好房”中价格从低到高，获取每一个二手房的信息，包括以下信息：

   ```text
   小区名(community_name)
   所在区(area)
   每平米单价(unit_price)
   房型(room)
   占地大小(size)
   距离最近的地铁站距离(subway)
   距离最近的公交站距离(bus)
   距离最近的幼儿园距离(kindergarten)
   距离最近的小学距离(primary-school)
   距离最近的医院距离(hospital)
   距离最近的超市距离(supermarket)
   距离最近的公园距离(park)
   ```

- 在命令行中运行 `python run.py` 即可，输入要爬取的页数范围.