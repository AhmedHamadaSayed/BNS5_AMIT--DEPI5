def summary(df):
    print("Shape:", df.shape)
    print("\nData Types:")
    print(df.dtypes)
    print("\nUnique Values:")
    print(df.nunique())


from sklearn.preprocessing import MinMaxScaler


def scale_numerical_data(x, numerical_columns):
    scaler = MinMaxScaler()

    x[numerical_columns] = scaler.fit_transform(
        x[numerical_columns]
    )

    return x   




import category_encoders as ce


def encode_categorical_data(x, categorical_columns):
    encoder = ce.OneHotEncoder(
        cols=categorical_columns,
        use_cat_names=True
    )

    x_encoded = encoder.fit_transform(x)

    return x_encoded


