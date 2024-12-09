def blight_model():
    import pandas as pd
    import numpy as np

    train_dt = pd.read_csv('train.csv', engine='python')

    test_dt = pd.read_csv('readonly/test.csv')
    address_dt = pd.read_csv("readonly/addresses.csv", engine='python')
    lat_dt = pd.read_csv("readonly/latlons.csv", engine='python')

    my_list_train = train_dt.columns.values.tolist()
    my_list_test = test_dt.columns.values.tolist()

    train_dt = train_dt[train_dt.country == 'USA']
    train_dt = train_dt[(train_dt['compliance'] == 0) | (train_dt['compliance'] == 1)]
    test_dt = test_dt[test_dt.country == 'USA']

    y_train = train_dt['compliance']
    X_train = train_dt[['violation_street_number', 'fine_amount', 'late_fee', 'discount_amount']]

    X_test = test_dt[['violation_street_number', 'fine_amount', 'late_fee', 'discount_amount']]

    from sklearn import tree
    from sklearn.metrics import accuracy_score
    y_train.head()
    X_train.head()
    model = tree.DecisionTreeClassifier()
    clf = model.fit(X_train, y_train)
    y_train_model = model.predict(X_train)

    result = pd.concat([test_dt, X_test], axis=1)
    output = result.set_index('ticket_id')['prob']
    return output

blight_model()