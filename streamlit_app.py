import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher
import yaml
from yaml.loader import SafeLoader
from PIL import Image
import bcrypt
print(dir(Hasher))
st.set_page_config(initial_sidebar_state="collapsed")

#st.sidebar.markdown("Hi!")

#st.markdown("**Child-centric** design!")
st.subheader( "AI-Powered e-Learning Tool")
st.header( '''Welcome to :blue[LogoMate]!''', divider='rainbow')
st.markdown ( ''' A cutting-edge solution designed to ***transform language*** learning for **students** with :blue[learning difficulties]. :sunglasses:''' )

video_file = open("images/LogoMate - Language Learning _ Easy and Fun.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)
#names=["Diwei","Roberto"]
#username = ["DiweiL","RobertoD"]
#passwords =["123abc","456efg"]

#hashed_passwords=stauth.Hasher(passwords).generate() #bcrypt
#print(hashed_passwords)

with open('data/Admin.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)
authenticator.login('main', fields = {'Form name': 'Login'})
if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')     
    st.divider()     
    #st.switch_page("pages/1_🏠_Homepage.py")   
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        match = st.button("Learn_new_voca")
    with col2:
        management = st.button("learn_from_your_mistakes")
    with col3:
        prediction = st.button("📈 Memory_test")
    with col4:
        game = st.button("Games")
    #st.divider()
    if match:
        st.write("You have selected Learn_new_voca")
        st.switch_page("pages/01_Learn_new_voca.py")
    elif management:
        st.write("You have selected learn_from_your_mistakes")
        st.switch_page("pages/02_learn_from_your_mistakes.py")
    elif prediction:
        st.write("You have selected 📈 Memory_test")
        st.switch_page("pages/03_Memory_test.py")
    elif game:
        st.write("You have selected Games")
        st.switch_page("pages/04_Games.py")
#st.divider()
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
    signup = st.button("Sign up")
    reset=st.button("Reset Password")
    forget=st.button("Forget Password")
    if signup:
        st.switch_page("pages/reset.py")   

