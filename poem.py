# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 19:43:35 2025

@author: Kanchan Assudani
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "C:/Users/Kanchan Assudani/Documents/banking.csv"

 
df = pd.read_csv(file_path)

# Display first few rows of the dataset
print(df.head())

# 1. Distribution of Age
plt.figure(figsize=(8, 5))
sns.histplot(df['age'], bins=30, kde=True)
plt.title("Age Distribution of Clients")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
print("Mean Age:", df['age'].mean())
print("Median Age:", df['age'].median())
print("Age Range:", df['age'].min(), "to", df['age'].max())

# 2. Job Type Distribution
plt.figure(figsize=(10, 5))
sns.countplot(y=df['job'], order=df['job'].value_counts().index)
plt.title("Job Type Distribution")
plt.xlabel("Count")
plt.ylabel("Job Type")
plt.show()
print("Job Type Counts:")
print(df['job'].value_counts())

# 3. Marital Status Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x=df['marital'], order=df['marital'].value_counts().index)
plt.title("Marital Status Distribution")
plt.xlabel("Marital Status")
plt.ylabel("Count")
plt.show()
print("Marital Status Counts:")
print(df['marital'].value_counts())

# 4. Education Level Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x=df['education'], order=df['education'].value_counts().index)
plt.title("Education Level Distribution")
plt.xlabel("Education Level")
plt.ylabel("Count")
plt.show()
print("Education Level Counts:")
print(df['education'].value_counts())

# 5. Proportion of Clients with Credit in Default
default_proportion = df['default'].value_counts(normalize=True) * 100
print("Proportion of clients with credit in default:")
print(default_proportion)

# 6. Average Yearly Balance Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['balance'], bins=30, kde=True)
plt.title("Average Yearly Balance Distribution")
plt.xlabel("Balance (Euros)")
plt.ylabel("Count")
plt.show()
print("Mean Balance:", df['balance'].mean())
print("Median Balance:", df['balance'].median())
print("Balance Range:", df['balance'].min(), "to", df['balance'].max())

# 7. Number of Clients with Housing Loan
housing_count = df['housing'].value_counts()
print("Number of clients with housing loans:")
print(housing_count)

# 8. Number of Clients with Personal Loan
loan_count = df['loan'].value_counts()
print("Number of clients with personal loans:")
print(loan_count)

# 9. Communication Types Used
contact_types = df['contact'].value_counts()
print("Communication types used:")
print(contact_types)

# 10. Last Contact Day Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['day'], bins=31, kde=False)
plt.title("Last Contact Day Distribution")
plt.xlabel("Day")
plt.ylabel("Count")
plt.show()
print("Most Frequent Contact Day:", df['day'].mode()[0])

# 11. Last Contact Month Distribution
plt.figure(figsize=(10, 5))
sns.countplot(x=df['month'], order=["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])
plt.title("Last Contact Month Distribution")
plt.xlabel("Month")
plt.ylabel("Count")
plt.show()
print("Most Frequent Contact Month:", df['month'].mode()[0])

# 12. Duration of Last Contact Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['duration'], bins=30, kde=True)
plt.title("Duration of Last Contact")
plt.xlabel("Duration (seconds)")
plt.ylabel("Count")
plt.show()
print("Mean Duration:", df['duration'].mean())
print("Median Duration:", df['duration'].median())

# 13. Number of Contacts During Campaign
plt.figure(figsize=(8, 5))
sns.histplot(df['campaign'], bins=30, kde=False)
plt.title("Number of Contacts Per Client")
plt.xlabel("Contacts")
plt.ylabel("Count")
plt.show()
print("Mean Contacts Per Client:", df['campaign'].mean())

# 14. Previous Campaign Contact Days Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['pdays'], bins=30, kde=True)
plt.title("Days Since Last Contact")
plt.xlabel("Days")
plt.ylabel("Count")
plt.show()
print("Mean Days Since Last Contact:", df['pdays'].mean())

# 15. Outcome of Previous Campaigns
poutcome_count = df['poutcome'].value_counts()
print("Previous campaign outcomes:")
print(poutcome_count)

# 16. Clients Who Subscribed to a Term Deposit
plt.figure(figsize=(6, 4))
sns.countplot(x=df['y'])
plt.title("Term Deposit Subscription")
plt.xlabel("Subscribed")
plt.ylabel("Count")
plt.show()
print("Subscription Counts:")
print(df['y'].value_counts())

print("Analysis has been completed!!")









