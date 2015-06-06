#-*- coding: UTF-8 -*-
from Users.models import UserInfo
from public.public_api import Public_Error_Code, Public_Error_Msg
import re


def CheckPassword(password, AgainPassword):
    errCode = 0
    errMsg = []
    ret = False

    if len(password) < 6 or len(password) > 20:
        errCode = Public_Error_Code['PASSWORD_LENGTH_INVALID']
        errMsg = Public_Error_Msg['PASSWORD_LENGTH_INVALID']
    elif password != AgainPassword:
        errCode = Public_Error_Code['PASSWORD_CHECK_FAILED']
        errMsg = Public_Error_Msg['PASSWORD_CHECK_FAILED']
    else:
        errCode = 0
        ret = True
    #return [ret,errCode,errMsg]
    return {'retInfo': ret,
             'errCode': errCode,
             'errMsg' : errMsg}


def CheckUserNameLen(userName):
    errCode = 0
    errMsg = ""
    ret = False

    reRet = re.match(r"\w{3,20}", userName)
    if reRet is None:
        errCode = Public_Error_Code['USERNAME_LENGTH_INVALID']
        errMsg = Public_Error_Msg['USERNAME_LENGTH_INVALID']
    else:
        errCode = Public_Error_Code['SUCCESS']
        errMsg = Public_Error_Msg['SUCCESS']
        ret =True
    return {'retInfo' : ret,
            'errCode' : errCode,
            'errMsg'  : errMsg}


def CheckUserName(userName):
    errCode = 0
    errMsg = ""
    ret = False

    checkRet = CheckUserNameLen(userName)
    if 'False' == checkRet['retInfo']:
        return checkRet

    usrNameFilter = UserInfo.objects.filter(username = userName)
    if len(usrNameFilter) > 0:
        errCode = Public_Error_Code['USERNAME_EXISTED']
        errMsg = Public_Error_Msg['USERNAME_EXISTED']
    else:
        errCode = 0
        ret = True
    return {'retInfo' : ret,
             'errCode': errCode,
             'errMsg' : errMsg}


def CheckPhoneNum(phoneNum):
    errCode = 0
    errMsg = ""
    ret = False

    reRet = re.match(r"\d{6,15}", phoneNum)
    if reRet is None:
        errCode = Public_Error_Code['PHONE_NUM_CHECK_FAILED']
        errMsg = Public_Error_Msg['PHONE_NUM_CHECK_FAILED']
    else:
        errCode = 0
        ret = True
    return {'retInfo': ret,
             'errCode': errCode,
             'errMsg' : errMsg}


def SetUserInfo(userName, password, Email, sex, ages, phoneNum):
    usrInfo = UserInfo()

    usrInfo.username = userName
    usrInfo.set_password(password)
    usrInfo.email = Email
    usrInfo.sex = sex
    usrInfo.ages = ages
    usrInfo.phoneNum = phoneNum
    usrInfo.stat = 'S0A'
    usrInfo.save()

