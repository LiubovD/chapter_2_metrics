from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score,confusion_matrix
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score

# get data
df = pd.read_csv("dataset_09_26.csv")


# create our sklearn data

x = df.drop(['OID_', 'ID_upd', 'TreeMrt2ct', 'TreeMrt3ct', 'TreeMort_3', 'cnsrv_prcn', 'prcnt_fore',
             ],axis=1)
y = df['TreeMrt3ct']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

clf_rf = RandomForestClassifier(n_estimators=1000, criterion='gini',   min_samples_leaf= 10, random_state=1)
clr_rf = clf_rf.fit(x_train,y_train)
ac = accuracy_score(y_test,clf_rf.predict(x_test))
print('Accuracy is: ',ac)
cm = confusion_matrix(y_test,clf_rf.predict(x_test))
sns.heatmap(cm,annot=True,fmt="d")
plt.show()


# do the 5-fold cross validation
scores = cross_val_score(clr_rf, x, y, cv=5)
print("Fold Accuracies: {}".format(scores))
print("XV Accuracy: {:3.2f}".format(scores.mean()))

# import seaborn as sns
# sns.set()
# sns.pairplot(df, hue='TrMrt_2ct', height=3, vars=['def_index', 'CC_FRCP_p'])

# Train results: evaluate the model on the testing set of data
y_train_model = clf_rf.predict(x_train)
print("Train Accuracy: {:3.2f}".format(accuracy_score(y_train, y_train_model)))

# Test results: evaluate the model on the testing set of data
y_test_model = clf_rf.predict(x_test)
print("Test Accuracy: {:3.2f}".format(accuracy_score(y_test, y_test_model)))

#get importance
importance = clf_rf.feature_importances_
feature_names = x_train.columns
feature_names_importance = dict()

for i,v in enumerate(importance):
    feature_names_importance.update({feature_names[i]: v})
    #print('Feature: %0d, Score %.5f' % (i,v))
print(feature_names_importance)
print('/n')
sorted_list_var = sorted(feature_names_importance.items(), key=lambda item: item[1], reverse=True)
for i, v in sorted_list_var:
    print(i, v)

# param_grid =     {
#     "n_estimators": list(range(1,100)),
#     'criterion': ['entropy', 'gini']
#     }
# grid = GridSearchCV(clf_rf, param_grid, cv=5)
# grid.fit(x_train, y_train)
# print("Grid Search: best parameters: {}".format(grid.best_params_))
#
# # evaluate the best model
# best_model = grid.best_estimator_
# predict_y = best_model.predict(x_test)
# acc = accuracy_score(x_train, predict_y)
# lb, ub = classification_confint(acc, X.shape[0])
# print("Accuracy: {:3.2f} ({:3.2f},{:3.2f})".format(acc, lb, ub))