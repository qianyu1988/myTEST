# coding=utf-8
__author__ = 'Mark'
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
# 谷歌静默模式
option = webdriver.ChromeOptions()
option.add_argument('--headless')  # 静默模式

# 火狐静默模式
# option = webdriver.FirefoxOptions()
# option.add_argument('--headless')  # 静默模式


# 配置地址
test2 = "http://scm3-2.yunsom.cn/"
test1 = "http://scm3.yunsom.cn/"
online = "https://scm3.yunsom.com/"


# 测试参数
username = "17623458022"
password = "123123"
captcha = "111111"


#元素定位
Confirm_login = "ant-btn"
settingxpath = "//*[@id='root']/section/section/aside/div/div/div[1]/div/div[7]/img"
settingcss = "#root .ys-sider-1st-menu-item___3HtUC:nth-child(7)>img"
user_m = "用户管理"
user_r = "角色管理"
loginname = "//*[@id='logins_phone']"
loginpassword = "//*[@id='logins_password']"
longincaptcha = "//input[@id='logins_captcha']"



driver = webdriver.Chrome(chrome_options=option)
# driver = webdriver.Firefox(firefox_options=option)
driver.get(test2)
time.sleep(2)

driver.find_element_by_xpath(loginname).send_keys(username)
driver.find_element_by_xpath(loginpassword).send_keys(password)
driver.find_element_by_xpath(longincaptcha).send_keys(captcha)
driver.find_element_by_class_name(Confirm_login).click()
time.sleep(2)
# 选择设置菜单
# driver.find_element_by_xpath(settingxpath).click()
driver.find_element_by_css_selector(settingcss).click()
time.sleep(2)
# 选择用户管理菜单
driver.find_element_by_link_text(user_m).click()
print(driver.title)
