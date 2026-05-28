import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Model Analysis")

# Metrics
accuracy = 97
precision = 96
recall = 98
f1 = 97

# Top metrics
c1, c2, c3, c4 = st.columns(4)

c1.metric("Accuracy", "97%")
c2.metric("Precision", "96%")
c3.metric("Recall", "98%")
c4.metric("F1-score", "97%")

st.markdown("---")

# Bar chart

labels = ["Accuracy", "Precision", "Recall", "F1-score"]
values = [accuracy, precision, recall, f1]

fig, ax = plt.subplots()

ax.bar(labels, values)

ax.set_ylim(0, 100)

st.pyplot(fig)

st.markdown("---")

# Pie chart dataset

labels = ["Fake", "Real"]
sizes = [23481, 21417]

fig2, ax2 = plt.subplots()

ax2.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%'
)

st.pyplot(fig2)

