import pandas as pd
from config.config import DROP_COLUMNS
def summary(df:pd.DataFrame)-> pd.DataFrame:
    dtypes = df.dtypes
    n_uniq = df.nunique()
    return  pd.DataFrame({"Dtypes: ": dtypes,"Num_uniqe:" : n_uniq}).T




def drop_cols(df: pd.DataFrame, cols : list[str])-> pd.DataFrame:
    '''Drop specific cols from df  '''
    return df.drop(columns = cols)