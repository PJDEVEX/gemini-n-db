import streamlit as st
from src.ai.generator import get_gemini_response, prompt_text, read_sql_query


st.set_page_config(page_title="Data Dreamer", page_icon=":rocket:", layout="wide")
st.header("DataDreamer")
st.text("Unleash Insights, Imagine Possibilities: Where Data Dreams Come True")

question = st.text_input("Question:", key="input",
                         autocomplete="on",
                         help="Enter your input here",
                         )

submit = st.button("Submit", key="submit")

# if submit is clicked
if submit:
    response = get_gemini_response(question, prompt_text)
    print("Response is: ", response)
    sql_query = response.strip('`')
    sql_query = sql_query.replace("sql","")
    print("SQL Query is: ", sql_query)
    response = read_sql_query(sql_query, "student.db")
    st.subheader("Answer: ")
    for row in response:
        for row in response:
            st.text(row)