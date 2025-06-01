# Heart-Disease-Prediction-Model

This is a web application built using **Streamlit** that predicts whether a person is **Healthy** or has a **Defected Heart**.
The prediction is powered by a **Logistic Regression** machine learning model trained on clinical parameters.

## Features

- Interactive UI using Streamlit
- Predicts heart disease likelihood based on user inputs
- Clear output: “You have heart disease” or “You do not have heart disease”
- Displays model accuracy and uses a logistic regression model behind the scene

## Machine Learning Model

- **Algorithm Used**: Logistic Regression
- **Training Accuracy**: 85.24%
- **Testing Accuracy**: 80.48%
- **Saved Model File**: `modelheart.joblib`

## Input Features Used for Prediction

The model uses the following **13 medical parameters**:

1. `age` - Age of the patient
2. `sex` - Sex (0 = female, 1 = male)
3. `cp` - Chest pain type (0, 1, 2, 3)
4. `trestbps` - Resting blood pressure (in mm Hg)
5. `chol` - Serum cholesterol in mg/dl
6. `fbs` - Fasting blood sugar > 120 mg/dl (0 = False, 1 = True)
7. `restecg` - Resting electrocardiographic results (0, 1, 2)
8. `thalach` - Maximum heart rate achieved
9. `exang` - Exercise-induced angina (0 = No, 1 = Yes)
10. `oldpeak` - ST depression induced by exercise relative to rest
11. `slope` - Slope of the peak exercise ST segment (0, 1, 2)
12. `ca` - Number of major vessels colored by fluoroscopy (0–3)
13. `thal` - Thalassemia (1 = normal, 2 = fixed defect, 3 = reversible defect)
## 🛠️ How to Run the App

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/heart-disease-predictor.git
cd heart-disease-predictor
