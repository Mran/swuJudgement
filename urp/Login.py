# coding=utf-8
__author__ = '张孟尧'
__doc__ = '''登陆教务系统'''
import requests



def loginSwuEms ( ):
    # 校内门户地址
    urlUrp = "http://urp6.swu.edu.cn/login.portal"
    # 用户信息发送目标地址
    urllogin = "http://urp6.swu.edu.cn/userPasswordValidate.portal"
    # 登陆成功后跳转网页
    urlPortal = "http://urp6.swu.edu.cn/index.portal"
    # 用户教务系统网站 Ems意为swu Educational management system
    urlEms = "http://jw.swu.edu.cn/jwglxt/idstar/index.jsp"
    dafultTimeut = 5
    # 输入用户名和密码

    userName = input("请输入用户名")
    userPassword = input("请输入密码")

    # 模拟浏览器请求头信息
    userAgent = "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0"
    postHeader = {"Accept": "text/html, application/xhtml+xml, image/jxr, */*",
                  "Accept-Language": "zh-Hans-CN, zh-Hans; q=0.5",
                  "Connection": "Keep-Alive",
                  "DNT": "1",
                  "User-Agent": userAgent,
                  "Referer": "http://urp6.swu.edu.cn/index.portal",
                  "Host": "jw.swu.edu.cn"
                  }
    # 用户登录信息
    from_data = {'goto': "http://urp6.swu.edu.cn/loginSuccess.portal",
                 'gotoOnFail': "http://urp6.swu.edu.cn/loginFailure.portal",
                 'Login.Token1': userName,
                 'Login.Token2': userPassword}


# 构建一个持续的会话
    try:
        print("开始尝试连接")
        urp = requests.session()
        urlOk = urp.get(urlUrp, timeout = dafultTimeut)

    except  requests.exceptions.ReadTimeout as e:
        print("连接超时,请检查网络")
        return -1
    except requests.exceptions.ConnectTimeout as e:
        print("连接超时,请检查网络")
        return -1
    finally:
        pass
    if urlOk:
        print("已成功连接信息门户")
        print("正在登陆信息门户")
        try:
            # 将用户账户密码post上去
            urpResponse = urp.post(urllogin, data = from_data, timeout = dafultTimeut)
            # print(urp.cookies)

            if '错误' in urpResponse.text:
                print("密码或用户名错误")
                return -1
        except requests.exceptions.ReadTimeout as e:
            print("连接超时,请检查网络")
            return -1
        except requests.exceptions.ConnectTimeout as e:
            print("连接超时,请检查网络")
            return -1
        finally:
            pass
        if urpResponse:
            print("成功登陆信息门户")
            print("正在进入教务系统")
            urp.headers.update({"Host": "https://urp6.swu.edu.cn"})
            urp.headers.update({"User-Agent": userAgent})
            urp.headers.update({"Referer": "http://urp6.swu.edu.cn/index.portal"})
            urp.headers.update({"Host": "jw.swu.edu.cn"})
            ems = urp.get(urlEms, timeout = dafultTimeut)
            print(ems.status_code)

            print("成功进入教务系统")

        return urp
