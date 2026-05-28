import streamlit as st

st.title("📘 About Project")

st.write("""
## Fake News Detection AI

Đây là hệ thống AI giúp phát hiện tin giả bằng Machine Learning.

### 🎯 Mục tiêu
- chống lan truyền fake news
- hỗ trợ kiểm chứng thông tin
- nâng cao nhận thức cộng đồng

### 🛠 Công nghệ sử dụng
- Python
- NLP
- TF-IDF
- PassiveAggressiveClassifier
- Streamlit

### 📊 Dataset
Fake and Real News Dataset từ Kaggle.

### 👨‍💻 Chức năng
- Phân tích tin tức
- Dự đoán fake/real
- Hiển thị confidence score
- Dashboard phân tích model
""")

st.image(
    "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
    width=300
)

