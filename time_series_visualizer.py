import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import calendar
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("./fcc-forum-pageviews.csv", index_col="date", parse_dates=True)
# Clean data
start = round(len(df) / 100 * 2.5)
end = round(len(df) / 100 * 97.5)
df = df[start:end]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20, 7))
    ax = sns.lineplot(x="date", y="value", data=df, ax=ax, color="red", linewidth=2)
    ax.set(
        xlabel="Date",
        ylabel="Page Views",
        ylim=(0, 200000),
        title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
    )
    # Save image and return fig (don't change this part)
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot

    df_bar = df.copy()
    df_months = []
    df_years = []
    for i, row in df_bar.iterrows():
        df_months.append(i.month)
        df_years.append(i.year)
    df_bar["month"] = df_months
    df_bar["year"] = df_years
    df_bar = df_bar.sort_values("month")
    df_bar["month"] = df_bar.apply(
        lambda row: calendar.month_name[row["month"]], axis=1
    )

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(9, 11))

    ax = sns.barplot(x="year", y="value", hue="month", data=df_bar, ax=ax, ci=None)
    ax.set(xlabel="Years", ylabel="Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime("%b") for d in df_box.date]
    df_box["month_index"] = [d.month for d in df_box.date]
    df_box = df_box.sort_values("month_index")

    # Draw box plots (using Seaborn)
    # whats a box plotttt
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(36, 11))
    ax1 = sns.boxplot(data=df_box, y="value", x="year", ax=ax1)
    ax1.set(
        ylim=(0, 200000),
        ylabel="Page Views",
        yticks=[
            0,
            20000,
            40000,
            60000,
            80000,
            100000,
            120000,
            140000,
            160000,
            180000,
            200000,
        ],
        xlabel="Year",
        title="Year-wise Box Plot (Trend)",
    )

    ax2 = sns.boxplot(data=df_box, y="value", x="month", ax=ax2)
    ax2.set(
        ylim=(0, 200000),
        yticks=[
            0,
            20000,
            40000,
            60000,
            80000,
            100000,
            120000,
            140000,
            160000,
            180000,
            200000,
        ],
        ylabel="Page Views",
        xlabel="Month",
        title="Month-wise Box Plot (Seasonality)",
    )

    # Save image and return fig (don't change this part)
    fig.savefig("box_plot.png")
    return fig
