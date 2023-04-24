import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpg')

with col2:
    st.tile('Mrkić Rade')
    content = """
    Zdravo. Ja sam Mrkić Rade i ja sam Python developer i educator web dizajna i web programiranja. Radim kao asistent i saradnik u 
    on line školi programiranja "Danilo Vešović. 
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have build in Python. Please, feel free to contact me.
"""

st.write(content2)