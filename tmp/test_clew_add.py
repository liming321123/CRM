import unittest

from data.read_data import read_excel
from testcase.base_testcase import BaseTestCase
from tmp.clew_page import ClewPage
from page.login_page import LoginPage

class ClewAddTestCase(BaseTestCase):
    def test_clew_add(self):
        lp = LoginPage(self.driver )#实例化登录page的LoginPage类
        lst_user = read_excel(r"D:\workspace\webAutoCRM\data\user.xlsx","user")#读取数据
        result = lp.login(lst_user[0][0], lst_user[0][1])#调用登录login方法
        self.assertIn(lst_user[0][0], result)

        cp = ClewPage(self.driver)#实例化ClewPage类
        cp.clew_add('zls')#调用新增线索clew_addd时需要传一个参数

if __name__ == '__main__':
    unittest.main()
