# Ding Wencan chrisdin@usc.edu
# Fall 2022
# Lab 13
# Description:
# Write a program which will visualize the Palmer Penguin dataset in the following way: frequency of flipper length
# for each species.

import pandas as pd
import matplotlib.pyplot as plt
def main():
    df = pd.read_csv ("penguins.csv")
    df = df.dropna()
    species_list = df["species"].unique()
    df_grouped = df.groupby("species")
    colors = ["orange","magenta","cyan"]

    df.round({"flipper_length_mm":0})
    count = []
    for species in species_list:
        count.append(df_grouped.get_group(species)["flipper_length_mm"].value_counts())
    for i, species in enumerate(species_list):
        plt.bar(count[i].index,count[i].values,width=1,label=species,alpha=0.4,color=colors[i])
    plt.title(label="Penguin flipper lengths(BAR)")
    plt.xlabel("Flipper length(mm)"),
    plt.ylabel("Frequency")
    plt.grid(which="major",color="#999999",alpha=0.2)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
