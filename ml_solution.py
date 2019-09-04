from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error

from sklearn import model_selection
# from sklearn import
import pandas as pd
import numpy as np
import feature_engineering


test, train = feature_engineering.main()

# print(train.head(5))

sc_x = MinMaxScaler()
sc_y = MinMaxScaler()

X = train.drop(['Item_Outlet_Sales','Item_Identifier'],axis=1)
Y = train['Item_Outlet_Sales']

X[['Item_Weight','Item_MRP','Outlet_Establishment_Year']] = sc_x.fit_transform(X[['Item_Weight','Item_MRP','Outlet_Establishment_Year']])

X_dummy = pd.get_dummies(X[['Outlet_Size','Outlet_Identifier','Outlet_Type']])
X = pd.concat([X,X_dummy],axis=1)
X = X.drop(['Outlet_Size','Outlet_Identifier','Outlet_Type'], axis=1)
# print(X.head(5))

x_train, x_validation, y_train, y_validation = model_selection.train_test_split(X,Y,test_size=0.2,random_state=51)

model = LinearRegression()

model.fit(x_train, y_train)
#
y_pridict = model.predict(x_validation)

# Perform cross-validation:
cv_score = model_selection.cross_val_score(model, x_train, y_train, cv=20,error_score='raise')
# cv_score = np.sqrt(np.abs(cv_score))
print(cv_score)
print(type(cv_score))

cv_score_p = model_selection.cross_val_predict(model, x_train, y_train, cv=20)
# cv_score = np.sqrt(np.abs(cv_score))
print(cv_score_p)
print(type(cv_score_p))

# Print model report:
print("\nModel Report")
# print("RMSE : %.4g" % np.sqrt(model.mean_squared_error(dtrain[target].values, dtrain_predictions)))
print("CV Score : Mean - %.4g | Std - %.4g | Min - %.4g | Max - %.4g" % (np.mean(list(cv_score)),
                                                                         np.std(cv_score),
                                                                         np.min(cv_score), np.max(cv_score)))

accuracy = mean_squared_error(y_validation, y_pridict)
accuracy = np.sqrt(accuracy)
print(accuracy)


# print(test)