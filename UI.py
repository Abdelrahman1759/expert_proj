# filepath: c:\Users\co.magic\OneDrive - Alexandria National University\Desktop\expert_systems\UI.py
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from expert_system import Patient, HeartDiseaseRiskAssessment

# Set the page configuration
st.set_page_config(page_title="Expert Systems UI", page_icon=":heart:", layout="wide")

# Custom CSS for enhanced styling
st.markdown("""
    <style>
    /* Overall background */
    .reportview-container {
        background: #606c38;
    }
    .sidebar .sidebar-content {
        background: #283618;
    }
    /* Title styling */
    .main .block-container h1 {
        font-size: 2.5rem;
        color: #fefae0;
    }
    /* Button styling */
    .stButton>button {
        background-color: #dda15e;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-size: 1rem;
    }
    /* Section header styling */
    .section-header {
        color: #333;
        border-bottom: 2px solid #bc6c25;
        padding-bottom: 0.2rem;
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Title of the app with a horizontal line for separation
st.title("Heart Disease Risk Assessment Expert System")
st.markdown("<hr>", unsafe_allow_html=True)

# Sidebar for input widgets with header styling
st.sidebar.header("Input Your Health Data")

# Input widgets
age = st.sidebar.number_input("Enter age", min_value=0, max_value=120, step=1, value=30)
cholesterol = st.sidebar.number_input("Enter cholesterol level", min_value=0, max_value=500, step=1, value=180)
blood_pressure = st.sidebar.number_input("Enter blood pressure", min_value=0, max_value=300, step=1, value=120)
smoking = st.sidebar.selectbox("Do you smoke?", ["yes", "no"], index=1)
exercise = st.sidebar.selectbox("Do you exercise regularly?", ["yes", "no"], index=0)
bmi = st.sidebar.number_input("Enter BMI", min_value=0.0, max_value=100.0, step=0.1, value=22.0)

# Container for Expert System Output and Visualizations
if st.sidebar.button("Run Expert System"):
    # Create an instance of the expert system
    engine = HeartDiseaseRiskAssessment()
    engine.reset()  # Reset the engine to clear previous facts

    # Declare the facts based on user input
    engine.declare(Patient(age=age, cholesterol=cholesterol, blood_pressure=blood_pressure,
                           smoking=smoking, exercise=exercise, bmi=bmi))
    engine.run()  # Run the engine to infer the risk

    # Display the result in a dedicated section
    st.markdown("<h2 class='section-header'>Expert System Result</h2>", unsafe_allow_html=True)
    result = engine.get_result()
    st.write(result)

    # Display the probability of heart issues
    risk_score = engine.get_risk_score()
    probability = min(max(risk_score, 0), 100)  # Ensure the probability is between 0 and 100
    st.markdown("<h2 class='section-header'>Probability of Heart Issues</h2>", unsafe_allow_html=True)
    st.write(f"The probability of heart issues based on the input data is: **{probability}%**")

    # Visualization Section
    st.markdown("<h2 class='section-header'>Health Data Visualization</h2>", unsafe_allow_html=True)
    
    # Prepare the data for visualization
    data = {
        'Age': age,
        'Cholesterol': cholesterol,
        'Blood Pressure': blood_pressure,
        'BMI': bmi
    }
    
    # Create two columns for side-by-side plots
    col1, col2 = st.columns(2)
    
    # Matplotlib Plot in the first column
    with col1:
        fig, ax = plt.subplots()
        colors = ['#FF6347', '#4682B4', '#8A2BE2', '#3CB371']
        ax.bar(data.keys(), data.values(), color=colors)
        ax.set_title('Health Data (Matplotlib)')
        ax.set_ylabel('Values')
        st.pyplot(fig)
    
    # Plotly Plot in the second column
    with col2:
        fig = px.bar(
            x=list(data.keys()), 
            y=list(data.values()), 
            labels={'x': 'Health Metrics', 'y': 'Values'}, 
            title='Health Data (Plotly)', 
            color=list(data.values()), 
            color_continuous_scale='Viridis'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Additional Statistics Section
    st.markdown("<h2 class='section-header'>Additional Statistics</h2>", unsafe_allow_html=True)
    average = sum(data.values()) / len(data)
    maximum = max(data.values())
    minimum = min(data.values())
    st.write(f"**Average Value:** {average:.2f}")
    st.write(f"**Maximum Value:** {maximum}")
    st.write(f"**Minimum Value:** {minimum}")