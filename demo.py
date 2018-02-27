#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@description:测试程序
"""
from evaluator import Evaluator


def demo_dict():
    """
    test classifier based on sentiment dict
    :return: 
    """
    from classifier.dict import DictClassifier
    dc = DictClassifier()
    # test single sentence
    sentence = input('please enter a sentence:  ')
    result = dc.analyse_sentence(sentence, "data/out/demo_result.out", True)
    print("result: ", result)


def demo_movie():
    from corpus import MovieCorpus
    name = "movie"
    # total :2000
    train_num = 800
    test_num = 200
    feature_num = 500
    max_iter = 100
    C = 80
    k = [1, 3, 5, 7, 9]
    corpus = MovieCorpus()
    evalutor = Evaluator(name, train_num, test_num, feature_num, max_iter, C, k, corpus)
    evalutor.test_knn()


def demo_hotel():
    from corpus import HotelCorpus

    name = "hotel"
    train_num = 2200
    test_num = 800
    feature_num = 5000
    max_iter = 500
    C = 150
    # k = 13
    k = [1, 3, 5, 7, 9, 11, 13]
    corpus = HotelCorpus()
    evaluator = Evaluator(name, train_num, test_num, feature_num, max_iter, C, k, corpus)

    # evaluator.test_knn()
    evaluator.test_bayes()


def demo_waimai():
    from corpus import WaimaiCorpus

    type_ = "waimai"
    train_num = 3000
    test_num = 1000
    feature_num = 5000
    max_iter = 500
    C = 150
    k = 13
    k = [1, 3, 5, 7, 9, 11, 13]
    corpus = WaimaiCorpus()

    test = Evaluator(type_, train_num, test_num, feature_num, max_iter, C, k, corpus)
    test.test_bayes()
    # test.test_maxent()
    test.test_svm()


#############################################
demo_movie()
# demo_dict()
#demo_waimai()
#############################################
