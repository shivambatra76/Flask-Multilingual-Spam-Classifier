## Multilingual -Flask-Deployment
This is the deploment of Multilingual Ham-Spam Classifier.
Demo Video - https://www.linkedin.com/posts/shivam-batra-34b63a17a_datascience-machinelearning-deeplearning-activity-6723524623419396096-uDcf

### Prerequisites
Please install all the modules from requirements.txt

### Project Structure
This project has four major parts :
1. Prediction.py - This contains code for our Machine Learning model to predict whether the text is Ham or Spam. It is using Mulitligual Embeding so we have support for more than 10 languages. The list of languages and data is shared in other repository.
2. main.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
3. request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
4. templates - This folder contains the HTML template to allow user to enter text and displays the predicted result.

### Running the project
1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python model.py
```
This would create a serialized version of our model into a file model.pkl

2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000/home
