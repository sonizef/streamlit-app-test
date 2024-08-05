import streamlit as st

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM ping;', ttl="10m")

# Print results.
for row in df.itertuples():
    st.write(f"{row.temperature} has a :{row.humidity}:")
