# Task_5
This Exploratory Data Analysis (EDA) provides valuable insights into the Titanic dataset, highlighting factors that may have influenced a passenger’s chance of survival. These insights can help in the development of predictive models for survival prediction or further exploration into the social and demographic patterns aboard the Titanic.

# Titanic Dataset Exploratory Data Analysis (EDA)

## Overview

This project performs **Exploratory Data Analysis (EDA)** on the Titanic dataset to uncover insights about the passengers aboard the RMS Titanic. The dataset contains information about passengers such as age, sex, class, and survival status. The goal of this analysis is to identify patterns and relationships within the dataset, specifically factors affecting survival rates.

---

## Project Structure

```plaintext
Titanic_Dataset/
├── EDA.py                # Python script that performs EDA on the Titanic dataset
├── train.csv             # Titanic dataset (CSV format)
└── README.md             # Project documentation
Dataset Information
The Titanic dataset contains 891 entries with 12 columns:

Column	Description
PassengerId	Unique identifier for each passenger.
Survived	Survival status (0 = No, 1 = Yes).
Pclass	Passenger class (1 = 1st, 2 = 2nd, 3 = 3rd).
Name	Name of the passenger.
Sex	Gender of the passenger.
Age	Age of the passenger in years.
SibSp	Number of siblings or spouses aboard.
Parch	Number of parents or children aboard.
Ticket	Ticket number.
Fare	Fare paid for the ticket.
Cabin	Cabin number.
Embarked	Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).
Features of the Analysis
Missing Value Handling:

Missing Age values are filled with the median of the column.

Missing Embarked values are filled with the mode (most frequent port).

Statistical Summaries:

Summary statistics for numerical columns such as mean, standard deviation, and quantiles.

Visualizations:

Histograms and Kernel Density Estimation (KDE) plots for continuous features like Age, Fare, SibSp, and Parch.

Correlation Matrix to explore relationships between numeric features.

Count Plots to visualize the distribution of categorical features like Sex, Embarked, and Pclass.

Pairplots to visualize the relationship between pairs of features with respect to survival.

Observations & Insights:

Insights based on the visualizations and statistical analysis of features such as Age, Fare, SibSp, and more.

Requirements
The following Python libraries are required to run the code:

pandas - For data manipulation.

matplotlib - For data visualization.

seaborn - For statistical data visualization.

Installation
To install the necessary libraries, you can use the following pip command:

bash
Copy code
pip install pandas matplotlib seaborn
How to Run the Code
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/titanic-eda.git
Navigate to the project directory:

bash
Copy code
cd titanic-eda
Run the Python script EDA.py to perform the Exploratory Data Analysis:

bash
Copy code
python EDA.py
Outputs
When running the script, you will get:

Dataset Info: The summary of the dataset including the shape, column data types, and missing values.

Statistical Summary: Descriptive statistics such as the mean, standard deviation, and quantiles for numerical columns.

Visualizations:

Histograms for Age, Fare, SibSp, Parch.

Correlation matrix heatmap.

Count plots for categorical variables like Sex, Embarked, and Pclass.

Pair plots to explore relationships between selected features.

Key Observations: Insights such as survival rates based on passenger class, sex, and other features.

Example Output
1. Correlation Heatmap
The heatmap visually shows the relationships between numerical features. For instance, there’s a strong negative correlation between Fare and Pclass (higher fare means a higher class).

2. Pairplot
A pairplot helps to see how different features interact with each other, especially the Survived column. It shows that higher-class passengers had a better chance of survival.

3. Count Plots
Count plots display the frequency distribution of categorical variables. For example, more passengers boarded from Southampton (S), and most passengers were male.

Key Insights
Survival Rates:

Females had a higher chance of survival compared to males.

Passengers in 1st class had a much higher chance of survival compared to those in 3rd class.

Age distribution is right-skewed, with most passengers being between 20 and 40 years old.

Fare distribution is right-skewed, with many passengers paying low fares and a few paying high fares.

Embarked Port:

The majority of passengers boarded the Titanic from Southampton (S).
