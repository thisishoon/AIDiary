import pandas as pd
import numpy as np
import re
from keras.preprocessing.sequence import pad_sequences


def put(token, sentence, mc):
    stopwords = ['의', '가', '이', '은', '들', '는', '걍', '과', '도', '를', '으로', '에', '와', '하다']
    sentence2 = []
    sentence = re.sub('\.|\,|\~|\"|\ㅜ|\ㅠ|\ㅎ|\ㅋ|\ㅡ', '', sentence)
    sentence2 = mc.morphs(sentence)
    sentence2 = [word for word in sentence2 if not word in stopwords]
    print(sentence2)
    '''
    if len(sentence2)<2:
        output= token.texts_to_sequences(sentence)
    else:
    '''
    output = token.texts_to_sequences(sentence2)
    print(output)
    return output


# 결과 변환 함수
def convert(input):
    result = np.argmax(input, axis=1)
    return result


def out(sentence, model):
    # 기본처리
    final = np.array([])
    k = 0

    # sentence의 원소를 체크합니다.
    for nums in sentence:
        final = np.append(final, nums)  # 토큰에 있는 단어면 추가합니다.
        k = k + 1  # 추가된 단어의 개수입니다.
    if k == 0:
        return [5]  # 모든 단어가 토큰 리스트에 없는 단어이거나, 길이가 0인 문장이면 "예외"를 출력합니다.
    final2 = np.array([])
    final2 = np.append(final2, final)
    zero = np.zeros((30 - k, 1))
    final2 = np.append(zero, final2)  # padding과 유사한 효과입니다.
    final2 = final2.reshape(30, 1)  # 길이 30의 문장을 만들기 위해 reshape 합니다.
    print(final2.T)
    result = model.predict(final2.T)
    return convert(result)
