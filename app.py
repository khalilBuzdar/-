import streamlit as st
import google.generativeai as genai
import random

# آپ کی API Key
API_KEY = "AIzaSyB0AqvpZ72UF9txSfwTuclf-rfA7ZytDy4"
genai.configure(api_key=API_KEY)

# ایپ کی سیٹنگ
st.set_page_config(page_title="بلوچوں کی تاریخ", page_icon="🛡️")

# 1. ویلکم نوٹ (سلائیڈنگ ٹیکسٹ)
welcome_note = """
<marquee style='color: #d35400; font-weight: bold; font-size: 20px; background-color: #fcf3cf; padding: 10px;'>
    🌟 پروانہ بلوچ ویلکم ... بلوچوں کی تاریخ کے سفر میں خوش آمدید 🛡️ | 
    حق باھوٹ و میار ! بلوچ قوم کی غیرت و تاریخ زندہ باد 🦅 | 
    خلیل بزدار عرف پروانہ بلوچ آپ کی خدمت میں حاضر ہے ✍️
</marquee>
"""
st.markdown(welcome_note, unsafe_allow_html=True)

# 2. ایپ کا مین نام
st.markdown("<h1 style='text-align: center; color: #2c3e50;'>📜 بلوچوں کی تاریخ</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold;'>ترتیب و پیشکش: خلیل بزدار عرف پروانہ بلوچ</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# سرچ بار
user_input = st.text_input("", placeholder="سرچ پروانہ (بلوچ تاریخ کے بارے میں لکھیں)...")

# جواب کے نیچے کے مختلف انداز (Signatures)
signatures = [
    "\n\n---\n> **✍️ یہ بلوچوں کی تاریخ خلیل بزدار عرف پروانہ بلوچ نے بنایا ہے۔**\n> 📞 فون: 03284782193",
    "\n\n---\n> **🛡️ بلوچ تاریخ کی یہ معلومات خلیل بزدار (پروانہ بلوچ) کی محنت کا نتیجہ ہیں۔**\n> 📱 رابطہ: 03284782193",
    "\n\n---\n> **🦅 فخرِ بلوچ: خلیل بزدار عرف پروانہ بلوچ کی پیشکش۔**\n> 📞 واٹس ایپ: 03284782193",
    "\n\n---\n> **📜 اس علمی کاوش کے بانی: خلیل بزدار عرف پروانہ بلوچ**\n> 📞 موبائل: 03284782193"
]

if user_input:
    with st.spinner('پروانہ بلوچ جواب تیار کر رہا ہے...'):
        try:
            model = genai.GenerativeModel('gemini-1.5-flash',
                system_instruction="تمہارا نام پروانہ بلوچ ہے۔ تم صرف بلوچ تاریخ کے بارے میں جواب دو گے۔ زبان صرف اردو یا بلوچی ہوگی۔")
            
            response = model.generate_content(user_input)
            st.markdown(f"<div style='direction: rtl; text-align: right; font-size: 20px; line-height: 1.6;'>{response.text}</div>", unsafe_allow_html=True)
            st.markdown(random.choice(signatures))
            
            # امیج سرچ لنک
            img_url = f"https://www.google.com/search?q={user_input}+baloch+history&tbm=isch"
            st.markdown(f"<br><a href='{img_url}' target='_blank'><button style='width:100%; height:50px; background-color:#2c3e50; color:white; border:none; border-radius:10px; font-size:16px;'>🖼️ اس ٹاپک کی تصاویر دیکھیں</button></a>", unsafe_allow_html=True)
            
        except Exception:
            st.error("نیٹ ورک یا API میں مسئلہ ہے۔")

st.markdown("<br><hr><p style='text-align: center;'>تمام حقوق محفوظ ہیں © خلیل بزدار عرف پروانہ بلوچ</p>", unsafe_allow_html=True)
