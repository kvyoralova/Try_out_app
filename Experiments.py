import streamlit as st
from PIL import Image
from gtts import gTTS
from transliterate import translit, get_available_language_codes

st.title("Итальянский разговорник для детей - Італійський розмовник для дітей")

language = st.radio( "Выберите язык - Виберіть мову" , ('Русский', 'Yкраїнський'))

if language == 'Русский':
  placechoice = st.selectbox("Куда ты хочешь пойти сегодня? Bыбери одно из указанных мест:", ('Площадка для игр', 'Школа', 'Магазин'))
  if placechoice == 'Площадка для игр':
    st.header("Русский")
    text = 'Andiamo a giocare a nascondino'
    st.write(translit(text, 'uk'))
   
