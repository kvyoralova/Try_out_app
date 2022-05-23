import streamlit as st
from PIL import Image
from gtts import gTTS
from googletrans import Translator
translator = Translator()
#from google.transliteration import transliterate_text
from transliterate import translit, get_available_language_codes

st.title("Італійський розмовник для дітей - Итальянский разговорник для детей")

language = st.radio( "Виберіть мову - Выберите язык" , ('Русский', 'Yкраїнський'))

def trans(sentence):
  translation = translator.translate(sentence, dest='it')
  st.write(translation)
  tts1=gTTS(translation, lang = 'it')
  tts1.save('your_file.mp3')
  audio_file = open('your_file.mp3', 'rb')
  st.audio(data=audio_file, format="audio/mp3", start_time = 0)
  if language == 'Русский':
    lan = 'ru'
  elif language == 'Yкраїнський'
    lan = 'uk'
  result = translit(translation, lan)
  st.write(result)
    

if language == 'Русский':
  placechoice = st.selectbox("Куда ты хочешь пойти сегодня? Bыбери одно из указанных мест:", ('Площадка для игр', 'Школа', 'Магазин'))
  if placechoice == 'Площадка для игр':
    image1 = Image.open('playground.jpg')
    st.image(image1, caption='Photo by Pond Juprasong on Unsplash')
    sentence1 = "Пойдем в парк" 
    sentence2 = "Давай играть в прятки"
    sentence3 = "Давай покатаемся на качелях"
    sentence4 = "Пойдем на горку"
    
    col1, col2 = st.columns(2)
    with col1:
      st.header("Русский")
      st.write(sentence1)
      
    with col2:
      st.header("Итальянский")
      trans(sentence1)
      
    with col1:
      st.write(sentence2)
    with col2:
      trans(sentence2)
      
    with col1:  
      st.write(sentence3)
    with col2:           
      trans(sentence3)
      
    with col1:  
      st.write(sentence4)
    with col2:           
      trans(sentence4)
      
  if placechoice == 'Школа':
    image2 = Image.open('school.jpg')
    st.image(image2, caption='Photo by Kenny Eliason on Unsplash')
    #sentence6 = '
    
  
if language == 'Yкраїнський':
  placechoiceuk = st.selectbox("Куди ти хочеш піти сьогодні? Bыбери одно з вказаних місць:", ('Майданчик для ігор', 'Школа', 'Магазин'))
  if placechoiceuk == 'Майданчик для ігор':
    image1 = Image.open('playground.jpg')
    st.image(image1, caption='Photo by Pond Juprasong on Unsplash')
    sentence1uk = "1. Підемо в парк"
    sentence2uk = "2. Давай пограємо в хованки"
    sentence3uk = "3. Давай покатаємося на гойдалках"
    sentence4uk = "4. Підемо на гірку"
    
    col3, col4 = st.columns(2)
    with col3:
      st.header("Yкраїнський")
      st.write(sentence1uk)
    with col4:
      st.header("Італійський")
      trans(sentence1uk)
      
    with col3:
      st.write(sentence2uk)
    with col4:
      trans(sentence2uk)
      
    with col3:
      st.write(sentence3uk)
    with col4:           
      trans(sentence3uk)
     
    with col3:
      st.write(sentence4uk)
    with col4:           
      trans(sentence4uk)
  if placechoiceuk == 'Школа':
    image2 = Image.open('school.jpg')
    st.image(image2, caption='Photo by Kenny Eliason on Unsplash') 
