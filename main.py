import streamlit as st  # For web interface
import pandas as pd  # For data manipulation
import datetime  # For handling dates
import csv  # For reading/writing CSV file
import os  # For file operations

# Define the file name for storing mood data
MOOD_FILE = "mood_tracker.csv"

# Function to read mood data from CSV file
def load_mood_data():
    if not os.path.exists(MOOD_FILE) or os.stat(MOOD_FILE).st_size == 0:
        return pd.DataFrame(columns=["Date", "Mood"])
    try:
        return pd.read_csv(MOOD_FILE, encoding="utf-8")  # Fix Encoding Issue
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=["Date", "Mood"])

# Function to add new mood entry to CSV file
def save_mood_data(date, mood):
    with open(MOOD_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])

# Streamlit app configuration
st.set_page_config(page_title="Mood Tracker 😊📊", page_icon="📌", layout="centered")

# Custom CSS for styling (Dark Mode & Buttons)
st.markdown("""
    <style>
    .st-emotion-cache-1104ytp h1 {
     color: white;
    }
    
    .st-emotion-cache-1104ytp h3 {
    color: white;
    }
            
    .st-emotion-cache-1104ytp h4 {
    color: white;
    }       
          
    .stApp {
        background-color: #121212;
    }
    h1, h2, h3, h4, p, label {
        color: white;
    }
    .stButton>button {
        background-color: #ff7f50 !important;
        color: white !important;
        font-size: 16px !important;
        padding: 12px 28px !important;
        border-radius: 10px !important;
    }
    .stButton>button:hover {
        background-color: #e76f3c !important;
    }
    .stSelectbox div {
        background-color: #1e1e1e !important;
        color: white !important;
    }
    .stSuccess {
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# App title with emoji
st.markdown("<h1 style='text-align: center;'>📝 Mood Tracker 📊</h1>", unsafe_allow_html=True)

# Get today's date
today = datetime.date.today()

# Mood Input Section
st.markdown("### 🌟 How are you feeling today?")
mood = st.selectbox("💭 Select your mood:", ["😃 Happy", "😞 Sad", "😡 Angry", "😐 Neutral"])

# Log Mood Button
if st.button("✅ Log Mood"):
    save_mood_data(today, mood)
    st.success("🎉 Mood Logged Successfully!")

# Load existing mood data
data = load_mood_data()

# Mood Data Visualization
if not data.empty:
    st.markdown("---")
    st.markdown("### 📈 Mood Trends Over Time")

    # Convert date column to datetime format
    data["Date"] = pd.to_datetime(data["Date"])

    # Count occurrences of each mood
    mood_counts = data["Mood"].value_counts()

    # Display bar chart
    st.bar_chart(mood_counts)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>❤️ Built with love by Muhammad Hanzala Ali ❤️</h4>", unsafe_allow_html=True)
