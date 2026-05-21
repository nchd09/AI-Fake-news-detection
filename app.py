
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

.big-title {
    font-size: 45px;
    font-weight: bold;
    color: #1f77b4;
}

.subtitle {
    font-size: 18px;
    color: gray;
}

.result-box {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

st.sidebar.title("📌 Thông Tin")

st.sidebar.info("""
### Fake News Detection AI
Hệ thống AI phát hiện tin giả bằng Machine Learning, giúp người dùng phân tích và đánh giá độ tin cậy của các bài báo, tin tức trên mạng xã hội.
""")

st.sidebar.success("Fake News Detection AI")

# =========================
# HEADER
# =========================

st.markdown(
    '<p class="big-title">📰 Fake News Detection AI</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Hệ thống AI phát hiện tin giả bằng Machine Learning</p>',
    unsafe_allow_html=True
)

st.markdown("---")

# =========================
# LAYOUT
# =========================

col1, col2 = st.columns([2,1])

with col1:

    news = st.text_area(
        "✍️ Nhập nội dung bài báo",
        height=300,
        placeholder="Ví dụ: Scientists discovered..."
    )

    predict_btn = st.button("🔍 Phân tích tin tức")

with col2:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2965/2965879.png",
        width=220
    )

# =========================
# PREDICTION
# =========================

if predict_btn:

    if news.strip() == "":
        st.warning("⚠️ Vui lòng nhập nội dung")
    else:

        vector = vectorizer.transform([news])

        prediction = model.predict(vector)

        probability = model.predict_proba(vector)

        fake_percent = round(probability[0][0] * 100, 2)
        real_percent = round(probability[0][1] * 100, 2)

        st.markdown("##  Kết quả phân tích")

        c1, c2 = st.columns(2)

        with c1:

            if prediction[0] == 1:
                st.success("✅ REAL NEWS")
            else:
                st.error("❌ FAKE NEWS")

        with c2:

            st.metric(
                label="Độ tin cậy",
                value=f"{max(fake_percent, real_percent)}%"
            )

        st.markdown("---")

        st.subheader(" Xác suất")

        st.progress(int(real_percent))

        m1, m2 = st.columns(2)

        with m1:
            st.metric("Fake", f"{fake_percent}%")

        with m2:
            st.metric("Real", f"{real_percent}%")

        st.markdown("---")

        st.info("""
         AI phân tích dựa trên:
        - từ khóa
        - cấu trúc văn bản
        - mẫu dữ liệu đã train
        """)

# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption("Made with love using Streamlit")