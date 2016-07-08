# coding=utf-8
__author__ = '张孟尧'
from urp import Login
from urp import GetBasicInfo
from urp.util import StudentTotalInfo
from urp import Judgment



urp = Login.loginSwuEms()
user = StudentTotalInfo.userTotalInfo
GetBasicInfo.getBasicInfo(urp, user)
print(user.swuID)
Judgment.judgment(urp, user)
