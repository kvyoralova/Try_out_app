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

for key in phrases_ru.keys():
  for choice in placechoice:
    for phrasecouple in phrases_ru.values():
      for el in phrasecouple:
        for (key, value) in el.items():
          col1, col2, col3, col4 = st.columns(4)
          with col1:
            st.write(key)
          with col2:
            translation = translator.translate(key, dest='it')
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
      #if language == 'Русский':
        #lan = 'ru'
      #elif language == 'Yкраїнський':
        #lan = 'uk'
      #else:
        #pass
            transliterated_text = translit(translated_text, 'ru')
            st.write(transliterated_text)
else:
  pass

#translation2 = "Giochiamo a nascondino"
#translation3 = "Andiamo sull'altalena"
#translation4 = "Andiamo sullo scivolo"
#translation5 = "Saltiamo la corda"
#translation6 = "Dopo giochiamo insieme?"
#translation7 = "Facciamo un puzzle"
#translation8 = "Disegnamo?"
#translation9 = "Andiamo in giardino?"
#translation10 = "Mi presti il tuo pennarello?"
#translation11 = "Buongiorno"
#translation12 = "Mi servirebbero dei quaderni"
#translation13 = "Avrei bisogno di un righello"
#translation14 = "Mi servirebbero le matite colorate"
#translation15 = "Avrei bisogno di un astuccio"

