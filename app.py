import streamlit as st
import time
import streamlit as st
st.title("النشاط التفاعلي ✨")
# نخزن القيمة في session_state
if "user_input" not in st.session_state:
   st.session_state.user_input = ""
# حقل الإدخال
user_input = st.text_input(
   "اكتبي إجابتك هنا:",
   value=st.session_state.user_input,
   key="input_box"
)
# زر التحقق
if st.button("تحقق"):
   if user_input.strip() != "":
       st.success("إجابة ممتازة 👏")
   else:
       st.warning("اكتبي إجابة أولاً")
# زر المسح
if st.button("مسح"):
   st.session_state.user_input = ""
   st.session_state.input_box = ""
   st.rerun()
st.set_page_config(page_title="تجربة الجملة التكرارية for", layout="centered")
# عنوان
st.markdown("<h1 style='text-align:center;'>✨ for تجربة الجملة التكرارية </h1>", unsafe_allow_html=True)
st.write("أدخل النص أو القائمة (القائمة مفصولة بفواصل):")
# إدخال المستخدم
user_input = st.text_input("")
# زر مسح صغير بجانب الإدخال
col1, col2 = st.columns([4,1])
with col2:
   if st.button("مسح"):
       st.session_state.clear()
       st.rerun()
# عرض النتائج
if user_input:
   st.markdown("<br>", unsafe_allow_html=True)
   # إذا قائمة
   if "," in user_input:
       items = [item.strip() for item in user_input.split(",") if item.strip()]
       for index, item in enumerate(items):
           st.markdown(
               f"""
<div style="
                   background-color:#FFB6C1;
                   padding:12px;
                   margin:12px 0;
                   border-radius:12px;
                   text-align:center;
                   font-weight:bold;
                   font-size:20px;
                   color:#222;">
                   ⭐ {item}
</div>
               """,
               unsafe_allow_html=True
           )
           time.sleep(0.2)
   # إذا نص
   else:
       for char in user_input:
           st.markdown(
               f"""
<div style="
                   background-color:#ADD8E6;
                   padding:12px;
                   margin:12px 0;
                   border-radius:12px;
                   text-align:center;
                   font-weight:bold;
                   font-size:20px;
                   color:#222;">
                   🌟 {char}
</div>
               """,
               unsafe_allow_html=True
           )
           time.sleep(0.2)





