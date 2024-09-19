import streamlit as st

st.set_page_config(layout="wide")

# st.title("Lecture VDO Selection")

# Title HTML Code
title_writing = "Lecture VDO Selection"
title_format = f'<p style="text-align: center; font-family: ' \
               f'Arial; color: #ffffff; font-size: 40px; ' \
               f'font-weight: bold;">{title_writing}</p>'
st.markdown(title_format, unsafe_allow_html=True)


st.write("This is some text")

st.header("This is a header")

st.markdown("## This an h2 header")

st.caption("This is a caption")



st.video('https://www.youtube.com/watch?v=tDt7X6coxvs') 
