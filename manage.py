#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from konlpy.tag import Komoran
from keras_self_attention import SeqSelfAttention
from keras.preprocessing.text import Tokenizer
from keras.models import load_model
import json




def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AIDiary.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # model = load_model('Project_model.h5', custom_objects={'SeqSelfAttention': SeqSelfAttention})
    # token = Tokenizer(9482)
    # mc = Komoran()
    # with open('wordIndex.json') as json_file:
    #     word_index = json.load(json_file)
    #     token.word_index = word_index
    main()
