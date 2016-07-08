# coding=utf-8
from urp.Save import save
from urp.Submit import submit

__author__ = '陈思定'
# reedit：
# 重写Main，将评教/提交封装在save和submit中，传入参数实现自动提交
# by 陈思定 2016/7/8


print("正确输入用户名和密码即可自动教评,用户,密码均未上传或保存到本地,可放心使用\n"
      "默认是所有选项为优秀,最后一项为良好,您可以手动修改参数\n"
      "本程序只是将选项勾选并保存,需要您手动点击提交.\n"
      "自动提交可修改urp/Judgment.py中第36行的参数为1,再次运行程序即可自动提交.")



userName = input("请输入用户名")
userPassword = input("请输入密码")

save(userName,userPassword)
submit(userName,userPassword)

print("教评完毕,请登录教务系统查看是否成功.")
