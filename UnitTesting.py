import unittest


def add(x,y):

    return x+y




# class MyApp1(unittest.TestCase):
#     def test_case3(self):
#         pass
#     def test_case4(self):
#         pass




class MyApp(unittest.TestCase):

    def test_case1(self):
        a=10
        b=22
        result=add(a,b)
        self.assertEqual(a+b, result)


    def test_case2(self):
        a=12.5
        b=12.9
        result=add(a,b)
        self.assertEqual(a+b, result)

if __name__=="__main__":
    unittest.main()




















# def add(a,b):
#     return a+b
#
# # result = add(2,3)
# result = add(2455252,34456)
# print(result)