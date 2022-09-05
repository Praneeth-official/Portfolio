

import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie

from PIL import Image

profile_pic =Image.open("/Users/praneethbadanapally/Desktop/Portfolio/assets/prt.jpg")

st.set_page_config(page_title="Praneeth Profile Page", page_icon=profile_pic,layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
    local_css("style/button.css")
st.balloons()
def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)
lottie_coding = load_lottiefile("lottiefiles/coding.json")


        
st.title("Welcome to Praneeth's World")
st.image(profile_pic,width=200)

with st.container():
    st.subheader("Hi, I am Praneeth Badanapally :wave:")
    st.title("A Data Analyst from India")
    st.write("### Passionate about to explore the technology. An inquisitive towards technology to empower the development and to solve interesting and challenging problems using computer programming.")

with st.container():
    st.write("---")
    left_column,right_column =st.columns(2)
    with left_column:
        st.header("# What I do?")
        st.write("#")
        st.write(
            """
            # Usually I am technophile and likes to do

            ### - Explore

            ### - Learn

            ### - Implement

            ### - Solve real time problems using ML and AI

            ## If this sounds interesting to you ,consider me and visit to my social handles mentioned below or put a message to me to reach you and let me help you to solve problem
        
            """
        )   
    with right_column:
        st_lottie(
    lottie_coding,
    speed = 1,
    reverse= False,
    loop= True,
    quality= "hign",
    # height=500,
    width= 500,
    key=None,
)
with st.container():
    st.write("---")
    left_column,right_column =st.columns(2)
    with left_column:
        def load_lottiefile(filepath:str):
            with open(filepath,"r") as f:
                return json.load(f)
        lottie_hello = load_lottiefile("lottiefiles/hello.json")

    #     def load_lottieurl(url:str):
    #         r = requests.get(url)
    #         if r.status_code !=200:
    #                 return None
    #         return r.json()
    # lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_emy3lanj.json")

    st_lottie(
        lottie_hello,
        speed = 1,
        reverse= False,
        loop= True,
        quality= "hign",
        height=500,
        width= 500,
        key="hello"
    )
    st.write(" # Let's ")
    t = '<p style="font-family:sans-serif; color:Green; font-size: 42px;"><b>Connect</b></p>'
        # st.markdown(t, unsafe_allow_html=True)
        # new_title = '<p style="font-family:sans-serif; color:Blue; font-size: 42px;"><b>Build</b></p>'
        # st.markdown(new_title, unsafe_allow_html=True)
        # s = '<p style="font-family:sans-serif; color:Red; font-size: 42px;"><b>Grow</b></p>'
    st.markdown(t, unsafe_allow_html=True)
    with right_column:
        
        def load_lottieurl(url:str):
            r = requests.get(url)
            if r.status_code !=200:
                    return None
            return r.json()
    lottie_anime = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_bpqri9y8.json")

    st_lottie(
        lottie_anime,
        speed = 1,
        reverse= False,
        loop= True,
        quality= "hign",
        height=500,
        width= 500,
        key="bye"
    )
    st.write(" # Solve ")
    q = '<p style="font-family:sans-serif; color:Green; font-size: 42px;"><b>Together</b></p>'
        # st.markdown(t, unsafe_allow_html=True)
        # new_title = '<p style="font-family:sans-serif; color:Blue; font-size: 42px;"><b>Build</b></p>'
        # st.markdown(new_title, unsafe_allow_html=True)
        # s = '<p style="font-family:sans-serif; color:Red; font-size: 42px;"><b>Grow</b></p>'
    st.markdown(q, unsafe_allow_html=True)
    
    
    with st.container():
        left_column,right_column =st.columns(2)
        with left_column:
            social_media = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<!-- Add font awesome icons -->
<a href="https://www.instagram.com/praneethbadanapally/?hl=en" class="fa fa-instagram"></a>
<a href="https://linkedin.com/in/badanapally-praneeth-657682196" class="fa fa-linkedin"></a>
<a href="https://medium.com/@badanapallypraneeth3" class="fa fa-medium"></a>
<a href="https://github.com/Praneeth-official/intro-html" class="fa fa-github"></a>
 

"""
    st.markdown(social_media,unsafe_allow_html=True)
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=
            True)
    local_css("style/button.css")

   
       
        
        




st.header(":mailbox: Get in touch with me !!!!")
contact_form ="""
<form action="https://formsubmit.co/praneethbadanapally8@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Details of your problem"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form,unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=
        True)
local_css("style/style.css")
