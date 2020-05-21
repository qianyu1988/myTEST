# 无头启动火狐浏览器
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

url = 'http://scm3-2.yunsom.cn/'

# 设置chrome为无界面浏览器
options = Options()
options.add_argument('--headless')

# 打开浏览器
browser = webdriver.Firefox(options=options)

# 利用get请求请求浏览器的一个网页
browser.get(url=url)

# # 打印输出这个网页的源代码
# print(browser.page_source)

# # 关闭浏览器
# browser.close()
#
# # 杀死chrome浏览器的连接桥(chromedriver)的进程
# browser.quit()