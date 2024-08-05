import streamlit as st
import pandas as pd

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM ping;', ttl="10m")

chart_data = pd.DataFrame(df.itertuples(), columns=["temperature", "humidity"])

st.line_chart(chart_data)
