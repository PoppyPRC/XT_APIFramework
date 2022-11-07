from public.send_method import SendMethod
from public.read_excel import ExcelData
from public.login_token import login
from public.Log import Logs
import unittest,sys
from ddt import ddt,data
import jsonpath,json

method = SendMethod()
test_data = ExcelData("test_case.xlsx","Sheet1").read_excel()


@ddt
class TestAddTopic(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        header = {'Authorization':login(),"Content-Type":"application/json"}
        method.get_header(header)


    def setUp(self) -> None:
        pass



    @data(*test_data)
    def test_add_topic(self,data):
            Logs().my_log("info","-"*60 + sys._getframe().f_code.co_name + "-"*60)
            method.get_url("/api/topicWarehouse/personalManage/add")
            value = json.loads(data["param"])
            method.get_data(value)
            response = method.post_with_json()
            status_code = jsonpath.jsonpath(response, "$..status_code")[0]
            if status_code != 200:
                Logs().my_log("info", jsonpath.jsonpath(response, "$..message")[0])
            else:
                pass
            self.assertEqual(status_code,int(data["stauts_code"]))


    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass




if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAddTopic))
    unittest.TextTestRunner(verbosity= 2).run(suite)