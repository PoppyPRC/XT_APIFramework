import requests
from get_config import config
import json,jsonpath
from public.Log import Logs


# method = "post"
# url = "http://test.api.xthy.xthktech.cn/api/login"
# data  = {"username":"18711111111","password":"111111"}
# header = {'APP-DEVICE':"web"}
# response = requests.request(method = method,url = url,headers = header,data = data)
# print(response.json())

class SendMethod():
    def __init__(self):
        global treaty,host,xthy
        treaty = config().get_http("treaty")
        host = config().get_http("host")
        xthy = config().get_xthy("xthy_host")
        self.url= None

    def get_method(self,method):
        self.method = method

    def get_url(self,url):
        self.url = treaty + "://" + host + url

    def get_xthy_url(self,url):
        self.url = treaty + "://" + xthy + url

    def get_data(self,data):
        self.data = data

    def get_param(self,param):
        self.param = param

    def get_header(self,header):
        self.header = header


    def get(self):
        try:
            response = requests.get(url= self.url,headers = self.header,params= self.param)
            Logs().my_log("info","request_url:" + self.url)
            Logs().my_log("info","request_data:" + self.param)

            return response.json()

        except Exception as e:
            Logs().my_log("error","get请求报错:" + str(e))
            print("接口请求报错")


    def post(self):
        try:
            response = requests.post(url= self.url,headers = self.header,data = self.data)
            json_response = response.json()
            status_code = jsonpath.jsonpath(json_response, "$..status_code")[0]
            message = jsonpath.jsonpath(json_response, "$..message")[0]
            Logs().my_log("info", "request_url:" + self.url)
            Logs().my_log("info", "request_data:" + json.dumps(self.data))

            # if status_code == 200:
            return json_response
            # else:
                # Logs().my_log("error",message)


        except Exception as e:
            Logs().my_log("error","post请求报错:" + str(e))
            print("接口请求错误")


    def post_with_json(self):
        try:
            response = requests.post(url= self.url,headers = self.header,data = json.dumps(self.data))
            json_response = response.json()
            status_code = jsonpath.jsonpath(json_response, "$..status_code")[0]
            message = jsonpath.jsonpath(json_response, "$..message")[0]
            Logs().my_log("info", "request_url:" + self.url)
            Logs().my_log("info", "request_data:" + json.dumps(self.data))

            # if status_code == 200:
            return json_response
            # else:
            #     Logs().my_log("error",message)


        except Exception as e:
            Logs().my_log("error","post请求报错:" + str(e))
            print("接口请求错误")




if __name__ == '__main__':
    a = SendMethod()
    url = a.get_url("/api/login")
    re_data = {"username": "18711111111", "password": "111111"}
    re_header = {'APP-DEVICE': "web"}
    a.get_data(re_data)
    a.get_header(re_header)
    rep = a.post()
    print(rep)