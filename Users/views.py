#-*- coding: UTF-8 -*-
from django.shortcuts import render
import json
from public.public_api import OutputErrAndLog
from Users.InnerFunction import  CheckUserName, CheckPhoneNum, SetUserInfo
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from public.public_api import Public_Error_Code, Public_Error_Msg
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#用户注册
@csrf_exempt
def Users_Register(request):
    try:
        if 'POST' == request.method:
            userName = request.POST.get('username')
            password = request.POST.get('password')
            Email = request.POST.get('email')
            sex = request.POST.get('sex')
            ages = request.POST.get('ages')
            phoneNum = request.POST.get('phone')

            result = CheckPhoneNum(phoneNum)
            if result['retInfo'] != True:
                error = OutputErrAndLog(result['errMsg'])
                ret = {'errCode': result['errCode'],
                       'Msg' : error
                }
                return HttpResponse(json.dumps(ret), mimetype='application/json')

            SetUserInfo(userName, password, Email, sex, ages, phoneNum)

            ret = {'errCode': Public_Error_Code['SUCCESS'],
                   'Msg'    : Public_Error_Msg['SUCCESS'],
            }

            response = HttpResponse(json.dumps(ret), mimetype='application/json')
            response.set_cookie('username', userName, 3600)
            return response
        else:
            error = OutputErrAndLog(Public_Error_Msg['400BadRequest'])
            return HttpResponseBadRequest(error)
    except Exception,e:
        error = OutputErrAndLog(str(e))
        ret = {'errCode': Public_Error_Code['EXCEPTION_ERR'],
               'errMsg' : error
        }
        return HttpResponse(json.dumps(ret), mimetype='application/json')


#用户登录
@csrf_exempt
def Users_LogIn(request):
    try:
        if 'POST' == request.method:
            userName = request.POST.get('username','')
            password = request.POST.get('password','')

            usrAuth = authenticate(username = userName,password = password)
            if usrAuth and usrAuth.is_active:
                login(request, usrAuth)
                ret = {'errCode': Public_Error_Code['SUCCESS'],
                       'Msg'    : Public_Error_Msg['SUCCESS'],
                }
                response = HttpResponse(json.dumps(ret), mimetype='application/json')
                response.set_cookie('username', userName, 3600)
                return response
            else:
                error = OutputErrAndLog(Public_Error_Msg['UN_PW_AUTH_FAILED'])
                ret = {'errCode': Public_Error_Code['UN_PW_AUTH_FAILED'],
                       'errMsg' : error
                }
                return HttpResponse(json.dumps(ret), mimetype='application/json')
        else:
            error = OutputErrAndLog(Public_Error_Msg['400BadRequest'])
            return HttpResponseBadRequest(error)
    except Exception,e:
        error = OutputErrAndLog(str(e))
        ret = {'errCode': Public_Error_Code['EXCEPTION_ERR'],
               'errMsg' : error
        }
        return HttpResponse(json.dumps(ret), mimetype='application/json')

#用户登出
@csrf_exempt
def Users_LogOut(request):
    try:
        if 'POST' == request.method:
            logout(request)
            ret = {'errCode': Public_Error_Code['SUCCESS'],
                    'Msg'   : Public_Error_Msg['SUCCESS'],
                  }
            response = HttpResponse(json.dumps(ret), mimetype='application/json')
            response.delete_cookie('username')
            return response
        else:
            error = OutputErrAndLog(Public_Error_Msg['400BadRequest'])
            return HttpResponseBadRequest(error)
    except Exception,e:
        error = OutputErrAndLog(str(e))
        ret = {'errCode': Public_Error_Code['EXCEPTION_ERR'],
               'errMsg' : error
        }
        return HttpResponse(json.dumps(ret), mimetype='application/json')


#用户名校验
@csrf_exempt
def Users_CheckUsers(request, username):
    try:
        if 'GET' == request.method:

            result = CheckUserName(username)
            ret = {
                'existed'  :  result['retInfo']
            }


            if result['retInfo'] != True:
                error = OutputErrAndLog(result['errMsg'])
                ret = {'errCode': result['errCode'],
                       'Msg'    : error
                }
                return HttpResponse(json.dumps(ret), mimetype='application/json')
    except Exception, e:
        error = OutputErrAndLog(str(e))
        ret = {'errCode': Public_Error_Code['EXCEPTION_ERR'],
               'errMsg' : error
        }
        return HttpResponse(json.dumps(ret), mimetype='application/json')




