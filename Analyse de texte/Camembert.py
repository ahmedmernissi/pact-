# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 23:23:55 2021

@author: quent
"""

import pytorch
import pandas as pd
import transformers as tr
from fast_bert.data_lm import BertLMDataBunch
from fast_bert.learner_lm import BertLMLearner
from fast_bert.data import BertDataBunch
from fast_bert import BertLearner
from fast_bert.prediction import BertClassificationPredictor
from pathlib import Path

camembert = pytorch.hub.load('pytorch/fairseq', 'camembert.v0')

DATA_PATH = Path('./data/')
LOG_PATH = Path('./logs')
MODEL_PATH = Path('./model/')
LABEL_PATH = Path('./labels')

df = pd.read_csv('./data/labeled-data.csv',sep = ';',encoding='utf-8', error_bad_lines=False)
val_set = df.sample(frac=0.2, replace=False, random_state=42)
train_set = df.drop(index = val_set.index)
print(len(val_set),"évaluations")
print(len(train_set),"entrainements")
val_set.to_csv('./data/val_set.csv')
train_set.to_csv('./data/train_set.csv')
# labels = df.columns[1:].to_list()
labels=["tristesse","peur","douleur","colère","joie","amour","extase","rire","secret"]
print(labels)
with open('./labels/labels.txt','w') as f:
    for i in labels:
        f.write(i + "\n")
df_texts = pd.read_csv('./data/raw-data.csv',sep = ';',encoding='utf-8', error_bad_lines=False)
all_texts = df_texts['description'].to_list()

print(len(all_texts),"textes")


cuda = pytorch.device('cuda')   
   
databunch_lm = BertLMDataBunch.from_raw_corpus(
    data_dir = DATA_PATH,
    text_list = all_texts,
    tokenizer = 'camembert-base' ,
    batch_size_per_gpu = 16 ,
    max_seq_length = 30,
    multi_gpu = False ,
    model_type = 'camembert-base' ,
    logger = tr.logger )

lm_learner = BertLMLearner.from_pretrained_model(
    dataBunch = databunch_lm ,
    pretrained_path = 'camembert-base',
    output_dir = MODEL_PATH ,
    metrics = [] ,
    device = cuda ,
    logger = tr.logger ,
    multi_gpu = False ,
    fp16_opt_level = "O2")

lm_learner.fit(epochs=30,
                lr=1e-4,
                validate=True,
                schedule_type="warmup_cosine",
                optimizer_type="adamw")


databunch = BertDataBunch(DATA_PATH,LABEL_PATH,
                          tokenizer='camembert-base',
                          train_file='train_set.csv',
                          val_file='val_set.csv',
                          label_file='labels.csv',
                          text_col='description',
                          label_col=['tristesse','peur','douleur','colère','joie','amour','extase','rire','secret'],
                          batch_size_per_gpu=16,
                          max_seq_lenght=512,
                          multi_gpu=False,
                          multi_label=True,
                          model_type='camembert-base')

metrics = [{'name' : 'fbeta', 'function' : tr.fbeta},{'name': 'roc_auc','function': tr.roc_auc}]
OUTPUT_DIR = Path('./finetuned_model')
WGTS_PATH = Path('model/model_out/pytorch_model.bin')

cl_learner = BertLearner.from_pretrained_model(
    databunch,
    pretrained_path='model/model_out',
    metrics=metrics,
    device = cuda,
    logger = tr.logger ,
    output_dir=OUTPUT_DIR,
    finetuned_wgts_path=WGTS_PATH,
    warmup_steps=300,
    multi_gpu=False,
    multi_label=True,
    is_fp16=True,
    logging_steps=50)

predictor = BertClassificationPredictor(
    model_path='finetuned_model/model_out',
    label_path='labels/',
    multi_label=True,
    model_type='camembert-base',
    do_lower_case=False)

predictor.predict("Joie cela fonctionne")
    