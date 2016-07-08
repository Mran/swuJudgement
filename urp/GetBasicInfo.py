# coding=utf-8
__author__ = '张孟尧'
__doc__='用来获取用户的基本信息:学号,名字'

import re


def getBasicInfo ( urp, user ):

    urlEms = "http://jw.swu.edu.cn/jwglxt/xtgl/index_initMenu.html"
    ems = urp.get( urlEms )

    # 提取学号
    userSwuID = re.search( r'[0-9]{15}', ems.text )
    user.swuID = userSwuID.group( )
    return user
