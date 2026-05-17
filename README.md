# Diabetes Prediction 🩺

## Project Description
This project is an end-to-end Machine Learning Pipeline developed as part of the MLOps SP26 Assignment at Quaid-i-Azam University. It covers everything from data preprocessing and exploratory data analysis (EDA) to model training, evaluation, and finally deploying the best-performing model as a RESTful API using FastAPI. The goal is to accurately predict the likelihood of diabetes in patients based on their medical diagnostic measurements.

**Author:** Haris

## 🛠️ Setup Instructions

Follow these steps to set up the project locally:

1. **Clone the repository:**
   git clone <your-github-repo-link>
   cd MLOPS_ASSIGNMENT_1

2. Create a Virtual Environment:For Windows:
python -m venv venv
.\venv\Scripts\activate

For Linux/Mac:
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies:
pip install -r requirements.txt

🚀 How to Run the FastAPI Server
Once the dependencies are installed and the virtual environment is active, start the FastAPI server by running:
uvicorn app:app --reload

The API will be available at http://localhost:8000. You can also view the interactive automatic API documentation (Swagger UI) at http://localhost:8000/docs.

📊 Model Performance Comparison
Here is the performance comparison of the different classification models evaluated during the training phase on the test dataset (30% split):

## 📊 Model Performance Comparison

Here is the performance comparison of the different classification models evaluated during the training phase on the test dataset (30% split):

| Model                      | Accuracy | Precision | Recall   | F1-Score |
|----------------------------|----------|-----------|----------|----------|
| Logistic Regression        | 0.943894 | 0.939275  | 0.943894 | 0.939760 |
| Support Vector Machine (SVM)| 0.848185 | 0.719417  | 0.848185 | 0.778512 |
| Decision Tree Classifier   | 0.986799 | 0.986781  | 0.986799 | 0.986668 |
| Random Forest Classifier   | 0.980198 | 0.980357  | 0.980198 | 0.979331 |
| K-Nearest Neighbors (KNN)  | 0.933993 | 0.939510  | 0.933993 | 0.935741 |

(Note: Based on the evaluation, the Decision Tree model achieved the highest accuracy of ~98.6% and was saved as `diabetes_model.pkl` for deployment in the FastAPI application.)


💻 Example cURL Commands
You can test the API using the following cURL commands in a separate terminal:

Test 1 - Successful prediction (diabetic):
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d "{\"age\": 65, \"urea\": 7.5, \"cr\": 52.0, \"hba1c\": 11.2, \"chol\": 6.1, \"tg\": 2.8, \"hdl\": 0.9, \"ldl\": 3.5, \"vldl\": 1.2, \"bmi\": 32.5, \"gender\": \"M\"}"

Test 2 - Successful prediction (non-diabetic):
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d "{\"age\": 28, \"urea\": 4.2, \"cr\": 48.0, \"hba1c\": 5.1, \"chol\": 4.0, \"tg\": 1.2, \"hdl\": 1.8, \"ldl\": 2.1, \"vldl\": 0.6, \"bmi\": 22.0, \"gender\": \"F\"}"

Test 3 - Validation error (invalid gender):
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d "{\"age\": 45, \"urea\": 5.0, \"cr\": 50.0, \"hba1c\": 6.0, \"chol\": 5.0, \"tg\": 1.5, \"hdl\": 1.2, \"ldl\": 2.5, \"vldl\": 0.8, \"bmi\": 25.0, \"gender\": \"X\"}"

Test 4 - Missing field error:
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d "{\"age\": 50, \"urea\": 5.0, \"cr\": 50.0}"


📸 Screenshots of API Responses
Screenshots demonstrating the API responses for the above cURL commands have been saved in the screenshots/ directory of this repository.

![alt text](image.png)

![alt text](image-1.png)

![alt text](image-2.png)

![alt text](image-3.png)