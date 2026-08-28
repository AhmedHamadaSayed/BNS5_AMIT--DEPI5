import pandas as pd


def read_data_file(file_path)->pd.DataFrame:
    """
    Read a CSV file and return it as a pandas DataFrame.

    Parameters:
        file_path: The path of the CSV file.

    """
    try:
        df = pd.read_csv(file_path)
        return df

    except FileNotFoundError:
        print("File not found")

    except Exception as e:
        print(f"Error reading file: {e}")





def drop_unnecessary_features(
    df: pd.DataFrame,
    drop_cols: list[str]
) -> pd.DataFrame:

    '''This function drops columns and returns a DataFrame.'''

    return df.drop(columns=drop_cols)



def check_data_type(df: pd.DataFrame) -> pd.DataFrame:

    '''Check the data type and number of unique values for each column.'''

    dtypes = df.dtypes
    n_unique = df.nunique()

    return pd.DataFrame({
        "Dtypes": dtypes,
        "Num_unique": n_unique
    }).T


