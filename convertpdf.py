__author__ = "V.A. Moss and Shankar Dutt"
__version__ = "0.1"

import streamlit as st
from pdf2image import convert_from_bytes
from io import BytesIO
import base64
import os

st.set_page_config(page_title="Convert PDF to JPEG", initial_sidebar_state="expanded", )
st.sidebar.title("Convert PDF to JPEG")
st.sidebar.subheader("Author: Shankar Dutt (shankar.dutt@anu.edu.au) and Vanessa Moss (vanessa.moss@csiro.au)")

option = st.sidebar.selectbox("Menu",('4096px','1024px'))
if option =='4096px':
    uploaded_file = st.file_uploader("Choose a PDF file", type=['pdf'])

    def get_image_download_link(img,filename,text):
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        href =  f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
        return href

    if uploaded_file is not None and uploaded_file.type == "application/pdf":
        try:
            images = convert_from_bytes(uploaded_file.read(),size=(4096,None))
            for index, page in enumerate(images):
                st.image(page, use_column_width=True)
                name = os.path.splitext(uploaded_file.name)[0]
                st.markdown(get_image_download_link(page, name+'_page_'+f'{index+1}'+'_4096px'+'.jpg', 'Download ' + name +'_page_'+f'{index+1}'+'_4096px'+ '.jpg'), unsafe_allow_html=True)
        except:
            st.write("Choose different file. Input file not correct")

if option == '1024px':
    uploaded_file = st.file_uploader("Choose a PDF file", type=['pdf'])


    def get_image_download_link(img, filename, text):
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        href = f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
        return href


    if uploaded_file is not None and uploaded_file.type == "application/pdf":
        try:
            images = convert_from_bytes(uploaded_file.read(), size=(1024, None))
            for index, page in enumerate(images):
                st.image(page, use_column_width=True)
                name = os.path.splitext(uploaded_file.name)[0]
                st.markdown(get_image_download_link(page, name + '_page_' + f'{index + 1}' + '_1024px' + '.jpg',
                                                    'Download ' + name + '_page_' + f'{index + 1}' + '_1024px' + '.jpg'),
                            unsafe_allow_html=True)
        except:
            st.write("Choose different file. Input file not correct")