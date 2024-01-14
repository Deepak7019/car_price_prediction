# Car price prediction using linear regression

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/yourproject.svg)](https://github.com/yourusername/yourproject/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/yourusername/yourproject.svg)](https://github.com/yourusername/yourproject/issues)

The car price predection using quickr dataset which extrated from kaggle and its help the user to find correct price for second handed cars
its has 9 feature and by using 8 feature we are predicting the price of car 

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- Name- The model of car
- abel-Primmum of carLocation
- location of car
- Price-price of car
- Kms_driven-car using based on kms
- Fuel_type-type of fuel
- Owner-owership of car(frist ,second )
- Year- year of car when its bought
- Company-the name of car

## Installation
-step 1- data clearing


!pip install pandas
# problem in data 
-unnamed is unused columns so have to remove


-ower have more null values so have to remove


-the price as rupee symbol and its object need remove symbol convert into int


-in price its contains columns  "ask price" this could remove 


-kms_driven is  object and km content in values so need remove km and convert object into int


-name columns is complex


-in fuel there same indication of petrol so gap should remove


-clearing data by using the pandas

-step 2- data ananlyics


-!pip install matplotlib.pyplot


-!pip install seaborn

 
-this libray are using for ananlying the data and detecting the outlayer


-step 3- feature engineering


-pip install scikit-learns--------this will help in feature engineering and building models


-from sklearn.model_selection import train_test_split--used for spliting the data into test and train


-from sklearn.preprocessing import OneHotEncoder --- this used to convert the catagorial values into the number


-from sklearn.preprocessing import StandardScaler--this is uesd for standandazation of large values into btw 0 to 1


-from sklearn.preprocessing import OrdinalEncoder--this to label the data


-from sklearn.compose import make_column_transformer---to transformcolumns into numbers


-from sklearn.pipeline import make_pipeline--its the path from tranform  columns the data for modeling



step 4-model building


from sklearn.linear_model import LinearRegression--this ml alrogithm which used to build the data

step 5-valiadation of model


from sklearn.metrics import r2_score---valadiation of model using r2_score 

step 6---saving model into files


import pickle--this used saving model into a file 


step7---deplovement of model


pip install streamlit 


import streamlit --this used for deplovement of moidel

```bash
# Clone the repository
git clone https://github.com/yourusername/yourproject.git

# Navigate to the project directory
cd yourproject

# Install dependencies
npm install



