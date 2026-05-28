import streamlit as st
import pickle
# =========================
# LOAD MODEL
# =========================

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Fake News Detection AI",
    page_icon="📰",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.title {
    font-size: 50px;
    font-weight: bold;
    color: #1f77b4;
}

.subtitle {
    color: gray;
    font-size: 20px;
}

.result-box {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

st.sidebar.title("📌 Navigation")

st.sidebar.info("""
Fake News Detection AI

Công nghệ:
- NLP
- TF-IDF
- PassiveAggressiveClassifier
- Streamlit
""")

# =========================
# HEADER
# =========================

st.markdown(
    '<p class="title">📰 Fake News Detection AI</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">AI phát hiện tin giả bằng Machine Learning</p>',
    unsafe_allow_html=True
)

st.markdown("---")



# =========================
# MAIN LAYOUT
# =========================

col1, col2 = st.columns([2,1])

with col1:

    news = st.text_area(
        "✍️ Nhập nội dung tin tức",
        # value=default_text,
        height=300
    )

    predict_btn = st.button("🔍 Analyze News")

with col2:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2965/2965879.png",
        width=250
    )

# =========================
# PREDICT
# =========================

if predict_btn:

    if news.strip() == "":
        st.warning("⚠️ Vui lòng nhập nội dung")
    else:

        with st.spinner("AI đang phân tích..."):

            vector = vectorizer.transform([news])

            prediction = model.predict(vector)

            probability = model.predict_proba(vector)

            fake_percent = round(probability[0][0] * 100, 2)
            real_percent = round(probability[0][1] * 100, 2)

            st.markdown("## 📊 Result")

            c1, c2 = st.columns(2)

            with c1:
                st.metric("Fake", f"{fake_percent}%")

            with c2:
                st.metric("Real", f"{real_percent}%")

            st.markdown("---")

            if prediction[0] == 1:

                st.success("✅ REAL NEWS")

                st.info("""
                AI nhận thấy:
                - văn phong báo chí rõ ràng
                - nội dung hợp lý
                - ít dấu hiệu clickbait
                """)

            else:

                st.error("❌ FAKE NEWS")

                st.warning("""
                AI nhận thấy:
                - nội dung bất thường
                - từ ngữ cường điệu
                - thiếu nguồn xác thực
                """)

            st.progress(
                int(max(fake_percent, real_percent))
            )

st.markdown("---")



