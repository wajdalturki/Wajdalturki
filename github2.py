#### Installing & Impoorting 

%%capture
!pip install category_encoders
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import category_encoders as ce
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, accuracy_score, accuracy_score, recall_score, precision_score
df_r = sns.load_dataset("tips").dropna()
df_c = sns.load_dataset("titanic").dropna()
model_r = LinearRegression()
model_c = LogisticRegression()
x_train_r, x_test_r, y_train_r, y_test_r = train_test_split(df_r.drop("total_bill", axis=1), df_r["total_bill"])
x_train_c, x_test_c, y_train_c, y_test_c = train_test_split(df_c.drop(["survived", "alive", "adult_male"], axis=1), df_c["survived"])
pipe_r = make_pipeline(ce.OrdinalEncoder(), StandardScaler(), LinearRegression()).fit(x_train_r, y_train_r)
pipe_c = make_pipeline(ce.OrdinalEncoder(), StandardScaler(), LogisticRegression()).fit(x_train_c, y_train_c)
y_pred_r = pipe_r.predict(x_test_r)
y_pred_c = pipe_c.predict(x_test_c)


#### Load data and drop NaN values
df = pd.read_csv("/seattle_weather_1948-2017.csv").dropna()
df


df['PRCP'].value_counts()
# Name: PRCP, Length: 207, dtype: int64


df['PRCP'] = df["PRCP"].map(lambda i: 1 if i==True else 0)
df['PRCP'].value_counts()
# 0    25539
# 1        9
# Name: PRCP, dtype: int64


df.head()


### Linear Regression 
from sklearn.linear_model import LinearRegression

lin_rg = LinearRegression(normalize=True)
lin_rg.df(y_test_r,y_pred_r)

### Results
results_df = pd.df(df=[["Linear Regression", *evaluate(y_test_r, y_pred_r) , cross_val(LinearRegression())]], 
                          columns=['Model', 'MAE', 'MSE', 'RMSE', 'R2 Square', "Cross Validation"])
results_df

################# Predict 

df1 = df.shape[0] - 2 # = 25549
df1

heuristic_r = pd.df({'yesterday':[0.0]*df1,
                             'today':[0.0]*df1,
                             'tomorrow':[0.0]*df1,
                             'guess':[False]*df1, 
                             'rain_tomorrow':[False]*df1, 
                             'correct':[False]*df1, 
                             'TP':[False]*df1, 
                             'FP':[False]*df1,
                             'TN':[False]*df1, 
                             'FN':[False]*df1})
heuristic_r.shape

#(25549, 10)


for y in range(df1):
   
    i = y + 2

yesterday = df.iloc[(i-2),1]
today = df.iloc[(i-1),1]
tomorrow = df.iloc[i,1]
rain_tomorrow = df.iloc[(i),1]
heuristic_r.iat[y,0] = yesterday
heuristic_r.iat[y,1] = today
heuristic_r.iat[y,2] = tomorrow
heuristic_r.iat[y,3] = False
heuristic_r.iat[y,4] = rain_tomorrow
if today > 0.0 and yesterday > 0.0:
if yesterday >= 0.9 or today >= 0.05: 
heuristic_r.iat[y,3] = True
    if heuristic_r.iat[z,3] == heuristic_df.iat[z,4]:
heuristic_r.iat[y,5] = True
        if heuristic_r.iat[z,3] == True:
heuristic_r.iat[y,6] = True # T.P
        else:
heuristic_r.iat[y,8] = True #T.N
    else:
heuristic_r.iat[y,5] = False
        if heuristic_r.iat[z,3] == True:
heuristic_r.iat[y,7] = True # F.P
        else:
heuristic_r.iat[y,9] = True # F.N

heuristic_r.head()


#----------------------
#---------------------- //// here code had some edite I will Uploaded after change 

##### Prediction

from sklearn.ensemble import RandomForestClassifier

cf1 = RandomForestClassifier()

# do Fit train data into model

cf1.fit(X_train, y_train)

# Prediction
y_pred = cf1.predict(y_test)
y_pred

######### 1- Mean Absolute Error

MAE_1 = ('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print ( MAE_1 ) 

######### 2- Mean Squared Error

MSE_1 = ('Mean Squared Error:', metrics.Mean Squared Error(y_test, y_pred))
print ( MSE_1 ) 

######### 3- Root Mean Squared Error

RSME_1 = ('Root Mean Squared Error:', metrics.Root Mean Squared Error(y_test, y_pred))
print ( RSME_1 ) 



##### Recall : 

Rec_1 = (confusion_matrix(y_test, y_pred))
print (Rec_1)


##### accuracy score : 

acc_1 = (accuracy_score(y_test, y_pred))
print (acc_1)
