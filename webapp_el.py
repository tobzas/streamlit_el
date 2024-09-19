#import streamlit as st

#st.set_page_config(layout="wide")

# st.title("Lecture VDO Selection")

# Title HTML Code
#title_writing = "Lecture VDO Selection"
#title_format = f'<p style="text-align: center; font-family: ' \
#               f'Arial; color: #ffffff; font-size: 40px; ' \
#               f'font-weight: bold;">{title_writing}</p>'
#st.markdown(title_format, unsafe_allow_html=True)


#st.write("This is some text")

#st.header("This is a header")

#st.markdown("## This an h2 header")

#st.caption("This is a caption")

# st.video('https://www.youtube.com/watch?v=tDt7X6coxvs') 
# video_format

import os
import streamlit as st
import json
# import streamlit_wordcloud as wordcloud
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import random
import numpy as np
from PIL import Image
import ast

st.set_page_config(
    layout="wide",
)


try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    script_dir = os.getcwd()  # Get current working directory if __file__ is not defined


# file_list_vdo = os.path.join('data_list_vdo.json')
# # output_folder = os.path.join('data.json')

# ## list vdo name 
# with open(file_list_vdo, 'r', encoding='utf-8') as file:
#     data_file_vdo  = json.load(file)
# # st.write(output_folder)

# Title of the app
st.title("Lecture VDO Selection")

def format_func(option):
    return CHOICES[option]

# options=list(CHOICES.keys()), format_func=format_func
CHOICES = {'vdo01': "E-DTM-CH5-Virach_97m", "vdo02": "E-superai_Kiyoki_5m.mp4", "vdo03": "J-Proj_Hayashi_db_design_5m.mp4", "vdo04": "J-TM_CH9_Virach_5m.mp4", "vdo05": "T-SuperAI-Virach_5m.mp4"}

col21, col22 = st.columns([1, 1])
with col21:
    selected_vdo = st.selectbox(
        "Lecture VDO Selection : ", 
        index=0,
        options=list(CHOICES.keys()), format_func=format_func
        # label_visibility=st.session_state.visibility,
        # disabled=st.session_state.disabled,
    )
## first_letter
first_letter = CHOICES[selected_vdo][0]
# st.write(CHOICES[selected_vdo])
# st.write(first_letter)
file_path_data = f'{selected_vdo}/{selected_vdo}.json' #vdo01.json


output_folder = os.path.join('Test_data',file_path_data)
# file_path_edit_tmp = os.path.join(output_folder,output_txt_file+"_edited_subtitle_tmp.srt")
# Load the JSON data
with open(output_folder, 'r', encoding='utf-8') as file:
    data = json.load(file)


# st.write(data)
with col22:
    # Dropdown for selecting the language
    # language = st.selectbox("Choose a language:", options=["Japanese", "English (US)", "Thai"])
    if first_letter =='J':
        opt_language = "Japanese"
    
    if first_letter =='T':
        opt_language = "Thai"

    if first_letter =='E':
        opt_language = "English (US)"

    language = st.radio("Select language", horizontal=False, options=["Original ( "+opt_language+" )" ,"Japanese", "English (US)", "Thai"])
    # st.write(language)
    # Display the selected language data
    # if language:


    text_language = language
    word_to_check = "Original"

    # Check if the word is in the text
    if word_to_check in text_language:
        # st.write(True)
        language = "Original (language)"
        # st.write(data[language][0])
    else:
        language = language
        # st.write(False)
        # st.write(language)
 
#     if 
    selected_data = data[language][0]
    # st.write(selected_data)
    #     st.write(f"**Video Content**: {selected_data['file_vdo']}")
    #     st.write(f"**Japanese Subtitles**: {selected_data['sub_jp']}")
    #     st.write(f"**English Subtitles**: {selected_data['sub_en']}")
    #     st.write(f"**Thai Subtitles**: {selected_data['sub_th']}")
    #     st.write(f"**Summary**: {selected_data['file_summery']}")
    #     st.write(f"**Quiz**: {selected_data['file_quiz']}")
    #     st.write(f"**Keywords**: {selected_data['file_keywords']}")
  

