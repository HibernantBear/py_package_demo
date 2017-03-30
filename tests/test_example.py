import unittest  # 导入单元测试模块

from my_package.my_module import MyClass


class UnittestExample(unittest.TestCase):  # 单元测试类，如果测试太多可以使用TestSuite
    def setUp(self):  # 一些测试开始前的准备工作
        self.obj = MyClass()

    def test_example(self):  # 示例测试函数，以test_开头
        self.assertEquals(type(self.obj), MyClass)  # 测试函数，这里的有很多功能不同的函数，以assert开头，详询该父类

    def tearDown(self):  # 一些测试完毕后的处理，比如释放文件对象
        pass

if __name__ == "__main__":  # 照搬就好了
    unittest.main()
