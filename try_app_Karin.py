import streamlit as st
from PIL import Image
from gtts import gTTS
from googletrans import Translator
translator = Translator()
from transliterate import translit, get_available_language_codes

st.title("Італійський розмовник для дітей - Итальянский разговорник для детей")

language = st.radio( "Виберіть мову - Выберите язык" , ('Русский', 'Yкраїнський'))

def phrasebook(sentence):
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    st.write(sentence)
  with col2:
    translation = translator.translate(sentence, dest='it')
    translation = translation.text
    st.write(translation)
  with col3:
    tts1=gTTS(translation, lang = 'it')
    tts1.save('your_file.mp3')
    audio_file = open('your_file.mp3', 'rb')
    st.audio(data=audio_file, format="audio/mp3", start_time = 0)
  with col4:
    if language == 'Русский':
      lan = 'ru'
    elif language == 'Yкраїнський':
      lan = 'uk'
    else:
      pass
    result = translit(translation, lan)
    st.write(result)
  

if language == 'Русский':
  placechoice = st.selectbox("Куда ты хочешь пойти сегодня? Bыбери одно из указанных мест:", ('Площадка для игр', 'Школа', 'Магазин'))
  if placechoice == 'Площадка для игр':
    image1 = Image.open('playground.jpg')
    st.image(image1, caption='Photo by Pond Juprasong on Unsplash')
    cola, colb, colc, cold = st.columns(4)
    with cola:
      st.subheader("Полезные выражения")
    with colb:
      st.subheader("Итальянский перевод")
    with colc:
      st.subheader("Вот как это звучит")
    with cold:
      st.subheader("На кириллице")
      
      
    sentence1 = "Пойдем в парк" 
    sentence2 = "Давай играть в прятки"
    sentence3 = "Давай покатаемся на качелях"
    sentence4 = "Пойдем на горки"
    
    phrasebook(sentence1)
    phrasebook(sentence2)
    phrasebook(sentence3)
    phrasebook(sentence4)
    
    #col1, col2, col3, col4 = st.columns(4)
    #with col1:
     # st.header("Русский")
      #st.write(sentence1)
      
    #with col2:
     # st.header("Итальянский")
      #trans(sentence1)
      
    #with col3:
     # aduio(sentence1)
      
    #with col4:  
     # tranllit(sentence3)
 
      
   # with col1:  
    #  st.write(sentence4)
    #with col2:           
     # trans(sentence4)
      
  #if placechoice == 'Школа':
   # image2 = Image.open('school.jpg')
    #st.image(image2, caption='Photo by Kenny Eliason on Unsplash')
    #sentence6 = '
    
  
if language == 'Yкраїнський':
  placechoiceuk = st.selectbox("Куди ти хочеш піти сьогодні? Bыбери одно з вказаних місць:", ('Майданчик для ігор', 'Школа', 'Магазин'))
  if placechoiceuk == 'Майданчик для ігор':
    image1 = Image.open('playground.jpg')
    st.image(image1, caption='Photo by Pond Juprasong on Unsplash')
    sentence1uk = "Підемо в парк"
    sentence2uk = "Давай пограємо в хованки"
    sentence3uk = "Xодімо на гойдалки"
    sentence4uk = "Підемо на гірки"
    
    cola, colb, colc, cold = st.columns(4)
    with cola:
      st.subheader("Корисні вирази")
    with colb:
      st.subheader("Італійський переклад")
    with colc:
      st.subheader("От як це звучить")
    with cold:
      st.subheader("На кирилиці")
    
    phrasebook(sentence1uk)
    phrasebook(sentence2uk)
    phrasebook(sentence3uk)
    phrasebook(sentence4uk)
    
    #col3, col4 = st.columns(2)
    #with col3:
     # st.header("Yкраїнський")
      #st.write(sentence1uk)
    #with col4:
     # st.header("Італійський")
      #trans(sentence1uk)
      
    #with col3:
     # st.write(sentence2uk)
    #with col4:
     # trans(sentence2uk)
      
    #with col3:
     # st.write(sentence3uk)
    #with col4:           
     # trans(sentence3uk)
     
    #with col3:
     # st.write(sentence4uk)
    #with col4:           
     # trans(sentence4uk)
  #if placechoiceuk == 'Школа':
   # image2 = Image.open('school.jpg')
    #st.image(image2, caption='Photo by Kenny Eliason on Unsplash') 
