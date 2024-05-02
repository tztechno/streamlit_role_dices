import streamlit as st
import random

dice_images = [
    "./dice/saikoro-illust1.png",
    "./dice/saikoro-illust2.png",
    "./dice/saikoro-illust3.png",
    "./dice/saikoro-illust4.png",
    "./dice/saikoro-illust5.png",
    "./dice/saikoro-illust6.png"
]

st.title("Role 9 Dices")

if st.button("Role"):
    nums = list(range(6))
    s = random.choices(nums, k=9)

    for i in range(3):
        _, col1, col2, col3, _ = st.columns([1.2, 1, 1, 1, 1.2])
        with col1:
            st.image(dice_images[s[i]], width=100)
        with col2:
            st.image(dice_images[s[i+3]], width=100)
        with col3:
            st.image(dice_images[s[i+6]], width=100)

    if (s[0]==s[1]==s[2]) or (s[3]==s[4]==s[5]) or (s[6]==s[7]==s[8]) or (s[0]==s[3]==s[6]) or (s[1]==s[4]==s[7]) or (s[2]==s[5]==s[8]) or (s[0]==s[4]==s[8]) or (s[2]==s[4]==s[6]):
        
        st.markdown("<span style='font-size: 24px; font-weight: bold; color: red;'>Congratulation!</span>", unsafe_allow_html=True)

