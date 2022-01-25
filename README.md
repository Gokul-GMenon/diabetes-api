# Diabetes-api
- This was a flask based API done for HACKFORTOMORROW hackathon.
- The model was done using scikit-learn library (polynomial regression model).
- The api was done in flask and hosted on heroku.

## Making it work
The POST request format is shown below:

{
  "input":  ["Glucode", "BloodPressure", "BMI", "DiabetesPedigreeFunction", "Age"]
}

- An example is shown below:

{
  "input":  [183, 64, 23.3, 0.672, 31]
}

- Send the request to: https://diabetes-api-app.herokuapp.com/predict/
- The response should be:
{
  "result: 1               // (or 0)
}
