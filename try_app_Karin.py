import streamlit as st
from PIL import Image
from gtts import gTTS
from googletrans import Translator
translator = Translator()
from transliterate import translit, get_available_language_codes

st.title("Італійський розмовник для дітей - Итальянский разговорник для детей")
st.write(""" -  UK: Цей додаток має на меті допомогти українським дітям, як російською, так і українською мовою, вивчити та використовувати деякі корисні фрази італійською""") 
st.write(""" -  RU: Это приложение нацелено на то, чтобы помочь украинским и русскоязычным детям выучить и использовать некоторые полезные фразы на итальянском языке""")

language = st.radio( "Виберіть мову - Выберите язык" , ('Русский', 'Yкраїнський'))
translation2 = "Giochiamo a nascondino"
translation3 = "Andiamo sull'altalena"
translation4 = "Andiamo sullo scivolo"
translation5 = "Saltiamo la corda"
translation6 = "Dopo giochiamo insieme?"
translation7 = "Facciamo un puzzle"
translation8 = "Disegnamo?"
translation9 = "Andiamo in giardino?"
translation10 = "Mi presti il tuo pennarello?"
translation11 = "Buongiorno"
translation12 = "Mi servirebbero dei quaderni"
translation13 = "Avrei bisogno di un righello"
translation14 = "Mi servirebbero le matite colorate"
translation15 = "Avrei bisogno di un astuccio"

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
    
def phrasebooknotranslation (sentence, translation):
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    st.write(sentence)
  with col2:
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
  placechoice = st.selectbox("Куда ты хочешь пойти сегодня? Bыбери одно из указанных мест:", ('Площадка для игр', 'Школа', 'Магазин канцтоваров'))
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
    sentence4 = "Пойдем на горку"
    sentence5 = "Давайте прыгать на скакалке"
    
    phrasebook(sentence1)
    phrasebook(sentence2)
    phrasebooknotranslation(sentence3, translation3)
    phrasebooknotranslation(sentence4, translation4)
    phrasebooknotranslation(sentence5, translation5)
      
  if placechoice == 'Школа':
    image2 = Image.open('school.jpg')
    st.image(image2, caption='Photo by Kenny Eliason on Unsplash')
    cola, colb, colc, cold = st.columns(4)
    with cola:
      st.subheader("Полезные выражения")
    with colb:
      st.subheader("Итальянский перевод")
    with colc:
      st.subheader("Вот как это звучит")
    with cold:
      st.subheader("На кириллице")
    sentence6 = "Потом поиграем вместе?"
    sentence7 = "Давай сделаем пазл"
    sentence8 = "Давай рисовать"
    sentence9 = "Пойдём в сад?"
    sentence10 = "Могу ли я взять твой фломастер?"
    
    phrasebook(sentence6)
    phrasebook(sentence7)
    phrasebook(sentence8)
    phrasebook(sentence9)
    phrasebooknotranslation(sentence10, translation10)
    
  if placechoice == 'Магазин канцтоваров':
    image3 = Image.open('stationary_shop.jpg')
    st.image(image3, caption='Photo by @candelarms on Unsplash')
    cola, colb, colc, cold = st.columns(4)
    with cola:
      st.subheader("Полезные выражения")
    with colb:
      st.subheader("Итальянский перевод")
    with colc:
      st.subheader("Вот как это звучит")
    with cold:
      st.subheader("На кириллице")
    sentence11 = "Добрый день"
    sentence12 = "Мне нужны тетради"
    sentence13 = "Мне нужна линейка"
    sentence14 = "Мне нужны цветные карандаши"
    sentence15 = "Мне нужен пенал"
    
    phrasebooknotranslation(sentence11, translation11)
    phrasebook(sentence12)
    phrasebooknotranslation(sentence13, translation13)
    phrasebook(sentence14)
    phrasebooknotranslation(sentence15, translation15)
  
if language == 'Yкраїнський':
  placechoiceuk = st.selectbox("Куди ти хочеш піти сьогодні? Bыбери одно з вказаних місць:", ('Майданчик для ігор', 'Школа', 'Магазин канцтоварів'))
  if placechoiceuk == 'Майданчик для ігор':
    image1 = Image.open('playground.jpg')
    st.image(image1, caption='Photo by Pond Juprasong on Unsplash')
    cola, colb, colc, cold = st.columns(4)
    with cola:
      st.subheader("Корисні вирази")
    with colb:
      st.subheader("Італійський переклад")
    with colc:
      st.subheader("От як це звучить")
    with cold:
      st.subheader("На кирилиці")
      
    sentence1uk = "Підемо в парк"
    sentence2uk = "Давай пограємо в хованки"
    sentence3uk = "Xодімо на гойдалки"
    sentence4uk = "Підемо на гірку"
    sentence5uk = "Давайте стрибати на скакалці"
    
    
    phrasebook(sentence1uk)
    phrasebook(sentence2uk)
    phrasebooknotranslation(sentence3uk, translation3)
    phrasebooknotranslation(sentence4uk, translation4)
    phrasebooknotranslation(sentence5uk, translation5)

  if placechoiceuk == 'Школа':
    image2 = Image.open('school.jpg')
    st.image(image2, caption='Photo by Kenny Eliason on Unsplash') 
    cola, colb, colc, cold = st.columns(4)
    with cola:
      st.subheader("Корисні вирази")
    with colb:
      st.subheader("Італійський переклад")
    with colc:
      st.subheader("От як це звучить")
    with cold:
      st.subheader("На кирилиці")
    
    sentence6uk = "Потім пограємось разом?"
    sentence7uk = "Давай зробимо пазл"
    sentence8uk = "Давай малювати"
    sentence9uk = "Підемо в сад?"
    sentence10uk = "Чи можу я узяти твій фломастер?"
    
    phrasebook(sentence6uk)
    phrasebook(sentence7uk)
    phrasebook(sentence8uk)
    phrasebook(sentence9uk)
    phrasebooknotranslation(sentence10uk, translation10)
    
  if placechoiceuk == 'Магазин канцтоварів':
    image3 = Image.open('stationary_shop.jpg')
    st.image(image3, caption='Photo by @candelarms on Unsplash') 
    cola, colb, colc, cold = st.columns(4)
    with cola:
      st.subheader("Корисні вирази")
    with colb:
      st.subheader("Італійський переклад")
    with colc:
      st.subheader("От як це звучить")
    with cold:
      st.subheader("На кирилиці")  
    sentence11uk = "Доброго ранку"
    sentence12uk = "Мені потрібні зошити"
    sentence13uk = "Мені потрібна лінійка"
    sentence14uk = "Мені потрібні кольорові олівці"
    sentence15uk = "Мені потрібен пенал"
    
    phrasebook(sentence11uk)
    phrasebooknotranslation(sentence12uk, translation12)
    phrasebooknotranslation(sentence13uk, translation13)
    phrasebook(sentence14uk)
    phrasebooknotranslation(sentence15uk, translation15)
    
  
with st.expander("See credits"):
     st.write("""
          - For images: https://unsplash.com/
        """)
     
     st.write("""- For the tutorial: https://docs.streamlit.io/library/api-reference/media
     """)
