import spacy
import json
import os

nlp = spacy.load('ru_core_news_lg')
answers_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "answers.json")
with open(answers_path) as f:
    answer_types = json.load(f)

'''
по полученному ответу (строке) определяет какая ветка разговора выбрана
'''
def lemmatization(sentence1: spacy.tokens.doc.Doc, sentence2: spacy.tokens.doc.Doc):
    sentence1 = nlp(" ".join([word.lemma_ for word in sentence1]))
    sentence2 = nlp(" ".join([word.lemma_ for word in sentence2]))
    return sentence1, sentence2

def check_answer_type(answer: str, lemmatizing = False )->str:
    answer = nlp(answer)
    #type(answer) = spacy.tokens.doc.Doc
    distance = 0
    right_key = ""
    for key in answer_types:
        for item in answer_types[key]:
            example = nlp(item)
            if answer.similarity(example) > distance:
                distance = answer.similarity(example)
                right_key = key
                if distance == 1.0:
                    return right_key
            # если включена лемматизация то повторяем процедуру поиска расстояния но с лемматизированными выраженриями
            if lemmatizing == True:
                answer_lem, example_lem = lemmatizing(answer,example)
                if answer_lem.similarity(example_lem) > distance:
                    distance = answer_lem.similarity(answer_lem)
                    right_key = key
                    if distance == 1.0:
                        return right_key
    return right_key

