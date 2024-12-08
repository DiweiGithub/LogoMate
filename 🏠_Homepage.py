import streamlit as st
from PIL import Image

import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

img=Image.open('images/ppt_image.jpg')
st.image(img)
st.logo("images/LogoMate_logo_font.PNG", icon_image="images/LogoMate_logo_font.PNG")

#st.sidebar.markdown("Hi!")
    
st.subheader( "AI-Powered e-Learning Tool")

st.markdown("**Child-centric** design!")

st.header( '''Welcome to :purple[LogoMate]!''', divider='rainbow')
st.markdown ( ''' A cutting-edge solution designed to transform language learning for ***students*** with :purpe[learning difficulties]. :sunglasses:''' )

with open('data/Admin.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
authenticator.logout()

st.header( '''Welcome to :green[AgriFlow]!''', divider='rainbow')

col1, col2, col3 = st.columns(3)
with col1:
    match = st.button("🧦 Investment Matching")
with col2:
    management = st.button("📊 Budget Management")
with col3:
    prediction = st.button("📈 Predictive Trend Analytics")
#st.divider()
if match:
    st.write("You have selected 🧦 Investment Matching")
    st.switch_page("pages/3_🔗_Investment_Matching.py")
elif management:
    st.write("You have selected 📊 Budget Management")
    st.switch_page("pages/2_📊_Budget Management.py")
elif prediction:
    st.write("You have selected 📈 Predictive Trend Analytics")
    st.switch_page("pages/4_📈_Predictive_Trend_analytics.py")

#st.divider()
