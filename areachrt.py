"""
 this pandas data csv file 
import streamlit as st 
import pandas as pd


data = {"Name": ["John","Anna","Peter","Linda"],
        "Age": [23,29,35,32],
        "City": ["New York", "Pris", "Berlins", "London"]}
df = pd.DataFrame(data)

st.dataframe(df) #scrollable table

st.table(df)#non scrollable table


Displaying json data
import streamlit as st 

json_data = {
    "name": "John Doe",
    "age": 30,
    "adress": {
         "street": "123 road",
         "city": "kotwa"
    }
}
st.json(json_data)


import streamlit as st
import pandas as pd 
data = {"Name":["john", "anna", "peter", "linda"],
        "Age":[23,29,35,32],
        "City": ["New York", "Parsi", "Berlin", "London"]}
df = pd.DataFrame(data)
city = st.selectbox("Choose a city to filter", df["City"].unique())
filtered_data = df[df["City"] == city]

st.write(f"Data for city: {city}")
st.dataframe(filtered_data)


import streamlit as st
import pandas as pd 
data = {"Name":["john", "anna", "peter", "linda"],
        "Age":[23,29,35,32],
        "City": ["New York", "Parsi", "Berlin", "London"],
        "score": [85, 92, 79, 85]
        }

df = pd.DataFrame(data)


value_of_style = st.number_input("Enter the minimum number to display in yellow",value= 80)
styled_df = df.style.applymap(lambda x: "background-color: yellow" if isinstance(x, int) and x > value_of_style else " ")
st.dataframe(styled_df)


#DATA VISUALIZATION"""

import streamlit as st
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["A","B","C"]
)

st.area_chart(data)



