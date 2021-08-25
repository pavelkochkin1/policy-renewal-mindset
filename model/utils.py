import pandas as pd

class DataPreprocessing():
    def __init__(self, to_numeric=False):
        self.to_numeric = to_numeric
    
    def fit(self, X: pd.DataFrame(), Y = None):
        return self
    
    def transform(self, X: pd.DataFrame(), Y = None) -> pd.DataFrame:
        try:
            to_drop = ['DATA_TYPE', 'VEHICLE_MAKE', 'VEHICLE_MODEL', 'POLICY_INTERMEDIARY',
                        'POLICY_PRV_CLM_GLT_N', 'POLICY_COURT_SIGN', 'CLAIM_AVG_ACC_ST_PRD',
                        'CLIENT_REGISTRATION_REGION']

            new_data = X.copy()
            new_data.drop(labels=to_drop, inplace=True, axis=1, errors='ignore')

            if self.to_numeric:
                # POLICY_BRANCH
                new_data['POLICY_BRANCH'] = new_data['POLICY_BRANCH'].replace({'Москва':1, 'Санкт-Петербург':0})
                # INSURER_GENDER
                new_data['INSURER_GENDER'] = new_data['INSURER_GENDER'].replace({'F':0, 'M':1})
                # POLICY_CLM_N
                new_data['POLICY_CLM_N'] = new_data['POLICY_CLM_N'].replace({'0':0, '1L':1, '1S':2, 
                                                                             '2':3, '3':4, '4+':5, 'n/d':6})
                # POLICY_CLM_GLT_N
                new_data['POLICY_CLM_GLT_N'] = new_data['POLICY_CLM_GLT_N'].replace({'0':0, '1L':1, '1S':2, '2':3, 
                                                                                     '3':4, '4+':5, 'n/d':6})
                # POLICY_PRV_CLM_N
                new_data['POLICY_PRV_CLM_N'] = new_data['POLICY_PRV_CLM_N'].replace({'0':0, '1L':1, '1S':2, '2':3, 
                                                                                     '3':4, '4+':5, 'N':6})
                # POLICY_YEARS_RENEWED_N
                new_data['POLICY_YEARS_RENEWED_N'] = new_data['POLICY_YEARS_RENEWED_N']. \
                                                    replace({'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6,
                                                            '7':7, '8':8, '9':9, '10':10, 'N':11})
        
            return new_data
        except Exception as err:
            print('DataPreprocessing.transform(): {}'.format(err))
        return X

    def fit_transform(self, X: pd.DataFrame, Y = None):
        self.fit(X)
        return self.transform(X)
                    