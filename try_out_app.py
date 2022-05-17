import streamlit as st
from PIL import Image
from gtts import gTTS


st.title("Итальянский разговорник для детей - Італійський розмовник для дітей")

language = st.radio( "Выберите язык - Виберіть мову" , ('Русский', 'Yкраїнський'))

if language == 'Русский':
  placechoice = st.selectbox("Куда ты хочешь пойти сегодня? Bыбери одно из указанных мест:", ('Площадка для игр', 'Школа', 'Магазин'))
  if placechoice == 'Площадка для игр':
    image1 = Image.open('playground.jpg')
    st.image(image1, caption='Photo by Pond Juprasong on Unsplash')
    col1, col2 = st.columns(2)
    with col1:
      st.header("Русский")
      st.write("1. Пойдем в парк")
      
    with col2:
      st.header("Итальянский")
      text1 = "Andiamo al parco"
      st.write(text1)
      tts1=gTTS(text1, lang = 'it')
      tts1.save('your_file.mp3')
      audio_file = open('your_file.mp3', 'rb')
      st.audio(data=audio_file, format="audio/mp3", start_time = 0)
      
    with col1:
      st.write("2. Давай играть в прятки")
    with col2:
      st.write("2. Giochiamo a nascondino")
      text2 = "Giochiamo a nascondino"
      tts1=gTTS(text2, lang = 'it')
      tts1.save('your_file.mp3')
      audio_file = open('your_file.mp3', 'rb')
      st.audio(data=audio_file, format="audio/mp3", start_time = 0)
      
    with col1:  
      st.write("3. Давай покатаемся на качелях")
    with col2:           
      st.write("3. Andiamo sull'altalena")
      text3 = "Andiamo sull'altalena"
      tts1=gTTS(text3, lang = 'it')
      tts1.save('your_file.mp3')
      audio_file = open('your_file.mp3', 'rb')
      st.audio(data=audio_file, format="audio/mp3", start_time = 0)
  
if language == 'Yкраїнський':
  placecoicheuk = st.selectbox("Куди ти хочеш піти сьогодні? Bыбери одно з вказаних місць:", ('Майданчик для ігор', 'Школа', 'Магазин'))
  if placecoicheuk == 'Майданчик для ігор':
    image1 = Image.open('playground.jpg')
    st.image(image1, caption='Photo by Pond Juprasong on Unsplash')
    st.write("1. Давайте пограємо в хованки")
  
    
