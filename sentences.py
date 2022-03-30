import requests
import streamlit as st



st.markdown("<style>#MainMenu, footer{visibility:hidden} </style>", unsafe_allow_html=True)

col1,col2 = st.columns([3,1])
with col1:
    st.title('Definitions and Sentences')
with col2:
    st.error('With love from Vahid')
word = st.text_input('Enter a word')
if word:
    url =f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    try:
        re = requests.get(url).json()
        # ipa = re[0]['phonetics'][0]['text']
        # if ipa == False:
        #     ipa = re[0]['phonetics'][]['text']
        audio = re[0]['phonetics'][0]['audio']
        if audio == False:
            audio = re[0]['phonetics'][1]['audio']
        ms = re[0]['meanings']
        meanings = []

        for i in ms:
            pos = i["partOfSpeech"]
            for j in i['definitions']:
                if 'example' in j.keys():
                    defs = j['definition']
                    ex = j['example']
                    meanings.append([defs,ex,pos])
                else:
                    defs = j['definition']
                    meanings.append([defs,'No Example found',pos])


        if meanings:
            # st.code(ipa)
            if audio:
                st.audio(audio)
            for i in meanings:
                st.success(f"Definition: ({pos}) - {i[0]}")
                st.text(f"Examples: {i[1]}\n+++++++++")
        else:
            st.error('Sorry No such word!')
    except KeyError:
        st.error('Sorry baby, your word was not found!')
