import unittest
from main import CosineSimilarity


class EmptyError(Exception):
    def __init__(self):
        print('The txt is empty')


x = {}
y = open('orig.txt', 'r', encoding='UTF-8')
x['orig.txt'] = y.read()
y.close()
y = open('orig_0.8_add.txt', 'r', encoding='UTF-8')
x['orig_0.8_add.txt'] = y.read()
y.close()
y = open('orig_0.8_del.txt', 'r', encoding='UTF-8')
x['orig_0.8_del.txt'] = y.read()
y.close()
y = open('orig_0.8_dis_1.txt', 'r', encoding='UTF-8')
x['orig_0.8_dis_1.txt'] = y.read()
y.close()
y = open('orig_0.8_dis_3.txt', 'r', encoding='UTF-8')
x['orig_0.8_dis_3.txt'] = y.read()
y.close()
y = open('orig_0.8_dis_7.txt', 'r', encoding='UTF-8')
x['orig_0.8_dis_7.txt'] = y.read()
y.close()
y = open('orig_0.8_dis_10.txt', 'r', encoding='UTF-8')
x['orig_0.8_dis_10.txt'] = y.read()
y.close()
y = open('orig_0.8_dis_15.txt', 'r', encoding='UTF-8')
x['orig_0.8_dis_15.txt'] = y.read()
y.close()
y = open('orig_0.8_mix.txt', 'r', encoding='UTF-8')
x['orig_0.8_mix.txt'] = y.read()
y.close()
y = open('orig_0.8_rep.txt', 'r', encoding='UTF-8')
x['orig_0.8_rep.txt'] = y.read()
y.close()
y = open('none.txt', 'r', encoding='UTF-8')
x['none.txt'] = y.read()
y.close()


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_main():
        for i in x.keys():
            if x[i] != '':
                sim = CosineSimilarity(x['orig.txt'], x[i])
                similarity = sim.main()
                print('样本：%s，查重率为：%.2f' % (i, similarity))
            else:
                raise EmptyError


if __name__ == '__main__':
    unittest.main()
