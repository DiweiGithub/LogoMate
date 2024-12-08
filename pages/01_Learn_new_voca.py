import streamlit as st
from PIL import Image

img=Image.open('images/ppt_image.jpg')
st.image(img)
st.logo("images/LogoMate_logo_font.PNG", icon_image="images/LogoMate_logo_font.PNG")
