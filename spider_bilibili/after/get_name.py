from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.bilibili.com/video/BV1qW411H7UX")
time.sleep(5)
pages = browser.find_elements_by_xpath('//div[@class="link-content"]/span[@class="part"]')
title = browser.find_element_by_xpath('//span[@class="tit tr-fix"]')
print(title.text)
# for i in pages:
#     print(i.text)
browser.quit()

