import streamlit as st
import pandas as pd

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Définissez votre requête SQL
query = """
SELECT date, temperature, humidity
FROM ping
ORDER BY date
"""

# Exécutez la requête et chargez les résultats dans un DataFrame
df = pd.read_sql(query, conn)

# Configurez Streamlit
st.title('Line Chart of Temperature and Humidity')

# Créez le Line Chart
st.line_chart(df.set_index('date'))
