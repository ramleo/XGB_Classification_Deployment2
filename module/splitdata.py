def data_split(data=None):
    '''Bifurcating features and target variable'''
    # Importing relevant packages
    from sklearn.model_selection import train_test_split
    X = data.drop('churn', axis=1)
    y = data['churn']

    # Splitting the dataset into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify = y, shuffle=True, random_state=7)

    return X_train.copy(),X_test.copy(),y_train.copy(),y_test.copy()