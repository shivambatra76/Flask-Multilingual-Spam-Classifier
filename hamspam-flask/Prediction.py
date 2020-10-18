import re 
import pickle
from sentence_transformers import SentenceTransformer
class Prediction:
    def __init__(self):
        print("Loading models")
        self.Encoder = SentenceTransformer('distiluse-base-multilingual-cased',device="cpu")
        ## load encoder 
        self.classifier = pickle.load(open("finalized_model.pkl", 'rb'))
        print("models loaded successfully")
    def preprocessing(self,text):
        """Changing text to lowercase ,removing extra spaces and cleaning the text.
        """
        text = text.lower().strip() 

        text = re.sub('[^a-zA-Z]',' ',text)

        text = re.sub(' +', ' ', text)
        return text
        
    def predict(self,input_string):
        data = str(input_string)
        text = self.preprocessing(data)
        encoded_text = self.Encoder.encode([text])
        
        if self.classifier.predict(encoded_text)[0]>0:
            return "Spam"
        else:
            return "Ham"
