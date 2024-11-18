from django.db import models

class Prediction(models.Model):
    # Fields for storing input data and prediction result
    age = models.IntegerField()
    smoking_status = models.IntegerField()
    result = models.CharField(max_length=50)  # To store prediction result like 'Positive' or 'Negative'
    created_at = models.DateTimeField(auto_now_add=True)  # To store when the prediction was made

    def __str__(self):
        return f"Prediction: {self.result} at {self.created_at}"