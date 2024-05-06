import streamlit as st
import myfunction as fn

city = [
    "Ambon",
    "Balikpapan",
    "Banjarmasin",
    "Baubau",
    "Biak",
    "Bombana",
    "Jakarta",
    "Kendari",
    "Makasar",
    "Manokwari",
    "Nabire",
    "Nunukan",
    "Oki",
    "Palu",
    "Serui",
    "Surabaya",
    "Tarakan",
]


st.title(":ship: Freshwater supply prediction💦")
st.caption(
    "This application can help you estimate the amount of freshwater needed on the trip"
)


col1, col2 = st.columns(2)
depart = col1.selectbox(
    "Select your starting port", (city), index=None, placeholder="Select port here ..."
)
destin = col2.selectbox(
    "Select your destination port",
    (city),
    index=None,
    placeholder="Select port here ...",
)

durr = st.number_input(
    "Trip Duration",
    value=None,
    placeholder="Insert estimated trip duration here...!",
    help="Number only",
)

gas = st.button("Calculate", type="primary")

if gas:
    if depart == None or destin == None or durr == None:
        st.error(
            "One or more of your input is empty, please check your input again",
            icon="🚨",
        )
    elif depart == destin:
        st.error(
            "Starting and destination port cannot be same",
            icon="🚨",
        )
    else:
        fresh_water = fn.predict_fresh_water(depart, destin, durr)
        st.write("You need to prepare approximately: ")
        html_str = f"""
<style>
    .result{{
        font-size : 60px;
        font-weight : bold;

    }}
</style>
<p class="result">{str(int(fresh_water))} Litter</p>
"""
        st.markdown(html_str, unsafe_allow_html=True)
