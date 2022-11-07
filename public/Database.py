import pymysql
from sshtunnel import SSHTunnelForwarder
from get_config import config



class Database():

    def __init__(self):
        global host,username,password,port,database
        host = config().get_DB("host")
        username = config().get_DB("username")
        password = config().get_DB("password")
        port = config().get_DB("port")
        database = config().get_DB("database")
        self.db_info = {"host":host,
                        "user":username,
                        "password":password,
                        "port":int(port),
                        "database":database,
                        "charset":"utf8"}
        self.db = None
        self.cursor = None
        self.server = None



    def Connect_DB(self):
        if config().get_SSH("SSH_Tunnel_Forwarder") == "True":
            return self.SSH_Tunnel_Forwarder()
        elif config().get_SSH("SSH_Tunnel_Forwarder") == "False":
            # self.db = pymysql.connect(self.db_info)
            self.db = pymysql.connect(host=host,user = username,password =password,port = int(port),
                                      database =database,charset = "utf8" )
            self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
            if self.cursor != None:
                return self.cursor
            else:
                print("connect error!")




    def SSH_Tunnel_Forwarder(self):
        self.server = SSHTunnelForwarder(ssh_address_or_host = config().get_SSH("ssh_address"),
                                ssh_port = int(config().get_SSH("ssh_port")),
                                ssh_username = config().get_SSH("ssh_username"),
                                ssh_password = config().get_SSH("ssh_password"),
                                remote_bind_address= ( host,int(port)))
        self.server.start()

        self.db = pymysql.connect(host = "127.0.0.1",
                            port = self.cursor.local_bind_port,
                            username = username,
                            password = password,
                            database = database,
                            charset = "utf-8")
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def get_close(self):
        if config().get_SSH("SSH_Tunnel_Forwarder") == "True":
            self.server.close()
            self.cursor.close()
            self.db.close()
        else:
            self.cursor.close()
            self.db.close()


    def get_one(self,sql):
        self.Connect_DB()
        try:
            self.cursor.execute(sql)
            value = self.cursor.fetchone()
            self.get_close()
            return value
        except Exception as e:
            self.get_close()
            return e


    def get_all(self,sql):
        try:
            self.Connect_DB()
            self.cursor.execute(sql)
            value = self.cursor.fetchall()
            self.get_close()
            return value
        except Exception as e:
            self.get_close()
            return e


if __name__ == '__main__':
    db = Database()
    value = db.get_one("SELECT * FROM teach_course;")
    print(value)

