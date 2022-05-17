import streamlit as st
from PIL import Image
from gtts import gTTS
from google.transliteration import transliterate_text
#from transliterate import translit, get_available_language_codes


st.title("Итальянский разговорник для детей - Італійський розмовник для дітей")

language = st.radio( "Выберите язык - Виберіть мову" , ('Русский', 'Yкраїнський'))

if language == 'Русский':
  placechoice = st.selectbox("Куда ты хочешь пойти сегодня? Bыбери одно из указанных мест:", ('Площадка для игр', 'Школа', 'Магазин'))
  if placechoice == 'Площадка для игр':
    image1 = Image.open('playground.jpg')
    st.image(image1, caption='Photo by Pond Juprasong on Unsplash')
    sentence1 = "1. Пойдем в парк" 
    sentence2 = "2. Давай играть в прятки"
    sentence3 = "3. Давай покатаемся на качелях"
    col1, col2 = st.columns(2)
    with col1:
      st.header("Русский")
      st.write(sentence1)
      
    with col2:
      st.header("Итальянский")
      textpl1 = "Andiamo al parco"
      st.write(" 1.", textpl1, )
      tts1=gTTS(textpl1, lang = 'it')
      tts1.save('your_file.mp3')
      audio_file = open('your_file.mp3', 'rb')
      st.audio(data=audio_file, format="audio/mp3", start_time = 0)
      #st.write(translit(textpl1, 'ru')
      result1 = transliterate_text(textpl1,  "ru")
      st.write(result1)
      
    with col1:
      st.write(sentence2)
    with col2:
      textpl2 = "Giochiamo a nascondino"
      st.write("2. ", textpl2)
      tts1=gTTS(textpl2, lang = 'it')
      tts1.save('your_file.mp3')
      audio_file = open('your_file.mp3', 'rb')
      st.audio(data=audio_file, format="audio/mp3", start_time = 0)
      result2 = transliterate_text(textpl2,  "ru")
      st.write(result2)
      #st.write(translit(textpl2 'ru')
      
    with col1:  
      st.write(sentence3)
    with col2:           
      textpl3 = "Andiamo sull'altalena"
      st.write("3.", textpl3)
      tts1=gTTS(textpl3, lang = 'it')
      tts1.save('your_file.mp3')
      audio_file = open('your_file.mp3', 'rb')
      st.audio(data=audio_file, format="audio/mp3", start_time = 0)
      result3 = transliterate_text(textpl3,  "ru")
      st.write(result3)
  
if language == 'Yкраїнський':
  placecoicheuk = st.selectbox("Куди ти хочеш піти сьогодні? Bыбери одно з вказаних місць:", ('Майданчик для ігор', 'Школа', 'Магазин'))
  if placecoicheuk == 'Майданчик для ігор':
    image1 = Image.open('playground.jpg')
    st.image(image1, caption='Photo by Pond Juprasong on Unsplash')
    st.write("1. Давайте пограємо в хованки")
  
    
