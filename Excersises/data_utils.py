
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_null_counts(df):
    df_missing = df.loc[:,df.isna().any()]

    nullCount = df_missing.isna().sum()

    plt.figure(dpi= 120, figsize=(6,4))

    plt.bar(nullCount.index, nullCount.values)
    plt.show()