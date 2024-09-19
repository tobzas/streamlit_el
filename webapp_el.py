import streamlit as st

st.title("Lecture VDO Selection")


title_writing = "Test Title"
title_format = f'<p style="text-align: center; font-family: ' \
               f'Arial; color: #000000; font-size: 40px; ' \
               f'font-weight: bold;">{title_writing}</p>'
st.markdown(title_format, unsafe_allow_html=True)


st.write("This is some text")

st.header("This is a header")

st.markdown("## This an h2 header")

st.caption("This is a caption")



st.video('https://www.youtube.com/watch?v=tDt7X6coxvs') 
