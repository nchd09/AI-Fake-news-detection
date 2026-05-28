import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(
    page_title="Model Analysis",
    page_icon="📊", 
    layout="wide"
)

st.title("📊 Model Analysis")

st.write("""
Trang hiển thị:
         - hiệu suất của mô hình
         - phân bố dữ liệu
         - so sánh các chỉ số đánh giá
         - khả năng hoạt động của hệ thống
""")

st.markdown("---")

st.subheader("📈 Model Performance")

c1,c2,c3,c4 = st.columns(4)
c1.metric("Accuracy", "97%")
c2.metric("Precision", "96%")
c3.metric("Recall", "98%")
c4.metric("F1-Score", "97%")

st.info("""
Ý nghĩa:
- Accuracy: độ chính xác tổng thể
- Precision: tỉ lệ dự đoán đúng trong số dự đoán là fake news
- Recall: số bỏ sót tin giả trong tổng số tin giả thực tế
- F1-Score: cân bằng giữa precision và recall
""")

st.markdown("---")

st.subheader("📊 Data Distribution")
labels = ["Accuracy", "Precision", "Recall", "F1-Score"]
values = [97, 96, 98, 97]
fig, ax = plt.subplots(figsize=(8,5))
bars = ax.bar(labels,values)
ax.set_ylim(0, 100)
ax.set_ylabel("Score (%)")
ax.set_title("Model Performance Scores")
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0,
             height+1,
                f'{height}%',
                ha='center'
            )
    
st.pyplot(fig)

st.success("""
           Biểu đồ thể hiện:
           - Accuracy cao cho thấy mô hình tổng thể tốt
           -Recall cao cho thấy mô hình ít bỏ sót tin giả
           - Precision cao cho thấy mô hình ít dự đoán sai tin giả
""")

st.markdown("---")

st.subheader("📰 Phân bố dữ liệu dataset")

fake_count = 23481
real_count = 21417

labels = ["Fake News", "Real News"]
sizes = [fake_count, real_count]
fig2, ax2 = plt.subplots(figsize=(6,6))
ax2.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%"
    )

ax2.set_title("Dataset Distribution")

st.pyplot(fig2)

st.info("""
Biểu đồ tròn thể hiện: tỉ lệ dữ liệu fake news và real news trong dataset. Dataset khá cân bằng, giúp mô hình học tốt cả hai loại tin tức.
""")

st.markdown("---")

