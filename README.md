# Electricity Price Explanation

Estimate daily electricity futures price variations in France and Germany based on explanatory variables.

## Description

This project aims to figure out how electricity prices in France and Germany are influenced by things like weather, energy data, and business factors. We want to understand the connections between these factors and how they all work together to affect electricity prices. By studying and analyzing these relationships, we hope to reveal a clearer picture of how weather, energy markets, and business aspects interact to determine electricity prices in both countries.

## Getting Started

### Dataset

* Dataset consists 3 csv files X_train,Y_train,X_test
* Training data contains 35 columns includes DAY,DAY_ID,_COUNTRY, variations in commodity prices, weather conditions, energy production and usage.
* Y_train contains DAY_ID corresponding to X_train and TARGET which represents daily price variation for 24 hrs.


### Data Preprocessing

* To maintain the integrity of our datasets and the consistency of our analyses, we have adopted a straightforward approach to handling missing values. All missing data points have been filled with 0. 

### Executing program

* Boosting
* Random Forest
* ADA Boost
* Gradient Boost Trees

## Authors

Contributors:
* Deepti Sammeta
* Nihitha Malayarukil
* Nishant Dave
* Serafina Luanqi Chen

## Version History

* 0.1
    * Initial Release, Data Preprocessing

## Acknowledgments

* [Data Challenge](https://challengedata.ens.fr/participants/challenges/97/)
