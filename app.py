import streamlit as st
import random

# Page config
st.set_page_config(
    page_title="A Special Question 💕",
    page_icon="💝",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #ffeef8 0%, #ffe0f0 100%);
    }
    .stButton > button {
        width: 100%;
        border-radius: 20px;
        height: 60px;
        font-size: 20px;
        font-weight: bold;
        transition: all 0.3s;
    }
    .yes-button > button {
        background: linear-gradient(45deg, #ff6b9d, #c44569);
        color: white;
        border: none;
    }
    .no-button > button {
        background: white;
        color: #666;
        border: 2px solid #ddd;
    }
    h1 {
        color: #c44569;
        text-align: center;
        font-size: 3em;
        margin-bottom: 30px;
    }
    .question {
        font-size: 1.8em;
        text-align: center;
        color: #333;
        margin: 30px 0;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'answered_yes' not in st.session_state:
    st.session_state.answered_yes = False

# Title
st.markdown("<h1>💝 Valentine's Day 💝</h1>", unsafe_allow_html=True)

# The question
st.markdown("<p class='question'>Will you be my Valentine? 🌹</p>", unsafe_allow_html=True)

# Different "No" button texts that get increasingly desperate/funny
no_button_texts = [
    "No",
    "Are you sure?",
    "Really?",
    "Think again!",
    "Pretty please?",
    "What if I get you flowers?",
    "Come on...",
    "You're killing me here...",
    "I'll cook dinner!",
    "But... but... 🥺",
    "My heart is breaking...",
    "Fine, I'll cry then",
    "The button is barely working now",
    "This button is almost gone",
    "One more click and it's gone!"
]

if not st.session_state.answered_yes:
    col1, col2 = st.columns(2)
    
    # Yes button (gets bigger each time they click no)
    yes_size = 1 + (st.session_state.no_count * 0.3)
    
    with col1:
        st.markdown('<div class="yes-button">', unsafe_allow_html=True)
        if st.button("YES! 💕", key="yes", use_container_width=True):
            st.session_state.answered_yes = True
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # No button gets different text and potentially moves/shrinks
        no_text_index = min(st.session_state.no_count, len(no_button_texts) - 1)
        no_text = no_button_texts[no_text_index]
        
        # Make the no button smaller as they click it
        if st.session_state.no_count < 10:
            st.markdown('<div class="no-button">', unsafe_allow_html=True)
            if st.button(no_text, key="no", use_container_width=True):
                st.session_state.no_count += 1
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        elif st.session_state.no_count < 15:
            # Button gets smaller
            st.markdown(f'<div class="no-button" style="font-size: {100 - st.session_state.no_count * 5}%;">', unsafe_allow_html=True)
            if st.button(no_text, key="no"):
                st.session_state.no_count += 1
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            # Button disappears
            st.markdown("<p style='text-align: center; color: #999; font-style: italic;'>The 'no' option has ceased to exist 😌</p>", unsafe_allow_html=True)

else:
    # Celebration when they say yes!
    st.balloons()
    st.markdown("""
    <div style='text-align: center; padding: 40px;'>
        <h2 style='color: #c44569; font-size: 3em;'>🎉 YAY! 🎉</h2>
        <p style='font-size: 1.5em; color: #333; margin: 20px 0;'>
            I knew you'd say yes! ❤️
        </p>
        <p style='font-size: 1.2em; color: #666;'>
            Get ready for the best Valentine's Day ever! 🌹✨
        </p>
        <p style='font-size: 4em; margin: 30px 0;'>
            💕 😊 💝 🥰 💖
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Ask me again? 😊"):
        st.session_state.answered_yes = False
        st.session_state.no_count = 0
        st.rerun()

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #999; font-size: 0.9em;'>Made with ❤️ just for you</p>", unsafe_allow_html=True)