# ITP 216 Homework 13
# Fall 2022

import pandas as pd
import matplotlib.pyplot as plt


def main():
    # reading in the dataset
    df = pd.read_csv("weather.csv")

    # removing rows of data where the observed temp is null
    df = df[df["TOBS"].notnull()]

    # making a column for year: allows us to easily get the last 10 years
    df["YEAR"] = df["DATE"].str[0:4]
    years_list = list(df["YEAR"].unique())

    # making a column for month: allows us to group by month
    df["MONTH_DAY"] = df["DATE"].str[-5:]
    df = df[df['MONTH_DAY'] != '02-29']  # drop leap years
    month_days_list = list(df["MONTH_DAY"].unique())
    df.sort_values(inplace=True, by='MONTH_DAY')
    print(df[['DATE', 'YEAR', 'MONTH_DAY', 'TOBS']])

    # list of months to label the x-axis of both graphs
    month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # create two plots
    fig, ax = plt.subplots(2,1)
    # add overall title
    fig.suptitle("Climate Visualization for LA from year 2018 to 2022")
    # -------- TOP GRAPH -------------------------------------------------

    # make the xtick list from a range from 0 to 365 and step by 31 days per month
    ax[0].xaxis.set_ticks(range(0,365,31))
    # to avoid warnings, use axis.xaxis.set_xticks() and .set_ticklabels()

    # you can use month_list aove for x labels
    ax[0].set_xticklabels(labels=month_list)
    # set your other axis attributes using set()

    # 4 colors, one for each year
    colors = ["orange","magenta","cyan","green","red"]
    # make an index into our color array to keep track of which color we're plotting
    index = 0
    # group by 'YEAR'
    df_grouped = df.groupby("YEAR")
    # loop through the years and plot observed temperature (TOBS) for every day
    for year in years_list:
        df_group = df_grouped.get_group(year)
    # get year group
    # plot year group TOBS (y-axis) vs year group month day (x axis)
        ax[0].plot(df_group["MONTH_DAY"],df_group["TOBS"],color=colors[index],label=years_list[index],linewidth=0.1)
    # incrementing index to move onto the next color
        index += 1
    # plot gridlines
    ax[0].set(title="most recent 4 years")
    ax[0].grid()
    # show legend (make sure to add label attributes to your plot() call for this to work
    ax[0].legend()
    # -------- BOTTOM GRAPH -------------------------------------------------

    # be sure to use ax[1] going forward now

    # set your attributes and xaxis ticks and labels as you did before
    ax[1].xaxis.set_ticks(range(0, 365, 31))
    # creating separate dfs to separate 2021 from the historical years
    ax[1].set_xticklabels(labels=month_list)
    ax[1].set(title="comparing current year and historical averages")
    dfs = df[df["YEAR"]=="2021"]
    # use filtering like penguins 5kg+ in lecture slides

    # take the first row of any unique date for the current year 2021
    dfs.drop_duplicates(subset=["MONTH_DAY"],inplace=True)
    # use drop_duplicates()

    # make an empty list to store average temps for historical data
    avertemps = []
    # convert current year df to a list using typecasting to store observed temps for 2021
    temps2021 = dfs["TOBS"].tolist()
    # group historical years by 'MONTH_DAY' / contains dates NOT in 2021
    df_historical = df[df["YEAR"]!="2021"]
    df_grouped = df_historical.groupby("MONTH_DAY")
    # loop through each day of the year (month day list) and finding the average using mean()
    for day in month_days_list:
    # get month day group
        df_group = df_grouped.get_group(day)
    # find the average of TOBS of the month day group using mean()
        mean = df_group["TOBS"].mean()
    # adding the average for this date to avg_list
        avertemps.append(mean)
    # # bar plot the historical averages (historical years avg list is your y axis) vs month days list (your x-axis)
    ax[1].bar(x=month_days_list,height=avertemps,color="cyan",label="historical average")
    # # be sure to specify a color of your choice and a label for the legend to work later
    #
    # # bar plot the current year temps (current year temps is your y-axis) vs month days list (your x-axis)
    ax[1].bar(x=dfs["MONTH_DAY"],height=temps2021,color="red",label="2021")
    # be sure to specify a color of your choice and a label for the legend to work later

    # add gridlines
    ax[1].grid()
    # add legend
    ax[1].legend()
    # make tight layout and finally show your plot
    plt.show()
    plt.tight_layout()

if __name__ == '__main__':
    main()
