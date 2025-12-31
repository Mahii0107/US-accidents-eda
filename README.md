# 🚗 US Accidents Exploratory Data Analysis & Dashboard

## 📌 Project Overview
This project performs an Exploratory Data Analysis (EDA) on the US Accidents dataset, followed by an interactive Streamlit dashboard to visualize accident patterns across time, weather, light conditions, and severity.

The goal is to extract meaningful insights from a large real-world dataset and present them through clean, high-impact visualizations.

### Dataset Source
The dataset can be downloaded from Kaggle:
https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents

## 🎯 Objectives
- Understand temporal patterns in accidents (hour, weekday, month)
- Analyze how weather and light conditions affect accident severity
- Identify relationships between visibility, distance, and severity
- Build an interactive dashboard for dynamic exploration
- Demonstrate data cleaning, analysis, and visualization skills

## 📂 Project Structure
```
US-accidents-eda/
│
├── US_Accident.py              # Streamlit dashboard
├── US_eda.ipynb                # Data cleaning & EDA notebook
├── requirements.txt            # Required libraries
├── README.md                   # Project documentation
└── data/
    └── us_accidents_sample.csv # Cleaned dataset
```

## 🧹 Data Cleaning & Preprocessing
Performed in `US_eda.ipynb`:
- Dropped irrelevant columns (IDs, descriptions, unused coordinates)
- Handled missing values (median imputation where appropriate)
- Converted date-time columns and extracted:
  - Hour
  - Weekday
  - Month
- Saved the cleaned dataset for reuse in Streamlit

✔ Cleaning is separated from visualization to improve performance and maintainability

## 📊 Exploratory Data Analysis (EDA)
### Key Analyses Performed:
- Accident distribution by hour, weekday, and month
- Day vs Night accident comparison
- Severity distribution across weather conditions
- Relationship between visibility and accident distance
- Identification and explanation of outliers

### Visualization Techniques Used:
- Count plots
- Histograms
- Box plots
- Scatter plots
- Heatmaps (multivariate analysis)

## 🖥️ Streamlit Dashboard
The interactive dashboard allows users to:
- Filter accidents by severity
- Compare day vs night accident trends
- Explore hourly accident patterns
- Analyze weather vs severity using heatmaps
- Visually inspect visibility vs distance relationships

The dashboard is optimized for:
- Clean UI
- Fast loading
- High-impact visual insights

## 🛠️ Technologies Used
- **Python** - Core programming language
- **Pandas & NumPy** - Data manipulation
- **Matplotlib & Seaborn** - Visualization
- **Streamlit** - Interactive dashboard
- **Git & GitHub** - Version control and deployment

## 🚀 Getting Started

### Prerequisites

pip install -r requirements.txt

### Running the Dashboard

streamlit run app.py


### Running the EDA Notebook
Open `US_eda.ipynb` in Jupyter Notebook or JupyterLab to explore the analysis.

## 📌 Key Insights
- Day has overwhelmingly more incidents , with severity 2 dominating across all light conditions, while sunrise/sunset periods show minimal activity.
- Night incidents, though far fewer in total, show a slightly higher proportion of severe cases (severity 3-4) compared to day, suggesting nighttime accidents may be more serious when they occur.
- Certain weather conditions show a higher proportion of severe accidents
- Low visibility is often associated with longer accident impact distances

## 🌐 Live Demo
(https://us-accidents-eda-nnak9scyqfgew3oaibadgp.streamlit.app/)


## 👩‍💻 Author
**Mahi**  
Aspiring Data Analyst | Python | Data Visualization | EDA
