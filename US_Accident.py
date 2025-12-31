import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="US Accidents EDA", layout="wide")

st.title("🚗 US Accidents Analysis Dashboard")
st.write("Interactive Exploratory Data Analysis of US Traffic Accidents")

@st.cache_data
def load_data():
    return pd.read_csv("data/US_accidents_sample.csv")

df = load_data()

st.sidebar.header("Filters")

severity = st.sidebar.multiselect(
    "Select Severity",
    options=sorted(df['Severity'].unique()),
    default=sorted(df['Severity'].unique())
)

light = st.sidebar.multiselect(
    "Light Condition",
    options=df['Sunrise_Sunset'].dropna().unique(),
    default=df['Sunrise_Sunset'].dropna().unique()
)

df_filtered = df[
    (df['Severity'].isin(severity)) &
    (df['Sunrise_Sunset'].isin(light))
]

st.subheader("🚦 Accidents by Light Condition")

plt.style.use('dark_background')

fig, ax = plt.subplots()
sns.countplot(
    x='Sunrise_Sunset',
    data=df_filtered,
    palette='Set2',
    ax=ax
)
ax.set_xlabel("Light Condition")
ax.set_ylabel("Accident Count")
ax.ticklabel_format(style='plain', axis='y')

st.pyplot(fig,use_container_width=False)


st.subheader("⏰ Accidents by Hour")

hourly = df_filtered['Hour'].value_counts().sort_index()

fig, ax = plt.subplots()
ax.plot(hourly.index, hourly.values)
ax.set_xlabel("Hour of Day")
ax.set_ylabel("Accident Count")

st.pyplot(fig)


st.subheader("🌧 Weather vs Severity")

weather_sev = pd.crosstab(
    df_filtered['Weather_Condition'],
    df_filtered['Severity'],
    normalize='index'
)

top_weather = weather_sev.sum(axis=1).sort_values(ascending=False).head(8).index
weather_sev = weather_sev.loc[top_weather]

fig, ax = plt.subplots(figsize=(8,4))
sns.heatmap(weather_sev, annot=True, cmap='YlOrRd', ax=ax)

st.pyplot(fig)
