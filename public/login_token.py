from get_config import config
from public.send_method import SendMethod
import jsonpath


def login():
    a = SendMethod()
    a.get_xthy_url("/api/login")
    a.get_header({'APP-DEVICE': "web"})
    a.get_data({"username": config().get_http("username"), "password": config().get_http("password")})
    response = a.post()
    token = jsonpath.jsonpath(response,"$..token")[0]
    return token


if __name__ == '__main__':
    token = login()
    print(token)