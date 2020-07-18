
import pandas as pd
import numpy as np
import re
from keras.preprocessing.sequence import pad_sequences

def put(token, sentence, mc):
        stopwords = ['의','가','이','은','들','는','과','도','를','으로','에','와']
        sware = ['ㅈ', '좇', '좃', '젓']
        sentence2 = []
        sentence = re.sub('\.|\,|\~|\"|\=|\<|\>|\*|\'', '', sentence)
        sentence = re.sub("\n", '', sentence)
        sentence = re.sub('[0-9]', '', sentence)
        #sentence = re.sub('[a-zA-Z]', '', sentence)
        sentence2 = mc.morphs(sentence,norm=True, stem=True)
        #print(sentence2)
        for word in sentence2:
                if word in sware:
                        sentence2[sentence2.index(word)] = '좆'
        sentence2 = [word for word in sentence2 if not word in stopwords]
        output= token.texts_to_sequences(sentence2)
        return output

# 결과 변환 함수
def convert(input):
        tot = [0,0,0,0,0]
        for emotion in input:
                tot = emotion+tot
        result = np.argmax(tot, axis=1)
        return result

def out(sentence, m1,m2,m3,m4,m5) :
     #기본처리
        final=np.array([])
        k=0
        #sentence의 원소를 체크합니다.
        for nums in sentence:
                if k==30:
                    break
                final=np.append(final,nums) # 토큰에 있는 단어면 추가합니다.
                k=k+1 # 추가된 단어의 개수입니다.
        if k == 0 :
                return [5] #모든 단어가 토큰 리스트에 없는 단어이거나, 길이가 0인 문장이면 "예외"를 출력합니다.
        final2=np.array([])
        final2=np.append(final2,final)
        
        if k!=30:
                zero = np.zeros((30-k, 1)) 
                final2 = np.append(zero, final2) #padding과 유사한 효과입니다.
                
        final2=final2.reshape(30,1) # 길이 30의 문장을 만들기 위해 reshape 합니다.
        
        result = [m1.predict(final2.T),m2.predict(final2.T),m3.predict(final2.T),m4.predict(final2.T),m5.predict(final2.T)]
        return convert(result)
