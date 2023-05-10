import streamlit as st

st.subheader('Hello, I am Anubhav :wave:')
st.title('I am a Data Analyst')
st.write("**My mission?** To boldly go where no data has gone before! I spend my days exploring the mysteries of data, teasing out insights, 🕵️‍♂️ and building models that can make the world a better place. This page is my humble attempt to share my personal projects and data analysis musings with the world. 🌍")

# loading image
# project1_img = 'home/anubhav/pyprojects/databhav.github.io/images/upwork.png'
st.write('##')
with st.container():
    st.header('My Projects')
    image_column, text_column = st.columns((1,2))
    with image_column:
        
        with text_column:
            st.write("---")
            st.subheader('Project 1: Upwork Job posting data analysis and Visualisation')
            st.write('---')