import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Analisis Sentimen Sampah Plastik Bali",
    layout="wide"
)

st.title("📊 Dashboard Analisis Sentimen Pengelolaan Sampah Plastik di Bali")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Overview",
        "Distribusi Sentimen",
        "Perbandingan Model",
        "Confusion Matrix",
        "Insight Penelitian"
    ]
)
