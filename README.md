
# Titanic Survival Prediction

This repository contains a machine learning project to predict passenger survival on the famous Titanic shipwreck dataset. Built using Python, it includes exploratory data analysis (EDA), feature engineering, model training and deployment via a simple web app.

---

## 🧭 Project Overview

**Objective:**  
Predict whether a given passenger on the Titanic survived or not, based on features such as age, sex, passenger class, etc.

**Why this dataset?**  
The famous Kaggle “Titanic – Machine Learning from Disaster” dataset is a great beginner-friendly dataset for learning classification, data cleaning, feature engineering and model evaluation.

**What this repo contains:**

- `train.csv` & `test.csv`: The original Titanic dataset splits.  
- `Titanic_prediction_model.ipynb`: Jupyter notebook with full EDA, cleaning, feature creation, model selection, evaluation and saving the final model.  
- `titanic_model.pkl`: Serialized (pickle) version of the trained model for deployment.  
- `app.py`: A simple web app script (Flask/Streamlit or whichever you used) to load the model and provide a user-interface for predictions.  
- `requirements.txt`: The list of Python dependencies.  
- `submission.csv`: Sample submission or output predictions (if used for a competition).  
- README.md: This document.

---

## 🛠️ Setup & Usage

### Prerequisites  
- Python 3.x  
- pip (Python package installer)  

### Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Priya-Bahuguna/Titanic-Survival-Prediction.git
   cd Titanic-Survival-Prediction


2. Install dependencies:
```
pip install -r requirements.txt
```
Running the Project
---
To explore the notebook:
Open Titanic_prediction_model.ipynb in Jupyter or VSCode and step through the analysis, cleaning, modeling, evaluation and saving of the model.

To deploy via the app:
```
python app.py
```
📊 Model & Evaluation
--
Missing value handling (Age, Cabin, Embarked)

Feature engineering (titles, family size, etc.)

Algorithms tested: Logistic Regression, Random Forest, XGBoost

Metrics used: Accuracy, Precision, Recall, F1-Score

Best model: Random Forest (~[add your accuracy]% on test data)
## 🧾 File Structure
---
<img src="https://github.com/user-attachments/assets/c853f943-2a08-4dc3-83ce-5aca59206eaa" alt="App Screenshot" width="480" height="295">

## 📸 Screenshots
---
<img src="https://github.com/user-attachments/assets/b9f2eadb-6a48-43ab-bdb4-f7cf6ba52ec0" alt="App Screenshot" width="800">


📚 References
--
Kaggle Titanic dataset

Python libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, Streamlit/Flask

