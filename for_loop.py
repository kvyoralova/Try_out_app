import streamlit as st
from PIL import Image
from gtts import gTTS
from googletrans import Translator
translator = Translator()
from transliterate import translit, get_available_language_codes


st.title("Італійський розмовник для дітей - Итальянский разговорник для детей")
purposeru = st.write(""" -  UK: Цей додаток має на меті допомогти українським дітям, як російською, так і українською мовою, вивчити та використовувати деякі корисні фрази італійською""") 
st.write(""" -  RU: Это приложение нацелено на то, чтобы помочь украинским и русскоязычным детям выучить и использовать некоторые полезные фразы на итальянском языке""")
purpose = st.checkbox('Clik here if you want to know the purpose of this app in another language')
if purpose:
  lang = st.selectbox("Insert the code of a language in which you want to know the purpose of the app:", ('en', 'de', 'it'))
  purposelang = lang.text
  translation = translator.translate(purposeru, dest = purposelang)
  purposetext= translation.text
  st.write(purposetext)
else:
  pass


language = st.radio( "Виберіть мову - Выберите язык" , ('Русский', 'Yкраїнський'))

if language == 'Русский':
  placechoice = st.selectbox("Куда ты хочешь пойти сегодня? Bыбери одно из указанных мест:", ('Площадка для игр', 'Школа', 'Магазин канцтоваров'))
  if placechoice == 'Площадка для игр':
      image1 = Image.open('playground.jpg')
      st.image(image1, caption='Photo by Pond Juprasong on Unsplash')
  if placechoice == 'Школа':
      image2 = Image.open('school.jpg')
      st.image(image2, caption='Photo by Kenny Eliason on Unsplash')
  if placechoice == 'Магазин канцтоваров':
      image3 = Image.open('stationary_shop.jpg')
      st.image(image3, caption='Photo by @candelarms on Unsplash')
  else:
    pass
cola, colb, colc, cold = st.columns(4)
with cola:
  st.subheader("Полезные выражения")
with colb:
  st.subheader("Итальянский перевод")
with colc:
  st.subheader("Вот как это звучит")
with cold:
  st.subheader("На кириллице")
      
phrases_ru = {'Площадка для игр': [{'Пойдем в парк' : 'Andiamo al parco'},
                                   {'Давай играть в прятки' : 'Giochiamo a nascondino'},
                                   {'Давай покатаемся на качелях' : "Andiamo sull'altalena"},
                                   {'Пойдем на горку' : 'Andiamo sullo scivolo'},
                                   {'Давайте прыгать на скакалке' : 'Saltiamo la corda'}],
              'Школа': [{'Потом поиграем вместе?' : 'Dopo giochiamo insieme?'},
                         {'Давай сделаем пазл' : 'Facciamo un puzzle'},
                         {'Давай рисовать' : 'Disegnamo?'},
                         {'Пойдём в сад?' : 'Andiamo in giardino?'},
                         {'Могу ли я взять твой фломастер?' : 'Mi presti il tuo pennarello?'}],
              'Магазин канцтоваров': [{' Добрый день' : 'Buongiorno'},
                                      {'Мне нужны тетради' : 'Mi servirebbero dei quaderni'},
                                      {'Мне нужна линейка' : 'Avrei bisogno di un righello'},
                                      {'Мне нужны цветные карандаши' : 'Mi servirebbero le matite colorate'},
                                      {'Сколько это стоит?' : 'Quanto costa?'}]
                        }


for (key, value) in phrases_ru.items():
  if placechoice == key:
    for phrasecouple in phrases_ru.values():
      for el in phrasecouple:
        for (key, value) in el.items():
          col1, col2, col3, col4 = st.columns(4)
          with col1:
            st.write(key)
          with col2:
            translation = translator.translate(key, dest= 'it')
            translated_text= translation.text
            if translated_text != value:
              translated_text = value
            else:
              translated_text = translated_text
            st.write(translated_text)
          with col3:
            tts1=gTTS(translated_text, lang = 'it')
            tts1.save('your_file.mp3')
            audio_file = open('your_file.mp3', 'rb')
            st.audio(data=audio_file, format="audio/mp3", start_time = 0)
          with col4:
            transliterated_text = translit(translated_text, 'ru')
            st.write(transliterated_text)
  else:
    pass
if language == 'Yкраїнський':
  placechoice = st.selectbox("Куди ти хочеш піти сьогодні? Bыбери одно з вказаних місць:", ('Майданчик для ігор', 'Школа', 'Магазин канцтоварів'))
  if placechoice == 'Майданчик для ігор':
    image1 = Image.open('playground.jpg')
    st.image(image1, caption='Photo by Pond Juprasong on Unsplash')
  if placechoice == 'Школа':
    image2 = Image.open('school.jpg')
    st.image(image2, caption='Photo by Kenny Eliason on Unsplash')
  if placechoice == 'Магазин канцтоварів':
    image3 = Image.open('stationary_shop.jpg')
    st.image(image3, caption='Photo by @candelarms on Unsplash')
else:
  pass

phrases_ukr = {'Майданчик для ігор': [{'Підемо в парк' : 'Andiamo al parco'},
                                   {'Давай пограємо в хованки' : 'Giochiamo a nascondino'},
                                   {'Xодімо на гойдалки' : "Andiamo sull'altalena"},
                                   {'Підемо на гірку' : 'Andiamo sullo scivolo'},
                                   {'Давайте стрибати на скакалці' : 'Saltiamo la corda'}],
              'Школа': [{'Потім пограємось разом?' : 'Dopo giochiamo insieme?'},
                         {'Давай зробимо пазл' : 'Facciamo un puzzle'},
                         {'Давай малювати' : 'Disegnamo?'},
                         {'Підемо в сад?' : 'Andiamo in giardino?'},
                         {'Чи можу я узяти твій фломастер?' : 'Mi presti il tuo pennarello?'}],
              'Магазин канцтоварів': [{'Доброго ранку' : 'Buongiorno'},
                                      {'Мені потрібні зошити' : 'Mi servirebbero dei quaderni'},
                                      {'Мені потрібна лінійка' : 'Avrei bisogno di un righello'},
                                      {'Мені потрібні кольорові олівці' : 'Mi servirebbero le matite colorate'},
                                      {'Скільки це коштує?' : 'Quanto costa?'}]
                        }
for (key, value) in phrases_ru.items():
  if placechoice == key: 
    for phrasecouple in phrases_ru.values():
      for el in phrasecouple:
        for (key, value) in el.items():
          col1, col2, col3, col4 = st.columns(4)
          with col1:
            st.write(key)
          with col2:
            translation = translator.translate(key, dest= 'it')
            translated_text= translation.text
            if translated_text != value:
              translated_text = value
            else:
              translated_text = translated_text
            st.write(translated_text)
          with col3:
            tts1=gTTS(translated_text, lang = 'it')
            tts1.save('your_file.mp3')
            audio_file = open('your_file.mp3', 'rb')
            st.audio(data=audio_file, format="audio/mp3", start_time = 0)
          with col4:
            transliterated_text = translit(translated_text, 'uk')
            st.write(transliterated_text)
else:
  pass
