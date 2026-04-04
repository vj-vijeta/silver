import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(page_title="Ei Mindspark Dashboard", layout="wide")

# Data structures based on the provided reports
SCHOOLS_DATA = {
    "Silver Oaks High School": {
        "metrics": {
            "Students": 1717,
            "Avg Usage (mins/week)": 27.4,
            "Accuracy (%)": 71.8,
            "Questions Attempted": 1293989,
            "Logged In (%)": 46.2,
            "Remediation Instances": 3347,
            "Higher Level Instances": 2454
        },
        "classes": ["3", "4", "5", "6", "7", "8", "9", "10"],
        "class_accuracy": {"3": 80.7, "4": 73.8, "5": 71.7, "6": 67.2, "7": 67.1, "8": 66.7, "9": 66.3, "10": 68.2},
        "class_usage": {"3": 221.6, "4": 183.2, "5": 124.6, "6": 143.2, "7": 67.9, "8": 45.0, "9": 34.9, "10": 20.1},
        "top_performers": [
            {"Class": "3", "Sparkies": "Harshil Allamsetty", "Questions": "Charanjit Routhu"},
            {"Class": "5", "Sparkies": "Hema Vasudha", "Questions": "Hema Vasudha"},
            {"Class": "10", "Sparkies": "Sampath Saicharan", "Questions": "Sampath Saicharan"}
        ]
    },
    "Silver Oaks International School Kommadi": {
        "metrics": {
            "Students": 257,
            "Avg Usage (mins/week)": 22.2,
            "Accuracy (%)": 71.7,
            "Questions Attempted": 215807,
            "Logged In (%)": 72.4,
            "Remediation Instances": 379,
            "Higher Level Instances": 370
        },
        "classes": ["3", "4", "5", "6", "7", "8", "9"],
        "class_accuracy": {"3": 80.8, "4": 67.3, "5": 69.0, "6": 69.1, "7": 63.5, "8": 57.8, "9": 0},
        "class_usage": {"3": 41.6, "4": 47.7, "5": 24.9, "6": 24.2, "7": 18.7, "8": 11.1, "9": 0},
        "top_performers": [
            {"Class": "3", "Sparkies": "Mitranshu Kumar Palo", "Questions": "Mitranshu Kumar Palo"},
            {"Class": "6", "Sparkies": "Lakshmi Nikshita Doddi", "Questions": "Lakshmi Nikshita Doddi"},
            {"Class": "8", "Sparkies": "Vedansh Gadam", "Questions": "Vedansh Gadam"}
        ]
    }
}

# Sidebar - School Selection
st.sidebar.title("Navigation")
selected_school = st.sidebar.selectbox("Select School", list(SCHOOLS_DATA.keys()))
data = SCHOOLS_DATA[selected_school]

# Header
st.title(f"📊 {selected_school}")
st.subheader(f"Academic Year 2025 | Report Duration: June 2025 - March 2026")

# --- SECTION 1: OVERALL METRICS ---
st.markdown("---")
cols = st.columns(5)
metrics = data["metrics"]
cols[0].metric("Registered Students", metrics["Students"])
cols[1].metric("Avg Usage (mins/week)", f"{metrics['Avg Usage (mins/week)']}m")
cols[2].metric("Overall Accuracy", f"{metrics['Accuracy (%)']}%")
cols[3].metric("Total Questions", f"{metrics['Questions Attempted']:,}")
cols[4].metric("Login Rate", f"{metrics['Logged In (%)']}%")

# --- SECTION 2: CLASS-WISE PERFORMANCE ---
st.header("Class-wise Learning Insights")
col_chart1, col_chart2 = st.columns(2)

# Usage Chart
df_usage = pd.DataFrame(list(data["class_usage"].items()), columns=["Class", "Mins/Month"])
fig_usage = px.bar(df_usage, x="Class", y="Mins/Month", title="Average Usage per Month (mins)", color_discrete_sequence=['#3498db'])
col_chart1.plotly_chart(fig_usage, use_container_width=True)

# Accuracy Chart
df_acc = pd.DataFrame(list(data["class_accuracy"].items()), columns=["Class", "Accuracy %"])
fig_acc = px.bar(df_acc, x="Class", y="Accuracy %", title="Average Math Accuracy (%)", color_discrete_sequence=['#2ecc71'])
col_chart2.plotly_chart(fig_acc, use_container_width=True)

# --- SECTION 3: REMEDIATION & HIGHER LEVELS ---
st.header("Personalized Learning Tracks")
col_rem, col_high = st.columns(2)

with col_rem:
    st.info(f"**Total Remediation Instances:** {metrics['Remediation Instances']}")
    st.write("Remedials provide scaffolding to address knowledge gaps[cite: 188].")

with col_high:
    st.success(f"**Total Higher Level Instances:** {metrics['Higher Level Instances']}")
    st.write("Advanced content challenges students to think critically[cite: 200].")

# --- SECTION 4: HALL OF FAME ---
st.header("🏆 Celebrating Achievements")
st.table(pd.DataFrame(data["top_performers"]))

# --- SECTION 5: BEST PRACTICES ---
with st.expander("Recommended Best Practices for Teachers"):
    st.markdown("""
    * **Time Allocation:** At least 60 minutes of usage per student per week[cite: 225].
    * **Lab Environment:** Use a school laboratory under teacher supervision for best results[cite: 223].
    * **Active Topics:** Maintain no more than 3-4 active topics to ensure focus[cite: 233].
    * **Intervention:** Step in if accuracy is low on the first attempt or topic progress stalls [cite: 243-247].
    """)

st.sidebar.markdown("---")
st.sidebar.caption("Data Source: Ei Mindspark Learning Reports 2025-26")