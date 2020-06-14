import pandas as pd
import numpy as np
import re
from keras.preprocessing.sequence import pad_sequences


def put(token, sentence, mc):
    sentence2 = []
    sentence.replace('.', '').replace(',', '').replace('~', '').replace('"', '')
    sentence2 = mc.morphs(sentence)
    print(sentence2)
    if len(sentence2) < 2:
        output = token.texts_to_sequences(sentence)
    else:
        output = token.texts_to_sequences(sentence2)
    output = np.array(output)
    return output


# 결과 변환 함수
def convert(input):
    result = np.argmax(input, axis=1)
    return result


def out(sentence, model):
    # 기본처리
    final = np.array([])

    # try:
    k = 0
    print(sentence)
    for nums in sentence:
        if any(nums) == False:
            continue
        final = np.append(final, nums)
        k = k + 1
        if k == 29:
            break
    if k == 0:
        return [5]

    final2 = np.array([])
    final2 = np.append(final2, final)
    zero = np.zeros((30 - k, 1))
    final2 = np.append(zero, final2)
    final2 = final2.reshape(30, 1)
    result = model.predict(final2.T)
    print(result)
    return convert(result)

# except:
#    return [5]
