# coding=utf-8
__author__ = '张孟尧'
from urp.util import Constant
import time
from bs4 import BeautifulSoup


def judgment ( urp, user ):
    # 构建网址参数
    urlParameter1 = {"_t": "{:.0f}".format(time.time()),
                    "gnmkdmKey": "N4010",
                    "sessionUserKey": user.swuID}
    urlParameter2 = {"gnmkdmKey": "N4010",
                     "sessionUserKey": user.swuID}
    postData1 = {"czdmKey": "00",
                "gnmkdm": "N4010"}
    txt = urp.post(Constant.urlGetTeacherList, params = urlParameter1, data = postData1)

    soup = BeautifulSoup(txt.text, "lxml")
    all = soup.tbody
    allTeacher=[]
    for i in all:
        if type(i) is type(soup.tbody):
            sets=[i["data-kch_id"],i["data-jgh_id"],i["data-xsdm"],i["data-jxb_id"]]
            allTeacher.append(sets)
    print(allTeacher)
    for j in allTeacher:
        postData2={"kch_id":j[0],
                       "jgh_id":j[1],
                       "modelList[0].pjdxdm":j[2],
                       "jxb_id":j[3],
                       "modelList[0].pjmbmcb_id":Constant.pjmbmcb_id,
                       "modelList[0].xspfb_id":Constant.xspfb_id,
                       "modelList[0].py":"",
                       # 这里为0的话就是保存,,为1的话就是提交
                       "tjzt":"0",
                       "modelList[0].xspjList[0].pjzbxm_id":Constant.F,
                       "modelList[0].xspjList[0].childXspjList[0].pfdjdmb_id":Constant.pfdjdmb_id,
                       "modelList[0].xspjList[0].childXspjList[0].pfdjdmxmb_id":Constant.A,
                       "modelList[0].xspjList[0].childXspjList[0].pjzbxm_id":Constant.F1,
                       "modelList[0].xspjList[0].childXspjList[1].pfdjdmb_id": Constant.pfdjdmb_id,
                       "modelList[0].xspjList[0].childXspjList[1].pfdjdmxmb_id": Constant.A,
                       "modelList[0].xspjList[0].childXspjList[1].pjzbxm_id": Constant.F2,
                       "modelList[0].xspjList[0].childXspjList[2].pfdjdmb_id":Constant.pfdjdmb_id,
                       "modelList[0].xspjList[0].childXspjList[2].pfdjdmxmb_id":Constant.A,
                       "modelList[0].xspjList[0].childXspjList[2].pjzbxm_id":Constant.F3,
                       "modelList[0].xspjList[0].childXspjList[3].pfdjdmb_id": Constant.pfdjdmb_id,
                       "modelList[0].xspjList[0].childXspjList[3].pfdjdmxmb_id": Constant.A,
                       "modelList[0].xspjList[0].childXspjList[3].pjzbxm_id": Constant.F3,

                       "modelList[0].xspjList[1].pjzbxm_id": Constant.G,
                       "modelList[0].xspjList[1].childXspjList[0].pfdjdmb_id": Constant.pfdjdmb_id,
                       "modelList[0].xspjList[1].childXspjList[0].pfdjdmxmb_id": Constant.A,
                       "modelList[0].xspjList[1].childXspjList[0].pjzbxm_id": Constant.G1,
                       "modelList[0].xspjList[1].childXspjList[1].pfdjdmb_id": Constant.pfdjdmb_id,
                       "modelList[0].xspjList[1].childXspjList[1].pfdjdmxmb_id": Constant.A,
                       "modelList[0].xspjList[1].childXspjList[1].pjzbxm_id": Constant.G2,
                       "modelList[0].xspjList[1].childXspjList[2].pfdjdmb_id": Constant.pfdjdmb_id,
                       "modelList[0].xspjList[1].childXspjList[2].pfdjdmxmb_id": Constant.A,
                       "modelList[0].xspjList[1].childXspjList[2].pjzbxm_id": Constant.G3,
                       "modelList[0].xspjList[1].childXspjList[3].pfdjdmb_id": Constant.pfdjdmb_id,
                       "modelList[0].xspjList[1].childXspjList[3].pfdjdmxmb_id": Constant.A,
                       "modelList[0].xspjList[1].childXspjList[3].pjzbxm_id": Constant.G4,
                       "modelList[0].xspjList[1].childXspjList[4].pfdjdmb_id": Constant.pfdjdmb_id,
                       "modelList[0].xspjList[1].childXspjList[4].pfdjdmxmb_id": Constant.A,
                       "modelList[0].xspjList[1].childXspjList[4].pjzbxm_id": Constant.G5,
                       "modelList[0].xspjList[1].childXspjList[5].pfdjdmb_id": Constant.pfdjdmb_id,
                       "modelList[0].xspjList[1].childXspjList[5].pfdjdmxmb_id": Constant.A,
                       "modelList[0].xspjList[1].childXspjList[5].pjzbxm_id": Constant.G6,

                       "modelList[0].xspjList[2].pjzbxm_id": Constant.H,
                       "modelList[0].xspjList[2].childXspjList[0].pfdjdmb_id": Constant.pfdjdmb_id,
                       "modelList[0].xspjList[2].childXspjList[0].pfdjdmxmb_id": Constant.A,
                       "modelList[0].xspjList[2].childXspjList[0].pjzbxm_id": Constant.H1,
                       "modelList[0].xspjList[2].childXspjList[1].pfdjdmb_id": Constant.pfdjdmb_id,
                       "modelList[0].xspjList[2].childXspjList[1].pfdjdmxmb_id": Constant.A,
                       "modelList[0].xspjList[2].childXspjList[1].pjzbxm_id": Constant.H2,

                       "modelList[0].xspjList[3].pjzbxm_id": Constant.I,
                       "modelList[0].xspjList[3].childXspjList[0].pfdjdmb_id": Constant.pfdjdmb_id,
                       "modelList[0].xspjList[3].childXspjList[0].pfdjdmxmb_id": Constant.A,
                       "modelList[0].xspjList[3].childXspjList[0].pjzbxm_id": Constant.I1,
                       "modelList[0].xspjList[3].childXspjList[1].pfdjdmb_id": Constant.pfdjdmb_id,
                       "modelList[0].xspjList[3].childXspjList[1].pfdjdmxmb_id": Constant.A,
                       "modelList[0].xspjList[3].childXspjList[1].pjzbxm_id": Constant.I2,
                       "modelList[0].xspjList[3].childXspjList[2].pfdjdmb_id": Constant.pfdjdmb_id,
                       "modelList[0].xspjList[3].childXspjList[2].pfdjdmxmb_id": Constant.B,
                       "modelList[0].xspjList[3].childXspjList[2].pjzbxm_id": Constant.I3
            }
        result = urp.post(Constant.urlPost, params = urlParameter2, data = postData2)
        print(result.text)

    return
