import pytest


class TestClass:
    workage2 = 5
    workage3 = 10
    # def setUpModule(self):
    #     print('test_pytest执行前')
    #
    # def tearDownModule(self):
    #     print('test_pytest执行后')
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print('类方法执行前')
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print('类方法执行后')

    def setUp(self):
        print('测试方法执行前执行')

    def tearDown(self):
        print('测试方法执行后执行')


    # Case上采用@pytest.mark. + 分组名称，就相当于该方法被划分为该分组中
    # 一个分组可以有多个方法，一个方法也可以被划分到多个分组中
    @pytest.mark.user_manage
    def test_case1(self):
        print('testcase1')

    @pytest.mark.user_managa
    def test_case2(self):
        print('testcase2')

    @pytest.mark.user_managa
    @pytest.mark.user_manage
    def test_case3(self):
        print('testcase3')

    @pytest.mark.skip(reason='跳过')
    def test_case4(self):
        print('testcase4')

    @pytest.mark.skipif(workage2<10,reason="222")
    def test_case5(self):
        print('是否被执行')

    @pytest.mark.skipif(workage3<10,reason="111")
    def test_case6(self):
        print('是否被执行1')

    @pytest.mark.skipif(workage3<workage2,reason="111")
    def test_case7(self):
        print('是否被执行2')


class TestClass2:
    def test_case8(self):
        print('是否被执行2')


if __name__ == '__main__':
    pytest.main(['-v', 'InterfaceAutomation/test_pytest.py::TestClass2::test_case8'])