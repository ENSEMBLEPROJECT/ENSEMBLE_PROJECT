import pandas as pd
def load_and_describe_datasets(x_train_path, y_train_path, x_test_path, y_random_path):
    # Load datasets
    x_train = pd.read_csv(x_train_path)
    y_train = pd.read_csv(y_train_path)
    x_test = pd.read_csv(x_test_path)
    y_random = pd.read_csv(y_random_path)

    # Describing the datasets to check for missing values
    dataframes_info = {
        'X_train': x_train.describe(include='all'),
        'Y_train': y_train.describe(include='all'),
        'X_test': x_test.describe(include='all'),
        'Y_random': y_random.describe(include='all')
    }

    # Outputting the descriptions
    for name, df_info in dataframes_info.items():
        print(f'{name} Summary:\n', df_info)
        print(f'{name} Missing Values:\n', df_info.isnull().sum())
