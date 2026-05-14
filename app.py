import streamlit as st
import pickle

# =====================
# LOAD MODEL
# =====================

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.write("✅ Model loaded")
st.write("✅ Vectorizer loaded")

# =====================
# UI
# =====================

st.title("📰 Fake News Detection AI")

news = st.text_area("Nhập nội dung tin tức")

# =====================
# BUTTON
# =====================

if st.button("Kiểm tra"):

    st.write("🔥 Button clicked")

    if news.strip() == "":
        st.warning("Vui lòng nhập nội dung")

    else:

        st.write("📌 Nội dung đã nhập:")
        st.write(news)

        # Vectorize
        vector = vectorizer.transform([news])

        st.write("✅ Vector created")

        # Predict
        prediction = model.predict(vector)

        st.write("✅ Prediction done")

        st.write(prediction)

        # Result
        if prediction[0] == 1:
            st.success("✅ Đây là tin thật")
        else:
            st.error("❌ Đây là tin giả")