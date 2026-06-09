import streamlit as st
from sql_generator import generate_sql
from sql_validator import validate_query
from query_executor import execute_query

st.set_page_config(
    page_title="AI SQL Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Natural Language to SQL Analyzer")

st.write(
    "Ask questions in English and get SQL query results from the employee database."
)

st.markdown("---")

st.markdown("### 💬 Enter Your Question")

question = st.text_area(
    "",
    height=180,
    placeholder="Example: Show employees whose salary is greater than 60000 and sort them by salary in descending order"
)

generate = st.button(
    "🚀 Generate SQL",
    use_container_width=True
)

st.sidebar.title("📌 Sample Questions")

st.sidebar.write("1. Show all employees")
st.sidebar.write("2. Show IT employees")
st.sidebar.write("3. Count total employees")
st.sidebar.write("4. Show highest paid employee")
st.sidebar.write("5. Show employees whose salary is greater than 60000")
st.sidebar.write("6. Show average salary by department")

st.sidebar.markdown("---")

st.sidebar.title("🗂 Database Info")
st.sidebar.write("Database: employee.db")
st.sidebar.write("Table: employees")
st.sidebar.write("Columns:")
st.sidebar.write("- id")
st.sidebar.write("- name")
st.sidebar.write("- department")
st.sidebar.write("- salary")

if generate:

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        try:
            sql_query = generate_sql(question)

            st.markdown("### 🧾 Generated SQL Query")
            st.code(sql_query, language="sql")

            if validate_query(sql_query):

                result = execute_query(sql_query)

                st.markdown("### 📊 Query Result")
                st.dataframe(
                    result,
                    use_container_width=True
                )

                st.success("Query executed successfully!")

            else:
                st.error("Unsafe SQL Query Detected!")

        except Exception as e:
            st.error(f"Error: {e}")