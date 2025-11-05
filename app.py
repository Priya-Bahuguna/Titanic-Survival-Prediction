import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open('titanic_model.pkl', 'rb'))

st.set_page_config(page_title="Titanic Survival Prediction", page_icon="🚢")
st.title("🚢 Titanic Survival Prediction App")

# Sidebar inputs
st.sidebar.header("Passenger Information")

pclass = st.sidebar.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
sex = st.sidebar.selectbox("Sex", ["male", "female"])
age = st.sidebar.slider("Age", 1, 80, 25)
sibsp = st.sidebar.slider("Siblings/Spouses Aboard", 0, 8, 0)
parch = st.sidebar.slider("Parents/Children Aboard", 0, 6, 0)
fare = st.sidebar.number_input("Ticket Fare", min_value=0.0, value=32.2)
embarked = st.sidebar.selectbox("Port of Embarkation", ["C", "Q", "S"])

# Convert categorical to numeric
sex = 1 if sex == "female" else 0
embarked_map = {'C': 0, 'Q': 1, 'S': 2}
embarked = embarked_map[embarked]

# Predict
input_data = pd.DataFrame({
    'Pclass': [pclass],
    'Sex': [sex],
    'Age': [age],
    'SibSp': [sibsp],
    'Parch': [parch],
    'Fare': [fare],
    'Embarked': [embarked]
})

prediction = model.predict(input_data)[0]

# Output
if st.button("Predict Survival"):
    if prediction == 1:
        st.success("🎉 The passenger SURVIVED!")
    else:
        st.error("💀 The passenger did not survive.")

