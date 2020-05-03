3. AB Test
- problem
```
Your company is running a test that is designed to compare two different versions of the company’s website.

Version A of the website is shown to 60% of users, while version B of the website is shown to the remaining 40%. The test shows that 8% of users who are presented with version A sign up for the company’s services, as compared to 4% of users who are presented with version B.

If a user signs up for the company’s services, what is the probability that she/he was presented with version A of the website?
```
- solution
```
75%
bayes theorem : P(A|S)=P(S|A)\*P(A)/P(S)
P(S|A)=0.08
P(A)=0.6
P(S)=0.6\*0.08+0.4\*0.04=0.064
ans=0.08\*0.6/0.064
```
4. Login Table
- problem
```
A company stores login data and password hashes in two different containers:

DataFrame with columns: Id, Login, Verified.
Two-dimensional NumPy array where each element is an array that contains: Id and Password.
Elements on the same row/index have the same Id.

Implement the function login_table that accepts these two containers and modifies id_name_verified DataFrame in-place, so that:

The Verified column should be removed.
The password from NumPy array should be added as the last column with the name "Password" to DataFrame.
For example, the following code snippet:

id_name_verified = pd.DataFrame([[1, "JohnDoe", True], [2, "AnnFranklin", False]], columns=["Id", "Login", "Verified"])
id_password = np.array([[1, 987340123], [2, 187031122]], np.int32)
login_table(id_name_verified, id_password)
print(id_name_verified)
Should print:

   Id        Login   Password
0   1      JohnDoe  987340123
1   2  AnnFranklin  187031122
```
- solution
```python
import pandas as pd
import numpy as np

def login_table(id_name_verified, id_password):
    """
    :param id_name_verified: (DataFrame) DataFrame with columns: Id, Login, Verified.
    :param id_password: (numpy.array) Two-dimensional NumPy array where each element
                        is an array that contains: Id and Password
    :returns: (None) The function should modify id_name_verified DataFrame in-place.
              It should not return anything.
    """
    df=pd.DataFrame(id_password, columns=[['Id', 'Password']])
    id_name_verified['Password']=df[['Password']]
    del id_name_verified['Verified'] # id_name_verified.drop('Verified', axis=1, inplace=True)

id_name_verified = pd.DataFrame([[1, "JohnDoe", True], [2, "AnnFranklin", False]], columns=["Id", "Login", "Verified"])
id_password = np.array([[1, 987340123], [2, 187031122]], np.int32)
login_table(id_name_verified, id_password)
print(id_name_verified)
```
5. Iris Classifier
- problem
```
As a part of an application for iris enthusiasts, implement the train_and_predict function which should be able to classify three types of irises based on four features.

The train_and_predict function accepts three parameters:

train_input_features - a two-dimensional NumPy array where each element is an array that contains: sepal length, sepal width, petal length, and petal width.
train_outputs - a one-dimensional NumPy array where each element is a number representing the species of iris which is described in the same row of train_input_features. 0 represents Iris setosa, 1 represents Iris versicolor, and 2 represents Iris virginica.
prediction_features - two-dimensional NumPy array where each element is an array that contains: sepal length, sepal width, petal length, and petal width.
The function should train a classifier using train_input_features as input data and train_outputs as the expected result. After that, the function should use the trained classifier to predict labels for prediction_features and return them as an iterable (like list or numpy.ndarray). The nth position in the result should be the classification of the nth row of the prediction_features parameter.
```
- solution
```python
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

def train_and_predict(train_input_features, train_outputs, prediction_features):
    """
    :param train_input_features: (numpy.array) A two-dimensional NumPy array where each element
                        is an array that contains: sepal length, sepal width, petal length, and petal width
    :param train_outputs: (numpy.array) A one-dimensional NumPy array where each element
                        is a number representing the species of iris which is described in
                        the same row of train_input_features. 0 represents Iris setosa,
                        1 represents Iris versicolor, and 2 represents Iris virginica.
    :param prediction_features: (numpy.array) A two-dimensional NumPy array where each element
                        is an array that contains: sepal length, sepal width, petal length, and petal width
    :returns: (list) The function should return an iterable (like list or numpy.ndarray) of the predicted
                        iris species, one for each item in prediction_features
    """
    lr=LogisticRegression(solver='liblinear', random_state=1)
    lr.fit(train_input_features, train_outputs)
    test_pred=lr.predict(prediction_features)
    return test_pred

iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                                    test_size=0.3, random_state=0)

y_pred = train_and_predict(X_train, y_train, X_test)
if y_pred is not None:
    print(metrics.accuracy_score(y_test, y_pred))
```
6. Dog Classification
- problem
```
The following .csv file contains the data from a classifier model that predicts if an image contains a dog: predictions.csv 

The first column contains information if the dog is in the image or not. The second column contains the classifier prediction, which is in the interval 0-100, with higher values meaning that the classifier is more confident that image contains a dog.

What is the value of the decision boundary that will maximize the accuracy of the model? Values greater than or equal to the decision boundary will be treated as positive.
```
- solution
51
```python
def get_accuracy(y_scores, true_value, boundary):
    ans=0
    for i in range(len(y_scores)):
        if y_scores[i]>=boundary and true_value[i]==1:
            ans+=1
        elif y_scores[i]<boundary and true_value[i]==0:
            ans+=1
    return ans/len(y_scores)
graph=[]
for i in range(100):
    graph.append(get_accuracy(file['Classifier prediction'], file['Dog is on image'], i))
import matplotlib.pyplot as plt
plt.plot(graph, 'o')
plt.show()
print(graph.index(max(graph)))
```
7. Marketing Costs
- problem
```
Implement the desired_marketing_expenditure function, which returns the required amount of money that needs to be invested in a new marketing campaign to sell the desired number of units.

Use the data from previous marketing campaigns to evaluate how the number of units sold grows linearly as the amount of money invested increases.

For example, for the desired number of 60,000 units sold and previous campaign data from the table below, the function should return the float 250,000.

Previous campaigns

CAMPAIGN	MARKETING EXPENDITURE	UNITS SOLD
#1	300,000	60,000
#2	200,000	50,000
#3	400,000	90,000
#4	300,000	80,000
#5	100,000	30,000
```
- solution
```python
import numpy as np
from sklearn import linear_model

def desired_marketing_expenditure(marketing_expenditure, units_sold, desired_units_sold):
    """
    :param marketing_expenditure: (list) A list of integers with the expenditure for each previous campaign.
    :param units_sold: (list) A list of integers with the number of units sold for each previous campaign.
    :param desired_units_sold: (integer) Target number of units to sell in the new campaign.
    :returns: (float) Required amount of money to be invested.
    """
    units_sold=np.array(units_sold)
    marketing_expenditure=np.array(marketing_expenditure)
    reg=linear_model.LinearRegression().fit(marketing_expenditure.reshape(-1, 1), units_sold)

    ans=((desired_units_sold-reg.intercept_)/reg.coef_[0])
    return ans

#For example, with the parameters below, the function should return 250000.0
print(desired_marketing_expenditure(
    [300000, 200000, 400000, 300000, 100000],
    [60000, 50000, 90000, 80000, 30000],
    60000))
```
8. Stock Prices
- problem
```
You are given a list of tickers and their daily closing prices for a given period.

Implement the most_corr function that, when given each ticker's daily closing prices, returns the pair of tickers that are the most highly (linearly) correlated by daily percentage change.
```
- solution
```python
import pandas as pd
import numpy as np

def most_corr(prices):
    """
    :param prices: (pandas.DataFrame) A dataframe containing each ticker's 
                   daily closing prices.
    :returns: (container of strings) A container, containing the two tickers that 
              are the most highly (linearly) correlated by daily percentage change.
    """
    ans=get_top_abs_correlation(prices)
    #print(ans.axes[0])
    return ans.axes[0][0]
def get_redundant_pairs(df):
    pairs_to_drop=set()
    cols=df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop
def get_top_abs_correlation(df, n=1):
    au_corr=df.corr().abs().unstack()
    labels_to_drop=get_redundant_pairs(df)
    au_corr=au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]

#For example, the code below should print: ('FB', 'MSFT')
print(most_corr(pd.DataFrame.from_dict({
    'GOOG' : [
        742.66, 738.40, 738.22, 741.16,
        739.98, 747.28, 746.22, 741.80,
        745.33, 741.29, 742.83, 750.50
    ],
    'FB' : [
        108.40, 107.92, 109.64, 112.22,
        109.57, 113.82, 114.03, 112.24,
        114.68, 112.92, 113.28, 115.40
    ],
    'MSFT' : [
        55.40, 54.63, 54.98, 55.88,
        54.12, 59.16, 58.14, 55.97,
        61.20, 57.14, 56.62, 59.25
    ],
    'AAPL' : [
        106.00, 104.66, 104.87, 105.69,
        104.22, 110.16, 109.84, 108.86,
        110.14, 107.66, 108.08, 109.90
    ]
})))
```