# st.write(path_data)

st.markdown("---")

col11, col12 = st.columns([2, 1])
with col11:
    """
    Lecture Video
    """ 
    path_data =  f"{selected_vdo}/{selected_data['file_vdo']}"

    # Convert SRT to VTT format
    # We'll read the SRT file and replace the necessary parts to match the VTT format

    # Define the path to the uploaded SRT file
    file_srt = os.path.join('Test_data',f"{selected_vdo}/{selected_data['subtitle']}")
    check_file_subtitle= os.path.exists(file_srt)
    if check_file_subtitle:
        srt_file_path = file_srt
        vtt_file_path = srt_file_path.replace('.srt', '.vtt')

        # Read the content of the SRT file
        with open(srt_file_path, 'r', encoding='utf-8') as file:
            srt_content = file.read()
        

        style = "STYLE::cue { text-align: center; }"
        # Convert the SRT content to VTT format
        vtt_content = "WEBVTT\n\n"+ style +"\n\n" + srt_content.replace(',', '.')

        # Save the converted content to a new VTT file
        with open(vtt_file_path, 'w', encoding='utf-8') as vtt_file:
            vtt_file.write(vtt_content)

        # vtt_file_path
        file_vtt    = os.path.join(vtt_file_path)
        # st.write(file_vtt)
        ## Video and Subtitle
        # VIDEO_URL = "https://example.com/not-youtube.mp4"
        # # st.video(VIDEO_URL, subtitles="subtitles.vtt")
        # st.video(VIDEO_URL)
        file_mp4 = os.path.join('Test_data',path_data)
        video_file = open(file_mp4, "rb")
        video_bytes = video_file.read()

        st.video(video_bytes, subtitles=file_vtt)
        # st.video(video_bytes)



    else:
        file_mp4 = os.path.join('Test_data',path_data)
        video_file = open(file_mp4, "rb")
        video_bytes = video_file.read()
        st.video(video_bytes)

