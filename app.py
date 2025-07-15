import streamlit as st
import speech_recognition as sr

st.set_page_config(page_title="Voice-Controlled Calculator", page_icon="🧮")
st.header("Voice-Controlled Calculator")

col1, col2 = st.columns([1, 1])  # side-by-side (i.e., same row)

with col1:
    st.image("calculator.png", width=300)
    
with col2:
    st.markdown(
        """
        Press the button and say something like:
        - `three plus five`
        - `twelve divided by four`
        - `seven times nine`
        """
        )
    
    if st.button("🎤 Start Voice Input"):
        recognizer = sr.Recognizer()
        
        with st.spinner("🎤 Listening... Please speak clearly"):
            with sr.Microphone() as source:
                try:
                    audio = recognizer.listen(source, timeout=5)
                    spoken_text = recognizer.recognize_google(audio)
                    st.success(f"You said: {spoken_text}")
                except sr.WaitTimeoutError:
                    st.warning("Listening timed out. Please try again.")
                except sr.UnknownValueError:
                    st.warning("Sorry, couldn't understand. Please try again.") 
                except Exception as e:
                    st.error(f"Error: {e}")

   
