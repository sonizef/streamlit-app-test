import streamlit as st
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# Obtenez les informations de connexion depuis secrets.toml
db_config = st.secrets["postgresql"]

# Créez une URL de connexion pour SQLAlchemy
DATABASE_URL = f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

# Créez un moteur SQLAlchemy
engine = create_engine(DATABASE_URL)

# Définissez votre requête SQL
query = """
SELECT TO_CHAR(date, 'YYYY-MM-DD HH24:mi:SS') AS date, temperature, humidity
FROM ping
ORDER BY date
"""

# Exécutez la requête et chargez les résultats dans un DataFrame
df = pd.read_sql(query, engine)

# Convertir la colonne 'date' en type datetime
df['date'] = pd.to_datetime(df['date'])

# Vérifiez le type de données et un extrait des données
st.write(df.head())

# Configurez Streamlit
st.title('Line Chart of Temperature and Humidity Arduino')

# Créez le Line Chart
st.line_chart(df.set_index('date'))
