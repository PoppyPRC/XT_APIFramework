import smtplib
from get_config import config
from email.mime.text import MIMEText    # 纯文本邮件
from email.utils import parseaddr,formataddr
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from public.Log import Logs


# text_message = MIMEText("桃之夭夭，灼灼其华", 'plain' ,"utf8")
# html_message = MIMEText("<html><body><p>桃之夭夭，灼灼其华<a href='http://www.baidu.com'>百度一下</a><p><body><html>",'html','utf8')

# def _format_addr(s):
#     name,addr = parseaddr(s)
#     return formataddr((Header(name,"utf8").encode(),addr))
#
# mail_send = config().get_mail("mail_send")
# mail_passwd = config().get_mail("mail_passwd")
# mail_sever = config().get_mail("mail_sever")
# reciver = config().get_mail("reciver")
# mail_port = config().get_mail("mail_port")
# #
# # text_message['From'] = _format_addr("poppy <%s>" % mail_send) # 显示发件人
# # text_message['to'] = _format_addr("lisa <%s>" % reciver)    # 显示收件人
# # text_message['subject'] = Header("接口测试报告","utf-8").encode()  # 显示主题
#
#
#
# # sever = smtplib.SMTP(mail_sever,mail_port)
# # sever.set_debuglevel(1)  # 打印出SMTP服务器交互信息
# # sever.login(mail_send,mail_passwd)
# # sever.sendmail(mail_send,[reciver],text_message.as_string())
# # sever.quit()
#
#
# msg = MIMEMultipart()
# msg['From'] = _format_addr("poppy <%s>" % mail_send) # 显示发件人
# msg['to'] = _format_addr("lisa <%s>" % reciver)    # 显示收件人
# msg['subject'] = Header("接口测试报告","utf-8").encode()  # 显示主题
#
# msg.attach(MIMEText("桃之夭夭，灼灼其华", 'plain' ,"utf8"))
#
# with open(r"F:/test_result/精品巩固课.pptx",mode= "rb") as file:
#     mine = MIMEBase("PPT","pptx",filename = "精品巩固课.pptx")
#     mine.add_header('Content-Disposition', 'attachment', filename='精品巩固课.pptx') # 加入头部信息
#
#     mine.set_payload(file.read())
#     encoders.encode_base64(mine)
#
#     msg.attach(mine)
#
# sever = smtplib.SMTP(mail_sever,mail_port)
# sever.set_debuglevel(1)  # 打印出SMTP服务器交互信息
# sever.login(mail_send,mail_passwd)
# sever.sendmail(mail_send,[reciver],msg.as_string())
# sever.quit()

class SendMail():
    def __init__(self):
        global mail_send,mail_passwd,mail_sever,reciver,mail_port
        mail_send = config().get_mail("mail_send")
        mail_passwd = config().get_mail("mail_passwd")
        mail_sever = config().get_mail("mail_sever")
        reciver = config().get_mail("reciver")
        mail_port = config().get_mail("mail_port")
        self.text = None
        self.subtype = None


    def _format_addr(self,value):
        name, addr = parseaddr(value)
        return formataddr((Header(name, "utf8").encode(), addr))


    def choice_subtype(self,subtype=None,text=None):
        if subtype == "plain" and text != None:
            self.text = text
            self.subtype = "plain"
            return self.send_text_mail(),self.subtype,self.text

        elif subtype == "html" and text != None:
            self.text = text
            self.subtype = "html"
            return self.send_html_mail(),self.subtype,self.text

        elif subtype == None and text != None or text == None:
            self.text = text
            return self.send_attach_mail(),self.text


    def send_email(self,message):
        try:
            sever = smtplib.SMTP(mail_sever, mail_port)
            sever.set_debuglevel(1)  # 打印出SMTP服务器交互信息
            sever.login(mail_send, mail_passwd)
            sever.sendmail(mail_send, [reciver], message.as_string())
            sever.quit()
            print("邮件发送成功！")
        except Exception as e:
            Logs().my_log("error","邮件发送失败:" + str(e))
            print("发送邮件失败！")


    def send_text_mail(self):
        text_message = MIMEText(_text = self.text, _subtype = self.subtype, _charset= "utf8")
        text_message['From'] = self._format_addr("<%s>" % mail_send)  # 显示发件人
        text_message['to'] = self._format_addr("<%s>" % reciver)    # 显示收件人
        text_message['subject'] = Header("接口测试报告","utf-8").encode()  # 显示主题
        self.send_email(text_message)


    def send_html_mail(self):
        html_message = MIMEText(_text=self.text, _subtype=self.subtype, _charset="utf8")
        html_message['From'] = self._format_addr("<%s>" % mail_send)
        html_message['to'] = self._format_addr("<%s>" % reciver)
        html_message['subject'] = Header("接口测试报告", "utf-8").encode()
        self.send_email(html_message)


    def send_attach_mail(self):
        msg = MIMEMultipart()
        msg['From'] = self._format_addr("<%s>" % mail_send)
        msg['to'] = self._format_addr("<%s>" % reciver)
        msg['subject'] = Header("接口测试报告","utf-8").encode()

        msg.attach(MIMEText(_text = self.text,_charset = "utf8"))

        with open(config().get_mail("filepath"),mode= "rb") as file:
            mine = MIMEBase("PPT","pptx",filename = "测试课件.pptx")
            mine.add_header('Content-Disposition', 'attachment', filename='测试课件.pptx') # 加入头部信息

            mine.set_payload(file.read())
            encoders.encode_base64(mine)
            msg.attach(mine)

        self.send_email(msg)




if __name__ == '__main__':
    text = "桃之夭夭，灼灼其华,我修改了数据"
    s = SendMail()
    # s.choice_subtype("plain",text)

    # html = "<html><body><p>桃之夭夭，灼灼其华<a href='http://www.baidu.com'>百度一下</a><p><body><html>"
    # s.choice_subtype("html",html)

    s.choice_subtype()



 