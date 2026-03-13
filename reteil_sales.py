import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class RetailAnalyzer:

    def __init__(self):
        self.data = None


    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("Data loaded successfully")
            print(self.data.head())
        except Exception as e:
            print("Error loading file:", e)


    def calculate_metrics(self):

        total_sales = self.data["Total Sales"].sum()

        avg_sales = self.data["Total Sales"].mean()

        popular_product = self.data["Product"].mode()[0]

        print("Total Sales:", total_sales)
        print("Average Sales:", avg_sales)
        print("Most Popular Product:", popular_product)


    def filter_data(self, category):

        filtered = self.data[self.data["Category"] == category]

        print(filtered)


    def display_summary(self):

        print(self.data.describe())


    def bar_chart(self):

        sales = self.data.groupby("Category")["Total Sales"].sum()

        sales.plot(kind="bar")

        plt.title("Sales by Category")

        plt.show()


    def line_graph(self):

        plt.plot(self.data["Date"], self.data["Total Sales"])

        plt.title("Sales Trend")

        plt.xlabel("Date")

        plt.ylabel("Sales")

        plt.show()


    def heatmap(self):

        corr = self.data[["Price","Quantity Sold","Total Sales"]].corr()

        sns.heatmap(corr, annot=True)

        plt.show()


# MAIN PROGRAM

analyzer = RetailAnalyzer()

analyzer.load_data(r"C:\Users\HP\Downloads\retail_sales.csv")

analyzer.calculate_metrics()

analyzer.display_summary()

analyzer.filter_data("Electronics")

analyzer.bar_chart()

analyzer.line_graph()

analyzer.heatmap()