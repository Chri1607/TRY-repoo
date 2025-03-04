import pandas as pd

def feature_engineering(df: pd.DataFrame)-> pd.DataFrame:
    '''
    Feature engineering process for the North America file.
    
    Arguments:
    -> Df (pd.DataFrame)
    
    Outputs
    -> Df (pd.DataFrame)
    '''
    df_new = df.copy()
    df_new['Established'] = 2025-df_new.Established
    return df_new