with col12:
    """
    Wordcloud
    """

    if first_letter =='J':
        if language == "Japanese":
            font_path= os.path.join('Font',"Japanese/Gen_Jyuu_Gothic_L Monospace_Light.ttf")
        
        if language == "Thai" :
            font_path= os.path.join('Font',"Thai/THSarabunIT.ttf")

        if language =="English (US)" :
            font_path= os.path.join('Font',"English/AbhayaLibre-Regular.ttf")

        if language =="Original (language)" :
            font_path= os.path.join('Font',"Japanese/Gen_Jyuu_Gothic_L Monospace_Light.ttf")

    if first_letter =='T':
        if language == "Japanese":
            font_path= os.path.join('Font',"Japanese/Gen_Jyuu_Gothic_L Monospace_Light.ttf")
        
        if language == "Thai" :
            font_path= os.path.join('Font',"Thai/THSarabunIT.ttf")

        if language =="English (US)" :
            font_path= os.path.join('Font',"English/AbhayaLibre-Regular.ttf")

        if language =="Original (language)" :
            font_path= os.path.join('Font',"Thai/THSarabunIT.ttf")

    if first_letter =='E':
        if language == "Japanese":
            font_path= os.path.join('Font',"Japanese/Gen_Jyuu_Gothic_L Monospace_Light.ttf")
        
        if language == "Thai" :
            font_path= os.path.join('Font',"Thai/THSarabunIT.ttf")

        if language =="English (US)" :
            font_path= os.path.join('Font',"English/AbhayaLibre-Regular.ttf")

        if language =="Original (language)" :
            font_path= os.path.join('Font',"English/AbhayaLibre-Regular.ttf")




    # if language == "Japanese" or  first_letter =='J':
    #     font_path= os.path.join('Font',"Japanese/Gen_Jyuu_Gothic_L Monospace_Light.ttf")

    # if language == "Thai"  or  first_letter =='T':
    #     font_path= os.path.join('Font',"Thai/THSarabunIT.ttf")

    # if language =="English (US)"  or  first_letter =='E':
    #     font_path= os.path.join('Font',"English/AbhayaLibre-Regular.ttf")

    # path = os.path.join(f'{download_path}/{output_audio_file}')
    # check_file = os.path.exists(path)

    file_keywords = os.path.join('Test_data',f"{selected_vdo}/{selected_data['file_keywords']}")
    check_file_keywords= os.path.exists(file_keywords)
    if check_file_keywords:

        with open(file_keywords, 'r', encoding='utf-8') as file:
            text_keywords = file.read()

        # st.write(text_keywords)
        # Create some sample text
        #text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'
        text = text_keywords

        # # Create and generate a word cloud image:
        # wordcloud = WordCloud().generate(text)

        # # Display the generated image:
        # fig, ax = plt.subplots()
        # ax.imshow(wordcloud, interpolation='bilinear')
        # ax.axis("off")
        # # Remove the spines (the borders)
        # for spine in ax.spines.values():
        #     spine.set_visible(False)

        # st.pyplot(fig)
        ######### V2 ###########
        # os.path.join('data.json')
        mask = np.array(Image.open(os.path.join('stormtrooper_mask.png')))
        # mask = np.array(Image.open(path.join(d, "stormtrooper_mask.png")))

        def grey_color_func(word, font_size, position, orientation, random_state=None,
                        **kwargs):
            return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)
        
        # Adding movie script specific stopwords
        stopwords = set(STOPWORDS)
        stopwords.add("int")
        stopwords.add("ext")

        # Define image size
        image_width = 400
        image_height = 200

        # wc = WordCloud(max_words=1000,  stopwords=stopwords, margin=10, random_state=1, width=image_width, height=image_height).generate(text)
        # wc = WordCloud(max_words=1000, mask=mask, stopwords=stopwords, margin=10, random_state=1, background_color=None, mode="RGBA").generate(text)
        wc = WordCloud(font_path=font_path, max_words=1000,  stopwords=stopwords, margin=10, random_state=1, mode="RGBA").generate(text)

        # Store default colored image
        default_colors = wc.to_array()

        # st.title("Custom colors")
        # fig1, ax1 = plt.subplots()
        # ax1.imshow(wc.recolor(color_func=grey_color_func, random_state=3), interpolation="bilinear")
        # ax1.axis("off")
        # st.pyplot(fig1)

        # st.title("Default colors")
        fig2, ax2 = plt.subplots(figsize=(40, 40))  # กำหนดขนาดของรูปภาพให้เล็กลง
        ax2.imshow(default_colors, interpolation="bilinear")
        ax2.axis("off")
        st.pyplot(fig2)

        # Optionally, save the output image
        wc.to_file("a_new_hope.png")

    ######### End V2 ###########
    # st.write(text_keywords)
st.markdown("---")

col21, col22 = st.columns([1, 1])
with col21:
    """
    Summary 
    """ 

    file_summery = os.path.join('Test_data',f"{selected_vdo}/{selected_data['file_summery']}")
    check_file_summery= os.path.exists(file_summery)
    if check_file_summery:
        with open(file_summery, 'r', encoding='utf-8') as file:
            summery_text = file.read()

        st.write(summery_text)
        st.markdown("---")


