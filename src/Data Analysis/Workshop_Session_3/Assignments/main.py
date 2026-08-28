from Preprocessing import (
    read_data_file,
    drop_unnecessary_features,
    check_data_type
)



from Config.config import DROP_COLUMNS


file_path = input ("Enter the CSV file path :")

df = read_data_file(file_path)

df = drop_unnecessary_features(df , DROP_COLUMNS)

result = check_data_type(df)

print(result)
