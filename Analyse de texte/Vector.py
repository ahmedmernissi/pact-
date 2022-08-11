# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 18:25:38 2021

@author: quent
"""


# IMPORT BDD MODULE
import os
# Condition if we ar in dev branch
if 'BDD' in os.listdir('..'):
    # Import module
    import Library
    # Set imported to True
    BDD = True
else:
    BDD = False
    

# from transformers import CamembertTokenizer , CamembertModel 
# import torch
# # import transformers

# camembert = torch.hub.load('pytorch/fairseq', 'camembert')
# # tokenizer = CamembertTokenizer.from_pretrained('camembert-base')
# # model = CamembertModel.from_pretrained('camembert-base')

# phrase = "Berlin est vraiment une belle ville. Elle a vraiment réussit la où les autres ont <mask>"


# ##############################################################################



# def givectormodel(phrase) :
#     inputs = tokenizer(phrase, return_tensors="pt")
#     outputs = model(**inputs)
#     long = outputs[0][0].size()[0]
#     return(outputs[0][0][1:long-1])

# def givectoreseau(phrase) :
#     tokens = camembert.encode(phrase)
#     all_layers = camembert.extract_features(tokens, return_all_hiddens=True)
#     embeddings = all_layers[0]
#     long = embeddings[0].size()[0]
#     return(embeddings[0][1:long-1])

# def giveid(phrase) :
#     token_ids = tokenizer.encode(phrase)
#     tokens = [tokenizer._convert_id_to_token(idx) for idx in token_ids]
#     print(tokens)
    
#     token_ids = torch.tensor(token_ids).unsqueeze(0)
#     print(token_ids)
    
#     output = model(token_ids)[0].squeeze()
#     cls_out = output[0]
#     print(cls_out.size())
    
# def fillmask(phrase) :
#     if "<mask>" in phrase :
#         return(camembert.fill_mask(phrase, topk=3))
#     else : return("There is no <mask>")
    
##############################################################################

# from transformers import CamembertTokenizer, CamembertForSequenceClassification
# import torch

# tokenizer = CamembertTokenizer.from_pretrained('camembert-base')
# model = CamembertForSequenceClassification.from_pretrained('camembert-base')

# inputs = tokenizer("Mon chien est trop mignon", return_tensors="pt")
# labels = torch.tensor([1]).unsqueeze(0)  # Batch size 1
# outputs = model(**inputs, labels=labels)
# print(outputs[1])
# # loss = outputs.loss
# # logits = outputs.logits

##############################################################################
# from transformers import pipeline

# classifier = pipeline('sentiment-analysis')
# print(classifier('I like this'))

##############################################################################
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer


def posneg(text):
    rate=TextBlob(text,pos_tagger=PatternTagger(),analyzer=PatternAnalyzer()).sentiment[0]
    return(rate)

list_ambiance = ["Distant Thunder","Gregorian Voices","Irish Coast","Summer Night","Waterfall","African Town","Medieval Village","Autumn Walk","Cafe Restaurant","Primeval Forest"]

if BDD:
    works = Library.getAllWork()
    for work in works:
        val = int(posneg(work.txt)*10)
        script = work.getScript()
        script.nameSoundAtmosphere = list_ambiance[val]
        print("[*] Sound Ambiance is :", script.nameSoundAtmosphere,
            " for image ", work.title)
        script.push()
    