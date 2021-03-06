# -*- coding: utf-8 -*-
# 思路：1、分词；2、列出所有词；3、分词编码；4、词频向量化；5、套用余弦函数计量两个句子的相似度。
# from memory_profiler import profile
# import line_profiler
# import sys
import jieba
import jieba.analyse
# import profile
# 机器学习包
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
    # @profile
    def extract_keyword(content):  # 提取关键词
        # 切割
        seg = jieba.lcut(content, cut_all=True)  # 全模式分词
        # print(seg)
        # 提取关键词
        keywords = jieba.analyse.extract_tags("/".join(seg), topK=200, withWeight=False)
        return keywords

    @staticmethod
    # @profile
    def one_hot(word_dict, keywords):  # oneHot编码函数
        # cut_code = [word_dict[word] for word in keywords]
        cut_code = [0] * len(word_dict)
        for word in keywords:
            cut_code[word_dict[word]] += 1
        return cut_code

    # @profile
    def main(self):
        # 提取关键词
        keywords1 = self.extract_keyword(self.s1)
        keywords2 = self.extract_keyword(self.s2)
        # 使用set函数创建集合并进行词的并集
        union = set(keywords1).union(set(keywords2))
        # 字典编码
        word_dict = {}
        i = 0
        for word in union:
            word_dict[word] = i
            i += 1

        s1_cut_code = self.one_hot(word_dict, keywords1)  # one_hot编码
        s2_cut_code = self.one_hot(word_dict, keywords2)
        sample = [s1_cut_code, s2_cut_code]  # 余弦相似度计算
        # 除零处理
        try:
            sim = cosine_similarity(sample)  # 输出结果为一2*2矩阵
            # print(sim)
            return sim[1][0]  # sim[0][1]也可
        except Exception as e:  # 捕获所有错误类型
            print(str(e))  # 打印异常到屏幕
            return 0.0


# 测试
if __name__ == '__main__':
    x1 = open('orig.txt', 'r', encoding='UTF-8')
    content_x1 = x1.read()
    x1.close()
    x2 = open('orig_0.8_dis_1.txt', 'r', encoding='UTF-8')
    content_x2 = x2.read()
    if content_x2 == '':
        # 文本为空，抛出异常
        raise EmptyError
    x2.close()
    similarity = CosineSimilarity(content_x1, content_x2)
    similarity = similarity.main()
    print('%.2f' % similarity)
    # ans_txt = open(sys.argv[3], 'w', encoding='UTF-8')
    # answer = str('%.2f' % similarity)
    # ans_txt.write(answer)
    # ans_txt.close()
    # profile.run('main()')
