# End to End Machine Learning Project
## Description:

    This project was done for a learning purpose and may not provide actual reasoning.

    This project contains gemstone prediction as per the kaggle dataset.
    LINK: https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv

## Aim of the project:
    The aim of this project is to predict the price of gemstones based on certain factors such as carat, clarity, depth etc.

## Introduction About the Data :

The goal is to predict `price` of given diamond.
This is a Regression Analysis as it would be predicting price which is a **continous value**

There are 10 independent variables (including `id`):

* `id` : unique identifier of each diamond
* `carat` : Carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstones and diamonds.
* `cut` : Quality of Diamond Cut
* `color` : Color of Diamond
* `clarity` : Diamond clarity is a measure of the purity and rarity of the stone, graded by the visibility of these characteristics under 10-power magnification.
* `depth` : The depth of diamond is its height (in millimeters) measured from the culet (bottom tip) to the table (flat, top surface)
* `table` : A diamond's table is the facet which can be seen when the stone is viewed face up.
* `x` : Diamond X dimension
* `y` : Diamond Y dimension
* `x` : Diamond Z dimension

Target variable:
* `price`: Price of the given Diamond.

## Pre-Requisites:
1. Setting up a virtual env:
```
conda create -p [virtual_environment_name] python==[version]
```
- Activating virutal environment:
```
conda activate [virtual_environment_name]
```
2. Installing necessary libraries:
```
pip install requirements.txt
```