with col22:
    """
     Quiz 
    """
    # file_quiz = os.path.join('Test_data',f"{selected_vdo}/{selected_data['file_quiz']}")
    # with open(file_quiz, 'r', encoding='utf-8') as file:
    #     quiz_text = file.read()
    
    # st.write(quiz_text)

    # Define the path to the uploaded file
    file_path = os.path.join('Test_data',f"{selected_vdo}/{selected_data['file_quiz']}")
    check_file_quiz = os.path.exists(file_path)
    
    # if check_file_quiz:
    #     # st.write(file_path)
    #     # Read the content of the file
    #     with open(file_path, 'r', encoding='utf-8') as file:
    #         content = file.read()

    #     # Split the content into questions
    #     questions = content.strip().split("\n\n")

    #     # Create a quiz with each question as a st.radio widget
    #     for i, question_block in enumerate(questions, 1):
    #         lines = question_block.splitlines()
    #         if len(lines) >= 2:
    #             question = lines[0]
    #             options = lines[1:5]
    #             correct_answer = lines[5].split(": ")[1] if len(lines) > 5 else None
                
    #             # Display the question
    #             # st.write(f"**Question {i}:** {question}")
    #             st.write(f"**Question :** {question}")
                
    #             # Display the options
    #             user_answer = st.radio(
    #                 label="",
    #                 options=options,
    #                 key=f"q{i}"
    #             )

    #             # st.write(f"User answer: {user_answer}")
    #             # st.write(f"Correct answer: {correct_answer}")

    #             # Extract only the first character (the letter) from the user_answer and correct_answer
    #             user_answer_letter = user_answer.split('.')[0].strip()  # This extracts "B" from "B. ด้วยการแนะนำตัว"
    #             correct_answer_letter = correct_answer.strip()

    #             # st.write(f"User answer: {user_answer_letter}")
    #             # st.write(f"Correct answer: {correct_answer_letter}")
                
    #             # # Optionally, check if the user's answer is correct
    #             # if correct_answer and user_answer == correct_answer:
    #             #     st.success("Correct! 🎉")
    #             # elif correct_answer:
    #             #     st.error(f"Wrong! The correct answer is: {correct_answer}")
    #             # if correct_answer and user_answer.strip().lower() == correct_answer.strip().lower():
    #             #     st.success("Correct! 🎉")
    #             # elif correct_answer:
    #             #     st.error(f"Wrong! The correct answer is: {correct_answer}")
    #             # Now compare the letters only
    #             if user_answer_letter == correct_answer_letter:
    #                 st.success("Correct! 🎉")
    #             # else:
    #                 # st.error(f"Wrong! The correct answer is: {correct_answer}")

    #             st.write("---")  # Add a horizontal line between questions
    if check_file_quiz:
    # st.write(file_path)
        # Read the content of the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Split the content into questions
        questions = content.strip().split("\n\n")

        # Create a quiz with each question as a st.radio widget
        for i, question_block in enumerate(questions, 1):
            lines = question_block.splitlines()
            if len(lines) >= 2:
                question = lines[0]
                options = lines[1:5]
                correct_answer = lines[5].split(": ")[1] if len(lines) > 5 else None

                # Prepend a placeholder to the options list
                options_with_placeholder = ["Select an answer"] + options

                # Display the question
                st.write(f"**Question :** {question}")

                # Display the options with a placeholder
                user_answer = st.radio(
                    label="",
                    options=options_with_placeholder,
                    key=f"q{i}",
                    index=0  # Ensure "Select an option" is selected by default
                )

                # Check if user has selected an actual option
                if user_answer != "Select an answer":
                    # Extract only the first character (the letter) from the user_answer and correct_answer
                    user_answer_letter = user_answer.split('.')[0].strip()  # This extracts "B" from "B. ด้วยการแนะนำตัว"
                    correct_answer_letter = correct_answer.strip()

                    # Now compare the letters only
                    if user_answer_letter == correct_answer_letter:
                        st.success("Correct! 🎉")
                    else:
                         st.error(f"Wrong! :x: ")
                        # st.error(f"Wrong! The correct answer is: {correct_answer}")
                # else:
                #     st.warning("Please select an answer to proceed.")

                st.write("---")  # Add a horizontal line between questions
