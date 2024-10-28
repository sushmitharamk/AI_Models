import streamlit as st
import ex
from ex import nnlb

st.title('Your Translator- powered by NLLB-200')
st.header('Enter text to translate: ')

target_langs = {
   'telugu' : 'tel_Telu',
   'hindi' : 'hin_Deva',
   'english' : 'eng_Latn',
   'Mesopotamian Arabic' : 'acm_Arab',
   'Taizzi-Adeni Arabic' : 'acq_Arab',
   'Tunisian Arabic' : 'aeb_Arab',
   'Afrikaans' : 'afr_Latn',
   'South Levantine Arabic' : 'ajp_Arab',
   'Akan' : 'aka_Latn',
   'Amharic' : 'amh_Ethi',
   'North Levantine Arabic' : 'apc_Arab',
   'Modern Standard Arabic' : 'arb_Arab',
   'Modern Standard Arabic (Romanized)' : 'arb_Latn',
   'Najdi Arabic' : 'ars_Arab',
   'Moroccan Arabic' : 'ary_Arab',
   'Egyptian Arabic' : 'arz_Arab',
    'Assamese' : 'asm_Beng',
    'Asturian' : 'ast_Latn',
    'Awadhi' : 'awa_Deva',
    'Central Aymara' : 'ayr_Latn',
    'South Azerbaijani' : 'azb_Arab',
    'North Azerbaijani' : 'azj_Latn',
    'Bashkir' : 'bak_Cyrl',
    'Bambara' : 'bam_Latn',
    'Balinese' : 'ban_Latn',
    'Belarusian' : 'bel_Cyrl',
    'Bemba' : 'bem_Latn',
    'Bengali' : 'ben_Beng',
    'Bhojpuri' : 'bho_Deva',
    'Banjar (Arabic script)' : 'bjn_Arab',
    'Banjar (Latin script)' : 'bjn_Latn',
    'Standard Tibetan' : 'bod_Tibt',
    'Bosnian' : 'bos_Latn',
    'Buginese' : 'bug_Latn',
    'Bulgarian' : 'bul_Cyrl'
}

input_text = st.text_area('write something to translate: ', height=100)
language_option = st.selectbox(
    'How would you like to be contacted?',
    ('Telugu', 'Hindi', 'English','Mesopotamian Arabic','Taizzi-Adeni Arabic',
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