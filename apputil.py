import seaborn as sns
import pandas as pd
import seaborn as sns


# Exercise 1

def fibonacci(n):
    """Return the nth Fibonacci number using recursion."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(9))



# Exercise 2

def to_binary(n):
    """Return the binary representation of a non-negative integer using recursion."""
    if n < 2:
        return str(n)

    return to_binary(n // 2) + str(n % 2)

print(to_binary(12)) 


# Exercise 3

def task_1():
    """Return column names sorted by increasing number of missing values."""
    df = df_bellevue.copy()

    print(
        "Cleaning gender column: standardizing case and converting blanks to NA."
    )
    df["gender"] = df["gender"].str.strip().str.lower()
    df_bellevue[df_bellevue['gender'].isin(['w', 'm'])]
    df["gender"] = df["gender"].replace("", pd.NA)

    missing_counts = df.isna().sum()
    sorted_columns = missing_counts.sort_values().index.tolist()

    return sorted_columns

print(task_1())


def task_2():
    """Return a DataFrame of total admissions per year."""
    df = df_bellevue.copy()

    print("Extracting year from date_in column.")

    df["date_in"] = pd.to_datetime(df["date_in"], errors="coerce")
    df["year"] = df["date_in"].dt.year

    admissions_per_year = (
        df.groupby("year")
        .size()
        .reset_index(name="total_admissions")
        .sort_values("year")
    )

    return admissions_per_year

print(task_2())


def task_3():
    """Return a Series of average age indexed by gender."""
    df = df_bellevue.copy()

    print(
        "Cleaning gender column and dropping rows with missing gender or age."
    )
    df = df_bellevue[df_bellevue['gender'].isin(['w', 'm'])]
    df = df.dropna(subset=["gender", "age"])

    average_age = df.groupby("gender")["age"].mean()

    return average_age

print(task_3())


def task_4():
    """Return a list of the five most common professions."""
    df = df_bellevue.copy()

    print(
        "Cleaning profession column: standardizing text and removing missing values."
    )
    df["profession"] = df["profession"].str.strip().str.lower()
    df["profession"] = df["profession"].replace("", pd.NA)

    df = df.dropna(subset=["profession"])

    top_professions = (
        df["profession"]
        .value_counts()
        .head(5)
        .index
        .tolist()
    )

    return top_professions

print(task_4())


#Exercise 4

from collections import defaultdict

memo = defaultdict(int)


def fibonacci(n):
    """Return the nth Fibonacci number using memoization."""
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]
