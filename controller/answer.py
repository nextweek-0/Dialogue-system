import db.qa as qa
import jieba
from gensim.models import KeyedVectors
import numpy as np
from controller import pachong

# 交集
def Set_List(docs_list):
    nums = len(docs_list)
    try:
        # 交集列表
        set_list = docs_list[0]
        for i in range(nums - 1):
            set_list = list(set(set_list) & set(docs_list[i + 1]))
    except:
        set_list = []
    return set_list


# BM25
def BM25(question_answer_list):
    pass

def wv():
    file = 'D:/PycharmProjects/QA/static/100000-small.txt'
    wv_from_text = KeyedVectors.load_word2vec_format(file,binary=False)
    wv_from_text.init_sims(replace=True)
    return wv_from_text

def Best_answer(wv_from_text,question_answer_list,user_question):

    # 用户问题的向量
    user_vector = np.zeros(200)
    for word in jieba.lcut(user_question):
        try:
            user_vector += np.array(wv_from_text[word])
        except:
            continue
    # 挑选出的问题的向量列表
    questions_vector_list = []
    for i,q_a in enumerate(question_answer_list):
        words_list = jieba.lcut(q_a[0])
        vector  = np.zeros(200)
        for word in words_list:
            try:
                vector += np.array(wv_from_text[word])
            except:
                continue
        questions_vector_list.append(vector)
    # 挑选出最相似的
    smaller = float('inf')
    min_num = 0
    for i,vector in enumerate(questions_vector_list):
        dist = np.linalg.norm(user_vector - vector)
        if dist < smaller:
            smaller = dist
            min_num = i
    return question_answer_list[min_num][1]

# 得到最有可能的10个句子
def top_10(question):
    words_list = jieba.lcut(question)
    docs_list = []
    # 取出出现过这些词语的交集
    for word in words_list:
        try:
            docs = qa.get_docs(word)
            docs = docs[0][0][1:-1].split(',')
            docs_list.append(docs)
        except:
            continue
    set_list = Set_List(docs_list)
    # 如果空集，单词少一个
    if len(set_list) < 10:
        for j in range(len(docs_list)):
            docs_list_1 = [i for i in docs_list if i != docs_list[j]]
            set_list += Set_List(docs_list_1)
            # print(set_list)
    if len(set_list) >= 10:
        return set_list[:10]
    else:
        return set_list


def answer(user_question,wv_from_text):
    question_answer_list = []
    for id in top_10(user_question):
        id = id.replace(' ','')
        id = int(id)
        question_answer = qa.search_question_answer(id)[0]
        question_answer_list.append(question_answer)
    best_answer = Best_answer(wv_from_text,question_answer_list,user_question)
    return best_answer
    return question_answer_list


