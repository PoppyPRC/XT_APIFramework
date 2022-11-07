import os
import configparser

curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath,"test_config\config.ini")


class config():
    def __init__(self):
        self._config = configparser.ConfigParser()
        self._config.read(cfgpath,encoding="utf8")


    def get_http(self,name):
        value = self._config.get("HTTP",name)
        return value

    def get_xthy(self,name):
        value = self._config.get("XTHYLOGIN",name)
        return value

    def get_DB(self,name):
        value = self._config.get("DATABASE",name)
        return value

    def get_SSH(self,name):
        value = self._config.get("SSHTunnelForwarder",name)
        return value

    def get_log(self,name):
        value = self._config.get("LOG",name)
        return value

    def get_mail(self,name):
        value = self._config.get("MAIL",name)
        return value

    def get_excel(self,name):
        value = self._config.get("EXCEL",name)
        return value





if __name__ == '__main__':
    A = config()
    print(A.get_http("host"))
