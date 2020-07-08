# 모델 불러오기
from tensorflow import Session
from tensorflow import global_variables_initializer
import tensorflow.python.keras
from keras.backend import get_session
from keras.models import load_model

#토크나이저 불러오기
from keras.preprocessing.text import Tokenizer
import numpy as np

from keras_self_attention import SeqSelfAttention
import json
from konlpy.tag import Okt
import kss

session = get_session()
init = global_variables_initializer()
session.run(init)

model = load_model('Project_model3.h5',custom_objects={'SeqSelfAttention':SeqSelfAttention})
token = Tokenizer(5611, oov_token = 'OOV',filters='')
mc = Okt()
load = mc.morphs("로딩중",norm=True, stem=True)
with open('wordIndexOkt.json') as json_file:
    word_index = json.load(json_file)
    token.word_index = word_index

def predict(paragraph):
    with session.as_default():
        with session.graph.as_default():
            emotions = [0,0,0,0,0,0]
            sentences = kss.split_sentences(paragraph)
            import Model
            for sentence in sentences:
                print(sentence)
                output = Model.put(token, sentence, mc) #문장 토크나이즈
                emotion = Model.out(output, model) #토큰화된 문장을 감정으로 출력
                emotions[emotion[0]]=emotions[emotion[0]]+1 #감정에 따라 감정 리스트에 각 감정점수를 플러스
                if emotion == [0]:
                    print("슬픔\n")
                elif emotion == [1]:
                    print("중립\n")
                elif emotion == [2]:
                    print("행복\n")
                elif emotion == [3]:
                    print("불안\n")
                elif emotion == [4]:
                    print("분노\n")
            return emotions

def predictTEST(sentence):
    with session.as_default():
        with session.graph.as_default():
            import Model
            output = Model.put(token, sentence, mc) #문장 토크나이즈
            emotion = Model.out(output, model) #토큰화된 문장을 감정으로 출력
            if emotion == [0]:
                return "슬픔"
            elif emotion == [1]:
                return "중립"
            elif emotion == [2]:
                return "행복"
            elif emotion == [3]:
                return "불안"
            elif emotion == [4]:
                return "분노"
