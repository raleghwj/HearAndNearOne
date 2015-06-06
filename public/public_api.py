#-*- coding: UTF-8 -*-
from public.LogInit import LOG

Public_Error_Code = {
    #Users
    'PASSWORD_LENGTH_INVALID'  :     4001,
    'PASSWORD_CHECK_FAILED'    :     4002,
    'USERNAME_EXISTED'         :     4003,
    'PHONE_NUM_CHECK_FAILED'   :     4004,
    'UN_PW_AUTH_FAILED'        :     4005,
    'USERNAME_LENGTH_INVALID'  :     4006,
    '400BadRequest'            :     400,

    'EXCEPTION_ERR'            :     8005,
    'SUCCESS'                  :     0,
}


Public_Error_Msg = {
    #Users
    'PASSWORD_LENGTH_INVALID'  :     "请输入6到20位密码！",
    'PASSWORD_CHECK_FAILED'    :     "两次输入密码不一致！",
    'USERNAME_EXISTED'         :     "用户名已存在！",
    'PHONE_NUM_CHECK_FAILED'   :     "请输入正确的电话号码！",
    'UN_PW_AUTH_FAILED'        :     "账号或密码错误",
    'USERNAME_LENGTH_INVALID'  :     "请输入3到20位呢称",
    '400BadRequest'            :     "400错误，错误请求！",

    'SUCCESS'                  :     "成功",
}


# 输出错误并记录日志
def OutputErrAndLog(err):
    error = err
    LOG.error(err)
    return error
