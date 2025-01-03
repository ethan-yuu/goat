import unittest

from goat.unittest.mydict import Dict


class TestDict(unittest.TestCase):

    # 测试方法执行前执行
    def setUp(self):
        print("我要启动了")

    # 测试方法执行后执行
    def tearDown(self):
        print("我结束了")

    # 没有以test开头，不算是测试方法
    def init(self):
        pass

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
        self.assertTrue(issubclass(Dict, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyError(self):
        d = Dict()
        # 期待抛出指定类型的Error
        # 通过d['empty']访问不存在的key时，断言会抛出KeyError
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrError(self):
        d = Dict()
        # 期待抛出指定类型的Error
        # 通过d.empty访问不存在的key时，期待抛出AttributeError
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == '__main__':
    # 运行单元测试
    unittest.main()
