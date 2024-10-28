#import model
import streamlit as st
import fasttext
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from os import path
from huggingface_hub import hf_hub_download

class nnlb:
    #facebook/nllb-200-distilled-600M
#https://huggingface.co/facebook/nllb-200-distilled-600M/resolve/main/pytorch_model.bin
    @st.cache_resource()
    def predicitions(text):
        model_path = hf_hub_download(repo_id="facebook/fasttext-language-identification", filename="model.bin")
        #model_path = hf_hub_download(repo_id="facebook/nllb-200-distilled-600M", filename="pytorch_model.bin")
        predict_model = fasttext.load_model(model_path)
        predictions = predict_model.predict(text, k = 1)
        input_lang = predictions[0][0].replace('__label__','')
        return input_lang

    @st.cache_resource()
    def translations(input_lang,op_lng, text):
        translate_model = AutoModelForSeq2SeqLM.from_pretrained('facebook/nllb-200-distilled-600M')
        tokenizer = AutoTokenizer.from_pretrained('facebook/nllb-200-distilled-600M')
        translator = pipeline('translation', model = translate_model, tokenizer= tokenizer, src_lang = input_lang, tgt_lang = op_lng, max_length = 400)
        out = translator(text)
        translated_text = out[0]['translation_text']
        return translated_text

