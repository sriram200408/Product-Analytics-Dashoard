import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

print("Loading cleaned datasets...")

reg = pd.read_csv("data/processed/reg_data_clean.csv")
auth = pd.read_csv("data/processed/auth_data_clean.csv")
ab = pd.read_csv("data/processed/ab_test_clean.csv")

reg["reg_ts"] = pd.to_datetime(reg["reg_ts"])
auth["auth_ts"] = pd.to_datetime(auth["auth_ts"])

print("Datasets Loaded!")

# Daily Registrations 

daily_reg = (
    reg.groupby(reg["reg_ts"].dt.date)["uid"]
    .count()
    .reset_index(name="registrations")
)

print(daily_reg.head())

#plot for daily registrations 

plt.figure(figsize=(12,5))

plt.figure(figsize=(15,6))

plt.plot(
    daily_reg["reg_ts"],
    daily_reg["registrations"],
    linewidth=2
)


plt.title("Daily User Registrations")
plt.xlabel("Date")
plt.ylabel("Registrations")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("screenshots/daily_registrations.png", dpi=300, bbox_inches="tight")
plt.show()

# Daily active Users

dau = (
    auth.groupby(auth["auth_ts"].dt.date)["uid"]
    .nunique()
    .reset_index(name="DAU")
)

print(dau.head())

# plot for daily active users

plt.figure(figsize=(15, 6))

plt.plot(
    dau["auth_ts"],
    dau["DAU"],
    linewidth=2
)

plt.title("Daily Active Users")
plt.xlabel("Date")
plt.ylabel("Users")

plt.xticks(rotation=45)

plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("screenshots/daily_active_users.png", dpi=300, bbox_inches="tight")
plt.show()


# Monthly User registrations and plots

monthly_reg = (
    reg.groupby(reg["reg_ts"].dt.to_period("M"))["uid"]
       .count()
       .reset_index(name="registrations")
)

monthly_reg["reg_ts"] = monthly_reg["reg_ts"].dt.to_timestamp()

plt.figure(figsize=(15,6))

plt.plot(
    monthly_reg["reg_ts"],
    monthly_reg["registrations"],
    linewidth=2
)

plt.title("Monthly User Registrations")
plt.xlabel("Month")
plt.ylabel("Registrations")

plt.grid(alpha=0.3)

ax = plt.gca()
ax.xaxis.set_major_locator(mdates.YearLocator(2))          # Show every 2 years
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("screenshots/monthly_registrations.png", dpi=300)

plt.show()


# Revenue Distribution and plots

plt.figure(figsize=(10,6))

plt.hist(ab["revenue"], bins=50)

plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("screenshots/revenue_distribution.png", dpi=300)

plt.show()


# revenue by test group and plot
group_rev = (
    ab.groupby("testgroup")["revenue"]
      .mean()
)

plt.figure(figsize=(6,5))

plt.bar(group_rev.index, group_rev.values)

plt.title("Average Revenue by Test Group")
plt.xlabel("Group")
plt.ylabel("Average Revenue")

plt.tight_layout()

plt.savefig("screenshots/ab_group_revenue.png", dpi=300)

plt.show()

# Top 10 most active users 

top_users = (
    auth.groupby("uid")
        .size()
        .sort_values(ascending=False)
        .head(10)
)

plt.figure(figsize=(10,6))

plt.bar(top_users.index.astype(str), top_users.values)

plt.title("Top 10 Most Active Users")
plt.xlabel("User ID")
plt.ylabel("Login Count")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("screenshots/top_users.png", dpi=300)

plt.show()


# Monthly active users

mau = (
    auth.groupby(auth["auth_ts"].dt.to_period("M"))["uid"]
    .nunique()
    .reset_index(name="MAU")
)

print(mau)

#A/B revenue analytics

print("\nRevenue by Group")

print(
    ab.groupby("testgroup")["revenue"].describe()
)
 # plot for revenue of A/B 
plt.figure(figsize=(8,6))

ab.boxplot(column="revenue", by="testgroup")

plt.title("Revenue Distribution by A/B Test Group")
plt.suptitle("")  
plt.xlabel("Test Group")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig("screenshots/revenue_boxplot.png", dpi=300)

plt.show()


