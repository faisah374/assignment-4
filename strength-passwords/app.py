import streamlit as st
import re

st.set_page_config(page_title="password strength checker", page_icon="🔒", layout="wide")

st.title("Password Strength Checker")
st.markdown(""""
#welcome to the ultimate password strength checker!
this app will help you determine the strength of your password and provide tips on how to make it stronger.🔏""")

password = st.text_input("Enter your password:", type="password")

feedback = []
score = 0
if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Your password is too short. It should be at least 8 characters long.")
    if  re.search(r"[A-Z]", password):
        score += 1
    else: 
        feedback.append("Your password should contain at least one uppercase letter.")
    if  re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Your password should contain at least one lowercase letter.")
        
    if  re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Your password should contain at least one number.")
    if  re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Your password should contain at least one special character.")
    if score == 5:
            feedback.append("✅Your password is strong!")
    elif score == 4:
                feedback.append("Your password is medium.")
    if score == 3:
                feedback.append("Your password is weak.")            
    if feedback:
        st.markdown("## improvements suggestions:")
        for tip in feedback:
                st.write(tip)
    else:
        st.info("Your password is strong!")


