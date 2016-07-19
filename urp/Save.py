# coding=utf-8

__author__="陈思定"

from urp import GetBasicInfo
from urp import Judgment
from urp import Login
from urp.util import StudentTotalInfo

def save(username, userpassword):
    urp = Login.loginSwuEms(username, userpassword)
    user = StudentTotalInfo.userTotalInfo
    GetBasicInfo.getBasicInfo(urp, user)
    print(user.swuID)
    Judgment.judgment(urp, user, 0)
    return

