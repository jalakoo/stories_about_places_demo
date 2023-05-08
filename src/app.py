import streamlit as st
from n4jgpt import Neo4jGPTQuery
from n4j import execute_query
from streamlit_card import card
import logging

# CONFIG
logger = logging.getLogger(__name__)
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(
    format=FORMAT)
logger.setLevel(logging.DEBUG)

OAI_KEY = st.secrets["OPENAI_KEY"]
N4J_URI = st.secrets["NEO4J_URI"]
N4J_U = st.secrets["NEO4J_USER"]
N4J_P = st.secrets["NEO4J_PASSWORD"]
st.set_page_config(layout="wide")

# HEADER
h1, h2, h3 = st.columns([1,8,1])
with h1:
    st.image("media/sap-logo-65e754a1f5347a94dde28597350a080e.png", width = 280)
with h2:
    st.write("")
with h3:
    st.image("media/person_icon.png")

# SEARCH QUERY
gds_db = Neo4jGPTQuery(
    url=N4J_URI,
    user=N4J_U,
    password=N4J_P,
    openai_api_key=OAI_KEY,
)
result = None
search_query = st.text_area("Search Query", value="")
if search_query is not None and search_query != "":
    # Convert search text to query
    result = gds_db.run(search_query)
    if result is not None:
        st.table(result)








