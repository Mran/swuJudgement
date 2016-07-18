# coding=utf-8
from urp.Save import save
from urp.Submit import submit
import tkinter as tk
import threading

__author__ = '陈思定'
# reedit：
# 重写Main，将评教/提交封装在save和submit中，传入参数实现自动提交
# by 陈思定 2016/7/8

window = tk.Tk()
window.title('swuJudgement')
window.geometry('320x135')
window.resizable(width=False,height=False)

# 用户输入区域
tk.Label(window, text='账户:',font=("黑体", "12")).grid(row=0, column=0, sticky='e')
tk.Label(window, text='密码:',font=("黑体","12")).grid(row=1, column=0, sticky='e')

username = tk.StringVar()  # 绑定变量
password = tk.StringVar()
tk.Entry(window, textvariable=username).grid(row=0, column=1)  # 初始化文本框+绑定
tk.Entry(window, textvariable=password, show='*').grid(row=1, column=1)


# 加一张西南大学开源协会的图片= =
photo = tk.PhotoImage(file='photo.jpg')
label = tk.Label(window, image=photo)
label.image = photo
label.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)


def confirm():
    global username
    global password
    global massage

    u = username.get()
    p = password.get()
    if u and p:
        try:
            threading.Thread(target=(lambda u, p:save(u,p) and submit(u,p))(u,p)).start()
            massage.set('评教成功，请登录教务系统查看.')  # 帐户名或密码错误 or 网络问题
        except:
            massage.set('服务器拒绝了请求')  # 帐户名或密码错误 or 网络问题


def cancel():
    exit()  # 退出程序


# 按钮绑定事件
tk.Button(window, text='确认', width=6, command=confirm, font=("黑体","11")).grid(row=2, column=2)
tk.Button(window, text='取消', width=6, command=cancel, font=("黑体", "11")).grid(row=2, column=3)

# 用户的反馈消息
massage = tk.StringVar()
massage.set('贡献者：Mran & xndxcsd')
tk.Label(window, textvariable=massage,font=('黑体','12','underline')).grid(row=2,column=0,columnspan=2,sticky='w')

window.mainloop()
