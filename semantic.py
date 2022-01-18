import spacy
import json
nlp = spacy.load('ru_core_news_lg')
with open('./answers.json') as f:
    answer_types = json.load(f)

'''
по полученному ответу (строке) определяет какая ветка разговора выбрана
'''


def check_answer_type(answer: str):
    answer = nlp(answer)
    distance = 0
    right_key = ""
    for key in answer_types:
        for item in answer_types[key]:
            example = nlp(item)
            #print(answer.similarity(example))
            if answer.similarity(example) > distance:
                distance = answer.similarity(example)
                right_key = key
                if distance == 1.0:
                    return right_key
    return right_key



#check_answer_type('хорошо')
