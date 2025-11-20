import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

data = pd.DataFrame({
    "Fruit" : ["Apple", "Banana", "Cherries", "Onions"],
    "Amount" : [10, 20, 30, 40]

})

fig = px.bar(data, x="Fruit", y="Amount", title="Fruit Sales")
st.plotly_chart(fig)