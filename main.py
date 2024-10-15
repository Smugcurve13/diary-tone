import streamlit as st
from functions import plotfigure

st.title("Diary Tone")

st.subheader("Positivity")

st.plotly_chart(plotfigure('pos'))

st.subheader("Negativity")

st.plotly_chart(plotfigure('neg'))