import streamlit as st
import json
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Praneeth Activities", page_icon="💡",layout="wide")

st.title("Our Latest Work :sunglasses:")
   
def load_lottiefile(filepath:str):
  with open(filepath,"r") as f:
    return json.load(f)
lottie_active = load_lottiefile("lottiefiles/active.json")
st_lottie(
            lottie_active,
            speed = 1,
            reverse= False,
            loop= True,
            quality= "hign",
            # height=500,
            width= 200,
            key=None,
        )
a ="""
        

        <div class="a">
          <h2>Student Portfolio</h2>
          <div class="p">Developed student user-friendly website of portfolio using <b>Streamlit</b>, of academic work and other forms of educational evidence assembled for the purpose of evaluating coursework quality, learning progress, and academic achievements. </div>

        </div>  
      

        <div class="b">
          <h2>Analysis of Motor Vehicle Collisions in NYC</h2>
          <div class="p">We made analysis of Motor Vehicle Collisions in <b>New York City</b> by applying Data Analysis concepts and visualizing with the help of <b>Streamlit</b> web based framework.Moreover we included every detailed report and analysis by consideration of different parameters.</div>
        </div>  
     
      
        <div class="c">
          <h2>Student Notes Maker</h2>
          <div class="p">An easy note maker web based application using HTML,CSS and JavaScript.</div>
        </div>  
      

        <div class="d">
          <h2>Simple Calculator Using Flutter</h2>
          <div class="p">Created a simple calculator using <b>Flutter</b> to develop cross platform applications for Android, iOS, Linux, macOS, Windows, Google Fuchsia, and the web from a single codebase.</div>
        </div>  
      
      
  """
st.markdown(a,unsafe_allow_html=True)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=
        True)
local_css("style/special.css") 
