# coding:utf-8
__author__ = 'Mark'
import os
import time

'''
配置全局参数
'''
# 项目的绝对路径（因为 windows执行时需要绝对路径才能执行通过）
project_path = "/Users/liuyan/Documents/myTEST/"
# 获取项目路径
# project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)[0]), '.'))
print (project_path)
# 测试用例代码存放路径（用于构建suite,注意该文件夹下的文件都应该以test开头命名）
test_case_path = project_path+"src/test_case"
# excel测试数据文档存放路径
test_data_path = project_path+"data/testData.xlsx"
# 日志文件存储路径
log_path = project_path+"log/mylog.log"
print (u'日志路径：'+log_path)
# 测试报告存储路径，并以当前时间作为报告名称前缀
report_path = project_path+"/report/"
report_name = report_path+time.strftime('%Y_%m_%d %H_%M_%S', time.localtime())
# 异常截图存储路径,并以当前时间作为图片名称前缀
img_path = project_path+"/error_img/"+time.strftime('%Y_%m_%d %H_%M_%S', time.localtime())
# 设置发送测试报告的公共邮箱、用户名和密码
smtp_sever = 'smtp.163.com'  # 邮箱SMTP服务，
email_name = 'm17623458004@163.com'  # 发件人邮箱
email_password = '19881217LJ'  # 发件人登录密码
email_To = 'ljwxj5020046@126.com'  # 收件人
