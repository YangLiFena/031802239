# -*- coding: utf-8 -*-
# 思路：1、分词；2、列出所有词；3、分词编码；4、词频向量化；5、套用余弦函数计量两个句子的相似度。
#用于命令行参数读入
import sys
# 用于分词
import jieba
# 用于关键词的抽取,使用默认的TF-IDF模型对文档进行分析
import jieba.analyse
# 余弦相似度计算
from sklearn.metrics.pairwise import cosine_similarity


# 空文本异常
class EmptyError(Exception):
    def __init__(self):
        print('The txt is empty')
        

class CosineSimilarity(object):

    def __init__(self, content_y1, content_y2):
        self.s1 = content_y1
        self.s2 = content_y2

    @staticmethod
    def extract_keyword(text):  # 提取关键词
        # 切割，此处是否进行切割查重结果会发生变化
        seg = jieba.lcut(text, cut_all=True)  # 全模式分词
        # print(seg)
        # 提取关键词,抽取200个关键词，withWeight=False：不设置权重
        keywords = jieba.analyse.extract_tags("/".join(seg), topK=200, withWeight=False)
        return keywords

    @staticmethod
    def one_hot(dictionary, keywords):  # oneHot编码函数
        word_frequency = [0] * len(dictionary)
        for word in keywords:
            word_frequency[dictionary[word]] += 1  #计算词频，生成词频向量
        return word_frequency

    def main(self):
        # 提取关键词，生成两个关键词集
        keywords1 = self.extract_keyword(self.s1)
        keywords2 = self.extract_keyword(self.s2)
        # 使用set函数创建集合并进行词的并集
        union_set = set(keywords1).union(set(keywords2))
        # 字典编码
        word_dict = {}
        i = 0
        for word in union_set:
            word_dict[word] = i
            i += 1

        s1_oh_code = self.one_hot(word_dict, keywords1)  # one_hot编码
        s2_oh_code = self.one_hot(word_dict, keywords2)
        array = [s1_oh_code, s2_oh_code]
        try:
            sim = cosine_similarity(array)  # x相似度计算，输出结果为一2*2矩阵
        # print(sim)
            return sim[1][0]  # sim[0][1]也可
        except Exception as e:  # 捕获所有错误类型
            print(e.args)  # 打印异常到屏幕
            return 0.0


# 测试
if __name__ == '__main__':
    x1 = open(sys.argv[1], 'r', encoding='UTF-8')
    content_x1 = x1.read()
    x1.close()
    x2 = open(sys.argv[2], 'r', encoding='UTF-8')
    content_x2 = x2.read()
    if content_x2 == '':
        # 文本为空，抛出异常
        raise EmptyError
    x2.close()
    cos_similarity = CosineSimilarity(content_x1, content_x2)
    similarity = cos_similarity.main()
    ans_txt = open(sys.argv[3], 'w', encoding='UTF-8')
    # answer = str('%.2f' % similarity)
    ans_txt.write('%.2f' % similarity)
    ans_txt.close()
    print('查重率为:%.2f' % similarity)
