# Heart_disease-Prediction

Project Summary
The goal of this project is to build a predictive model that can classify whether a patient is likely to have heart disease. It's an end-to-end project that starts with raw data, builds a machine learning model, and finally, presents it in an easy-to-use web interface.

The Data (heart_disease_data.csv): The project uses a medical dataset containing patient information. Key features include age, sex, chest pain type (cp), resting blood pressure (trestbps), cholesterol (chol), and other medical indicators. The target column is the key, where 1 signifies the presence of heart disease and 0 signifies its absence.
The Model (heart_disease.ipynb): This Jupyter Notebook is where the core machine learning work is done.
It begins by loading and exploring the dataset to understand its structure.
The data is then split into features (the medical attributes) and the target (the heart disease diagnosis).
A Logistic Regression model, a reliable algorithm for binary classification, is trained on this data. The model learns the patterns in the patient data that are most indicative of heart disease.
Finally, the model's performance is evaluated by checking its accuracy on unseen test data.
The Web Application (app.py): This Python script uses the Streamlit library to create a simple and interactive web page.
It provides a user-friendly form where a user can input their own medical details, such as age, sex, cholesterol levels, etc.
When the user clicks the "Predict" button, the application is designed to take these inputs and use the trained model to generate a prediction about the user's heart disease risk.

Project Flowchart
This flowchart illustrates the project's complete workflow, from the initial model training to the final prediction in the web application.

1. Model Training (heart_disease.ipynb)
This is the development phase where the predictive model is built and validated.

Flow:

Start 🎬

Load Dataset: The process starts by loading the heart_disease_data.csv file.
Separate Features and Target: The data is divided into input features (X), like age and blood pressure, and the output target (y), which is the heart disease diagnosis.
Split Data: The dataset is split into a training set (for teaching the model) and a testing set (for evaluating it)
Train the Model: A Logistic Regression model is trained on the training data.
Evaluate Performance: The model's accuracy is tested on the unseen test data to see how well it performs.
End of Training 🏆

2. Prediction Workflow (app.py)
This is the deployment phase where the trained model is used in a web application to make live predictions.
Flow:

Start App 🚀

User Enters Medical Data: A user interacts with the Streamlit web interface and enters their personal health information.
Load the Trained Model: The application loads the pre-trained Logistic Regression model.
Make a Prediction: The model uses the user's input data to predict the likelihood of heart disease.
Display the Result: The prediction is shown to the user on the web page, indicating whether they are at high or low risk for heart disease.

End 🎉
