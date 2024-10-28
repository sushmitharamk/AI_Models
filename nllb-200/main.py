import streamlit as st
import ex
from ex import nnlb

st.title('Your Translator- powered by NLLB-200')
st.header('Enter text to translate: ')

target_langs = {
   'telugu' : 'tel_Telu',
   'hindi' : 'hin_Deva',
   'english' : 'eng_Latn',
   'mesopotamian arabic' : 'acm_Arab',
   'taizzi-adeni-arabic' : 'acq_Arab',
   'tunisian arabic' : 'aeb_Arab',
   'afrikaans' : 'afr_Latn',
   'south levantine arabic' : 'ajp_Arab',
   'akan' : 'aka_Latn',
   'amharic' : 'amh_Ethi',
   'north levantine arabic' : 'apc_Arab',
   'modern standard arabic' : 'arb_Arab',
   'modern standard arabic (romanized)' : 'arb_Latn',
   'najdi arabic' : 'ars_Arab',
   'moroccan arabic' : 'ary_Arab',
   'egyptian arabic' : 'arz_Arab',
   'assamese' : 'asm_Beng',
   'asturian' : 'ast_Latn',
   'awadhi' : 'awa_Deva',
   'central aymara' : 'ayr_Latn',
   'south azerbaijani' : 'azb_Arab',
   'north azerbaijani' : 'azj_Latn',
   'bashkir' :'bak_Cyrl',
   'bambara' : 'bam_Latn',
   'balinese' : 'ban_Latn',
   'belarusian' : 'bel_Cyrl',
   'bemba' : 'bem_Latn',
   'bengali' : 'ben_Beng',
   'bhojpuri' : 'bho_Deva',
   'banjar (arabic script)' : 'bjn_Arab',
   'banjar (latin script)' : 'bjn_Latn',
   'standard tibetan' : 'bod_Tibt',
   'bosnian' : 'bos_Latn',
   'buginese' : 'bug_Latn',
   'bulgarian' : 'bul_Cyrl'
}

input_text = st.text_area('write something to translate: ', height=100)
language_option = st.selectbox(
    'How would you like to be contacted?',
    ('Telugu', 'Hindi', 'English','Mesopotamian Arabic','Taizzi-Adeni-Arabic',
     'Tunisian Arabic','Afrikaans','South Levantine Arabic', 'Akan','Amharic', 'North Levantine Arabic',
     'Modern Standard Arabic', 'Modern Standard Arabic (Romanized)', 'Najdi Arabic','Moroccan Arabic',
     'Egyptian Arabic', 'Assamese', 'Asturian', 'Awadhi', 'Central Aymara', 'South Azerbaijani', 'North Azerbaijani',
     'Bashkir', 'Bambara','Balinese','Belarusian','Bemba' ,'Bengali' ,'Bhojpuri' ,'Banjar (Arabic script)','Banjar (Latin script)',
     'Standard Tibetan','Bosnian','Buginese','Bulgarian'))
st.write('You selected:', language_option)

if st.button('Translate'):
  with st.spinner('translating....'):
    if language_option.lower() in target_langs.keys():
       translate_to = target_langs[language_option.lower()]
       i_lang = nnlb.predicitions(input_text)
       final_text = nnlb.translations(i_lang, translate_to, input_text)
       st.write(final_text)
       
    else:
       st("please check the output language")