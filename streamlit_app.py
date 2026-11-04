import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

st.title("My app yes thats the name : 'My app' ")

st.header("The data from the DSO_4")

df = pd.read_csv('DSP_4.csv',sep=';')


st.dataframe(df)


st.header("A plot of wiek based on objawy")
fig = plt.figure(1)

fig.add_axes(sb.barplot(x='objawy',y='wiek',data=df))

st.pyplot(fig)

st.header('Text processing')

from transformers import pipeline

option = st.selectbox(
    "Options",
    ["Emotions of text (eng)",
     "Translate from english to german"
      ]
      ,index =0
)
if option == "Emotions of text (eng)":
    st.text("A simple emotion detector based on the 'sentiment-analysis' model\nJust enter text and press the button")

    text = st.text_area(label="Enter text")

    if st.button("Process",icon="🔥") : 
        if text : 
            clasifier = pipeline('sentiment-analysis',device="cpu")
            ansver = clasifier(text)
            st.write(ansver)
            st.success("Text processed")
        else:
                    st.error("Text cant be empty")

if option == "Translate from english to german":

    st.text("A simple translator based on the 'Helsinki-NLP/opus-mt-en-de' model\nJust enter text and press the button")
    
    text = st.text_area(label="Enter text")
    
    if  st.button("Translate",icon="🔥") : 
        if text:
            translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de",device="cpu")
            ansver = translator(text)
            st.write(ansver)
            st.success("Translated sucesfully")
        else:
            st.error("Text cant be empty")


st.text("Made with love by s32057",text_alignment='right',width="stretch")