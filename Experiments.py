import streamlit as st
from PIL import Image
from gtts import gTTS
from googletrans import Translator
from google.transliteration import transliterate_text
translator = Translator()
#from transliterate import translit, get_available_language_codes


st.title("Італійський розмовник для дітей - Итальянский разговорник для детей")

language = st.radio( "Виберіть мову - Выберите язык" , ('Русский', 'Yкраїнський'))
#translation1 = "Andiamo al parco"
translation2 = "Giochiamo a nascondino"
translation3 = "Andiamo sull'altalena"
translation4 = "Andiamo sullo scivolo"
    

if language == 'Русский':
  placechoice = st.selectbox("Куда ты хочешь пойти сегодня? Bыбери одно из указанных мест:", ('Площадка для игр', 'Школа', 'Магазин'))
  if placechoice == 'Площадка для игр':
    image1 = Image.open('playground.jpg')
    st.image(image1, caption='Photo by Pond Juprasong on Unsplash')
    sentence1 = "1. Пойдем в парк" 
    sentence2 = "2. Давай играть в прятки"
    sentence3 = "3. Давай покатаемся на качелях"
    sentence4 = "4. Пойдем на горку"
    
    col1, col2 = st.columns(2)
    with col1:
      st.header("Русский")
      st.write(sentence1)
      
    with col2:
      st.header("Итальянский")
      
      translation1 = translator.translate(sentence1, dest='it')
      st.write("1. ", translation1)
      #tts1=gTTS(translation1, lang = 'it')
      #tts1.save('your_file.mp3')
      #audio_file = open('your_file.mp3', 'rb')
      #st.audio(data=audio_file, format="audio/mp3", start_time = 0)
      #st.write(translit(textpl1, 'ru')
      result1 = transliterate_text(translation1,  "ru")
      st.write(result1)
      
    with col1:
      st.write(sentence2)
    with col2:
      st.write("2. ", translation2)
      tts1=gTTS(translation2, lang = 'it')
      tts1.save('your_file.mp3')
      audio_file = open('your_file.mp3', 'rb')
      st.audio(data=audio_file, format="audio/mp3", start_time = 0)
      result2 = transliterate_text(translation2,  "ru")
      st.write(result2)
      #st.write(translit(textpl2 'ru')
      
    with col1:  
      st.write(sentence3)
    with col2:           
      st.write("3. ", translation3)
      tts1=gTTS(translation3, lang = 'it')
      tts1.save('your_file.mp3')
      audio_file = open('your_file.mp3', 'rb')
      st.audio(data=audio_file, format="audio/mp3", start_time = 0)
      result3 = transliterate_text(translation3,  "ru")
      st.write(result3)
