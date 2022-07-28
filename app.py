import random
import streamlit as st
import streamlit.components.v1 as stc

import pandas as pd
import neattext.functions as nfx

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import altair as alt

def load_bible(data):
    df = pd.read_csv(data)
    return df

from utils import HTML_BANNER

def main():
    stc.html(HTML_BANNER.format("Holy Bible App"))
    menu = ["Home", "Multiverse", "About"]

    df = load_bible("data/KJV_Bible.csv")

    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Single Verse Search")
        # st.dataframe(df)
        book_list = df['book'].unique().tolist()
        book_name = st.sidebar.selectbox("Book", book_list)
        chapter = st.sidebar.number_input("Chapter", 1)
        verse = st.sidebar.number_input('Verse', 1)
        bible_df = df[df["book"] == book_name]
        # st.dataframe(bible_df)

        # layout
        c1,c2 = st.columns([2,1])

        # Single Verse Layout
        with c1:
            try:
                selected_passage = bible_df[(bible_df['chapter'] == chapter) & (bible_df['verse'] == verse)]
                passage_details = "{} {} : {}".format(book_name, chapter, verse)
                st.info(passage_details)
                passage = "{}".format(selected_passage['text'].values[0])
                st.write(passage)
            except:
                st.warning("Book out of range.")
        
        with c2:
            st.success("Verse of the Day")
            chapter_list = range(1, 10)
            verse_list = range(1, 20)
            ch_choice = random.choice(chapter_list)
            vs_choice = random.choice(verse_list)
            random_book_name = random.choice(book_list)

            st.write("{} {} : {}".format(random_book_name, ch_choice, vs_choice))
            rand_bible_df = df[df["book"] == random_book_name]

            try:
                randomly_passage = rand_bible_df[(rand_bible_df['chapter'] == ch_choice) & (rand_bible_df['verse'] == vs_choice)]
                mytext = randomly_passage['text'].values[0]
            except:
                mytext = rand_bible_df[(rand_bible_df['chapter'] == ch_choice) & (rand_bible_df['verse'] == vs_choice)]
            
            st.write(mytext)
        
        search_term = st.text_input('Search Topic: ')
        with st.expander("View Results"):
            retrieved_df = df[df["text"].str.contains(search_term)]
            st.dataframe(retrieved_df[['book', 'chapter', 'verse', 'text']])

    elif choice == "Multiverse":
        st.subheader("Multiverse Retrieval")
    elif choice == "About":
        st.subheader("About")


if __name__ == "__main__":
    main()
