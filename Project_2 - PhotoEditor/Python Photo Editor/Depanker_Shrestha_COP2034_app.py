import streamlit as st 
import numpy as PIL
from PIL import Image 
from filters import apply_filter
import os 

st.sidebar.title('PixelPerfect ')
st.sidebar.write('Welcome to PixelPerfect! In this app you will be able to edit the image you upload. This application cosists of 5 filters that you are able to choose from to edit your photos. In addition, you are also able to increase or decrease the intesity of the filter allowing you to create the perfect photo!') 

col1, col2 = st.columns([4,1])
logo = 'fau_logo.png'
with col1: 
    st.markdown("<h1 style = 'text-align: center;'>Depanker Shrestha</h1>", unsafe_allow_html = True) 
    st.markdown("<h1 style = 'text-align: center;'>Final Project COP2034</h1>", unsafe_allow_html = True) 
    st.markdown("<h1 style = 'text-align: center;'>May 3rd 2023</h1>", unsafe_allow_html = True) 
    st.markdown('--'*50)
with col2: 
    st.image(logo, width = 100)
    
image = st.file_uploader('upload your image', type =['jpg','png','jpeg'])

if image: 
    img = Image.open(image)
    filters = st.sidebar.radio('Filters', ('Original', 'Blur', 'Detail', 'Black and White', 'Smooth', 'Inverted'))
    
    if filters != 'None':
        intensity = st.sidebar.slider('Intensity', 1, 255, 1, 1)
        filtered_img = apply_filter(filters, img, intensity)
        
        original_col, filtered_col = st.columns(2)

        with original_col:
            st.image(img, caption='Before', use_column_width=True)

        with filtered_col:
            st.image(filtered_img, caption='After', use_column_width=True)        
        filename = f"{filters.replace(' ', '_')}_{image.name}"
        filtered_img.save(os.path.join('output', f'{filename}.jpg'), 'JPEG')

        with open(os.path.join('output', f'{filename}.jpg'), 'rb') as f:
            image = f.read()
            st.download_button(label='Download filtered image', data=image, file_name=filename, mime='image/jpg')
    
  