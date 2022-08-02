# -*- coding: UTF-8 -*-

# https://github.com/dinuduke/Selenium-chrome-firefox-tips/blob/master/dissablemodelsinselenium.py
prefs = {"profile.managed_default_content_settings.images": 2,
         "profile.default_content_setting_values.notifications": 2,
         "profile.managed_default_content_settings.stylesheets": 2,
         "profile.managed_default_content_settings.cookies": 2,
         "profile.managed_default_content_settings.javascript": 1,
         "profile.managed_default_content_settings.plugins": 1,
         "profile.managed_default_content_settings.popups": 2,
         "profile.managed_default_content_settings.geolocation": 2,
         "profile.managed_default_content_settings.media_stream": 2,
         }   # 优化加载选项，没啥用
