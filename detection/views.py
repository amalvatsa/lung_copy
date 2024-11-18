import os
import pickle
from django.conf import settings
from django.shortcuts import render, redirect
import numpy as np





# Define the path to the saved model
model_path = os.path.join(settings.BASE_DIR, 'detection/ml_models/voting_model.pkl')


# Load the model
with open(model_path, 'rb') as file:
    lung_cancer_model = pickle.load(file)

def homepage(request):
    """Serve the homepage."""
    return render(request, 'detection/webpage.html')

def predict_lung_cancer(input_data):
    # Predict based on input features
    prediction = lung_cancer_model.predict(np.array(input_data).reshape(1, -1))
    print(f"Model Prediction: {prediction}")  # Log the prediction result to check the value
    return prediction[0]  # Return the first element of the prediction

def lung_cancer_form(request):
    if request.method == 'POST':
        # Collect data from the form
        age = int(request.POST.get('age'))
        allergy = int(request.POST.get('allergy'))
        smoker = int(request.POST.get('smoker'))
        wheezing = int(request.POST.get('wheezing'))
        yellow_fingers = int(request.POST.get('yellow_fingers'))
        alcohol_consumer = int(request.POST.get('alcohol_consumer'))
        anxiety = int(request.POST.get('anxiety'))
        coughing = int(request.POST.get('coughing'))
        peer_pressure = int(request.POST.get('peer_pressure'))
        chest_pain = int(request.POST.get('chestPain'))

        # Prepare input data for the model (ensure the order matches the training data)
        input_data = np.array([[age, allergy, smoker, wheezing, yellow_fingers, 
                                alcohol_consumer, anxiety, coughing, peer_pressure, chest_pain]])



        # Make prediction using the predict_lung_cancer function
        prediction = predict_lung_cancer(input_data)  # Use the function here
        print(f"Processed Input Data: {input_data}")  # Debugging input data
        print(f"Final Prediction: {prediction}")  # Debugging prediction

        # Redirect to result page with the prediction
        return redirect('result', result=prediction)

    return render(request, 'detection/lung-cancer-form.html')

def result_page(request, result):
    """Display the prediction result."""
    # Convert the result (which might be a number or a string) into a readable message
    if str(result) == '1':  # Ensure comparison is done as string
        result_message = "Positive for Lung Cancer"
    else:
        result_message = "Negative for Lung Cancer"

    # Render the result page and pass the result to the template
    return render(request, 'detection/result.html', {'result_message': result_message})