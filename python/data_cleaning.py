import pandas as pd
import numpy as np

print("loading datasets ...")

reg = pd.read_csv("data/raw/reg_data.csv",sep =";")
auth = pd.read_csv("data/raw/auth_data.csv",sep = ";")
ab = pd.read_csv("data/raw/ab_test.csv" , sep = ";")

print("Datasets loaded successfully")


# Registration section 

print("\n" + "="*60)
print("REGISTRATION DATA")
print("="*60)

print(reg.head())

print(f"\nShape: {reg.shape}")

print("\nInfo:")
reg.info()

print("\nMissing Values:")
print(reg.isnull().sum())

print("\nDuplicate Rows:", reg.duplicated().sum())

print("\nUnique Registered Users:", reg["uid"].nunique())

#Authentication section

print("\n" + "="*60)
print("AUTHENTICATION DATA")
print("="*60)

print(auth.head())

print(f"\nShape: {auth.shape}")

print("\nInfo:")
auth.info()

print("\nMissing Values:")
print(auth.isnull().sum())

print("\nDuplicate Rows:", auth.duplicated().sum())

print("\nUnique Auth Users:", auth["uid"].nunique())

# A/B test section

print("\n" + "="*60)
print("A/B TEST DATA")
print("="*60)

print(ab.head())

print(f"\nShape: {ab.shape}")

print("\nInfo:")
ab.info()

print("\nMissing Values:")
print(ab.isnull().sum())

print("\nDuplicate Rows:", ab.duplicated().sum())

print("\nUsers in A/B Test:", ab["user_id"].nunique())

print("\nRevenue Statistics")
print(ab["revenue"].describe())

print("\nA/B Group Distribution")
print(ab["testgroup"].value_counts())

#Timestamp conversion

reg["reg_ts"] = pd.to_datetime(reg["reg_ts"], unit="s")
auth["auth_ts"] = pd.to_datetime(auth["auth_ts"], unit="s")

#Date range 
print("\nRegistration Period")
print("Start:", reg["reg_ts"].min())
print("End:", reg["reg_ts"].max())

print("\nAuthentication Period")
print("Start:", auth["auth_ts"].min())
print("End:", auth["auth_ts"].max())

#Saving processed data

reg.to_csv("data/processed/reg_data_clean.csv", index=False)

auth.to_csv("data/processed/auth_data_clean.csv", index=False)

ab.to_csv("data/processed/ab_test_clean.csv", index=False)

print("\nCleaned datasets saved successfully!")