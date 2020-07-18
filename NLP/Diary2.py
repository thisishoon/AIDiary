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
from NLP.Model import *

session = get_session()
init = global_variables_initializer()
session.run(init)

model1 = load_model('NLP/Project_model_Ens1_.h5',custom_objects={'SeqSelfAttention':SeqSelfAttention})
model2 = load_model('NLP/Project_model_Ens2_.h5',custom_objects={'SeqSelfAttention':SeqSelfAttention})
model3 = load_model('NLP/Project_model_Ens3_.h5',custom_objects={'SeqSelfAttention':SeqSelfAttention})
model4 = load_model('NLP/Project_model_Ens4_.h5',custom_objects={'SeqSelfAttention':SeqSelfAttention})
model5 = load_model('NLP/Project_model_Ens5_.h5',custom_objects={'SeqSelfAttention':SeqSelfAttention})

token = Tokenizer(5658, oov_token = 'OOV',filters='')
mc = Okt()
load = mc.morphs("로딩중",norm=True, stem=True)

with open('NLP/wordIndexOktNum.json') as json_file:
    word_index = json.load(json_file)
    token.word_index = word_index

def predict(paragraph):
    with session.as_default():
        with session.graph.as_default():
            emotions = [0,0,0,0,0,0]
            sentences = kss.split_sentences(paragraph)
            for sentence in sentences:
                output = put(token, sentence, mc) #문장 토크나이즈
                emotion = out(output, model1, model2, model3, model4, model5) #토큰화된 문장을 감정으로 출력
                emotions[emotion[0]]=emotions[emotion[0]]+1 #감정에 따라 감정 리스트에 각 감정점수를 플러스
            return emotions
