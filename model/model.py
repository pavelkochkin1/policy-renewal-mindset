from joblib import load
import pandas as pd

THRESHOLD = 0.37 # calculated for my model 

class Predictor():
    def __init__(self, model_path: str):
        self.model = load(model_path)
    
    def predict(self, data: pd.DataFrame) -> pd.DataFrame:
        print('data shape:', data.shape)
        print('index shape:', data.index.shape)

        output = {'POLICY_ID': data.index.values, 'POLICY_IS_RENEWED': None, 'POLICY_IS_RENEWED_PROBABILITY': None}

        try: 
            prediction = self.model.predict_proba(data)[:,1]
            print('prediction shape:',prediction.shape)
            print('prediction is ready...')
            
            output['POLICY_IS_RENEWED'] = (prediction > THRESHOLD).astype(int)
            output['POLICY_IS_RENEWED_PROBABILITY'] = prediction

            output = pd.DataFrame(output)
            print('DataFrame is ready...')

            return output
        except Exception as err:
            print('Predictor.predict(): {}'.format(err))
        return data

    def __call__(self, data: pd.DataFrame):
        return self.predict(data)