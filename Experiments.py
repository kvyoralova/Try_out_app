import streamlit as st
from PIL import Image
from gtts import gTTS
from google.transliteration import transliterate_text

st.title("Итальянский разговорник для детей - Італійський розмовник для дітей")

language = st.radio( "Выберите язык - Виберіть мову" , ('Русский', 'Yкраїнський'))

if language == 'Русский':
  placechoice = st.selectbox("Куда ты хочешь пойти сегодня? Bыбери одно из указанных мест:", ('Площадка для игр', 'Школа', 'Магазин'))
  if placechoice == 'Площадка для игр':
    st.header("Русский")
    st.write(pd.DataFrame({'first column': ["1. Пойдем в парк", "2. Давай играть в прятки", "3. Давай покатаемся на качелях"],'second column': ["Andiamo al parco", "Giochiamo a nascondino", "Andiamo sull'altalena"]})
