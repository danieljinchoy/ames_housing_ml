# Ames Housing Machine Learning Project
![1_XbHGvrdlklAx7MsrtGBJ3w](https://user-images.githubusercontent.com/29543481/103142793-e3482080-46d7-11eb-8b8b-624a04af6106.jpeg)

### Introduction

House flipping is a common real estate investment strategy by purchasing a property and selling it in the hopes of making a profit. This can mean that sometimes, flipping a house means the temporary owner has to make a lot of repairs or renovations until the owner can sell it for more than the investment cost. Hence, the goal is to buy low and sell high. However, house flipping can sometimes be financially risky due to the uncertainty of the market. Our objective therefore is to come up with a pricing model that values homes in the city of Ames and to provide a greater transparency to homeowners or house flippers. 



### About the Data

The data contains 2558 observations and 190 features on homes sold in Ames, Iowa from 2006 to 2010. Within the features, we carefully selected a subset of these features and engineered some of our own features to simplify and sharpen the focus of our subsequent models. We also ran random forest and lasso regression to further select our features, before finalizing our features into our learn and tree-based machine learning models. 



### Understanding Ames, Iowa

![iowa-state-university-logo](https://user-images.githubusercontent.com/29543481/103159147-c40ec900-4793-11eb-868f-094e36cef61e.png)

Ames, Iowa economy and demographics is largely defined by the Iowa State University, a public research university located in the middle of the city. More than half of Ames population is either studying or working at Iowa State University, which makes Ames one large extended campus. Just like many college towns, Ames real estate market is defined by a very large proportion of rental properties, which explains the stability of the housing market in Ames (please note the EDA Jupyter Notebook for more information). 



### Objective

In this collaborative project, our objective is to: 
1. Explore Ames Housing Market in the context of house flipping market;
2. Train machine learning model to predict future housing sale prices in Ames, Iowa
3. Estimate the price differences made by specific house features 
4. Produce a practical guide for those looking to flip homes for a profit.



### About the Repository

The project was completed with a series of jupyter notebooks. 

- **Preprocessing**: Preprocessing folder contains two jupyter notebooks that cleans and merges data used in the project. The second version of the jupyter notebook contains codes for geocoding (creating new latitude and longitude values) and new variables such as distances. The distance variable is the distance value between each house and Iowa State University.
- **EDA**: EDA folder contains all the Exploratory Data Analysis on the housing market. 
- **Rfiles**: Folder that contains some R files and R project file that were used to do initial modeling and assessment.
- **data**: contains all the data used the project.
- **Presentations**: Folder that contains all the presentation files. 


