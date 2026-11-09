import streamlit as st
import streamlit.components.v1 as components

st.title("Tienes una invitación")

# Usamos HTML puro y el reproductor de Lottie para saltarnos la librería problemática
lottie_html = """
<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
<lottie-player 
    src="https://lottie.host/4b9a8ad7-204f-4f37-82e9-763145543601/x5kQU0nePB.json" 
    background="transparent" 
    speed="1" 
    style="width: 300px; height: 300px; margin: auto;" 
    loop 
    autoplay>
</lottie-player>
"""

# Le decimos a Streamlit que dibuje ese HTML nativamente
components.html(lottie_html, height=350)