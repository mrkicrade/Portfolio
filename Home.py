import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('Mrkić Rade')
    content = """
    Zdravo. Ja sam Mrkić Rade i ja sam Python developer i educator web dizajna i web programiranja. Radim kao asistent i saradnik u 
    on line školi programiranja "Danilo Vešović. 
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have build in Python. Please, feel free to contact me.
"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

