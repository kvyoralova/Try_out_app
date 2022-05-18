import streamlit as st
from PIL import Image
from gtts import gTTS
from transliterate import translit, get_available_language_codes

#st.title("Итальянский разговорник для детей - Італійський розмовник для дітей")

#language = st.radio( "Выберите язык - Виберіть мову" , ('Русский', 'Yкраїнський'))

#if language == 'Русский':
  #placechoice = st.selectbox("Куда ты хочешь пойти сегодня? Bыбери одно из указанных мест:", ('Площадка для игр', 'Школа', 'Магазин'))
  #if placechoice == 'Площадка для игр':
    #st.header("Русский")
    #text = "Andiamo sull'altalena"
    #st.write(translit(text, 'ru'))

from transliterate.base import TranslitLanguagePack, registry

class ExampleLanguagePack(TranslitLanguagePack):
    language_code = "ru"
    language_name = "Russian"
    pre_processor_mapping = {
    u"sci": u"щ",
    u"gi": u"дж",
    u"o": u"о"
}
registry.register(ExampleLanguagePack, force=True)

st.write(get_available_language_codes())

# ['el', 'hy', 'ka', 'ru', 'example']

st.write(translit(text, 'example'))

# Lor5m 9psum 4olor s9t 1m5t
