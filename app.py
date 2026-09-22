# AI-Based Student Academic Performance Predictor
# Author: Haris Maqsood Abbasi
# For: Open Doors Russia Scholarship 2026 - Computer Science Track

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from flask import Flask, request, render_template_string

# 1. Sample Dataset (Kaggle Student Performance se inspired)
data = {
    'attendance': [85, 90, 45, 75, 60, 95, 30, 80, 55, 88],
    'study_hours': [10, 15, 2, 8, 5, 18, 1, 12, 4, 14],
    'previous_marks': [78, 88, 40, 65, 55, 92, 35, 70, 50, 85],
    'assignment_score': [80, 90, 30, 70, 60, 95, 20, 75, 45, 88],
    'result': [1, 1, 0, 1, 0, 1, 0, 1, 0, 1] # 1=Pass, 0=Fail/Dropout
}
df = pd.DataFrame(data)

# 2. Model Training
X = df[['attendance', 'study_hours', 'previous_marks', 'assignment_score']]
y = df['result']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 3. Accuracy Check
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred) * 100
print(f"Model Accuracy: {accuracy:.2f}%")

# 4. Simple Flask Web App for Demo
app = Flask(__name__)

HTML_TEMPLATE = """
<h2>AI Student Performance Predictor</h2>
<p>Model Accuracy: {{accuracy}}%</p>
<form method="post">
  Attendance: <input type="number" name="attendance" required><br><br>
  Study Hours: <input type="number" name="study_hours" required><br><br>
  Previous Marks: <input type="number" name="previous_marks" required><br><br>
  Assignment Score: <input type="number" name="assignment_score" required><br><br>
  <input type="submit" value="Predict">
</form>
<h3>{{prediction}}</h3>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ""
    if request.method == 'POST':
        try:
            features = [[
                int(request.form['attendance']),
                int(request.form['study_hours']),
                int(request.form['previous_marks']),
                int(request.form['assignment_score'])
            ]]
            result = model.predict(features)[0]
            prediction = "Result: Student will PASS ✅" if result == 1 else "Result: Student at RISK of Dropout ❌"
        except Exception as e:
            prediction = f"Error: {e}"
    return render_template_string(HTML_TEMPLATE, prediction=prediction, accuracy=f"{accuracy:.2f}")

if __name__ == '__main__':
    app.run(debug=True)
