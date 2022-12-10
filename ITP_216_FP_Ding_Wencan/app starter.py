# Ding Wencan
# Fall 2022
# Section 32080
# Final Project
# Visualize the relationship between attributes and housing prices
# Make prediction based on the linear regression model

import base64
from flask import Flask, redirect, render_template, request, url_for
import pandas as pd
from matplotlib import pyplot as plt
import os
from sklearn.linear_model import LinearRegression
from io import BytesIO
import sqlite3 as sl

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("selectAttributes.html")

@app.route("/client",methods=["POST","GET"])
def client():
    global attribute
    if request.method == "POST":
        if "attribute" not in request.form:
            return render_template("Error.html", message="An error happend!")
        attribute = request.form["attribute"]
        # reg_equation = get_reg_equation(open_file("California housing price.csv"), attribute)
        return render_template("visualization.html",
                               title="Visualization of the Relationship Between the Attribute and Housing Price",
                               plot=visualization(open_file(get_data_from_database()),attribute,False))

@app.route("/action/re-pick",methods=["POST","GET"])
def re_pick():
    return redirect(url_for("home"))

@app.route("/action/return-to-homepage",methods=["POST","GET"])
def return_to_home_page():
    return redirect(url_for("home"))

@app.route("/prediction",methods=["POST","GET"])
def predict():
    global attribute
    df = open_file(get_data_from_database())
    intercept, coef = get_reg_equation(df,attribute)
    return render_template("Prediction.html",
                           helloworld=(str(intercept) + " + " + str(coef) + " * " + attribute),
                           plot=visualization(df,attribute,True))

@app.route("/action/calculate",methods=["POST","GET"])
def calculate():
    global attribute
    value = float(request.form["value"])
    intercept , coef = get_reg_equation(open_file(get_data_from_database()),attribute)
    result = value * coef + intercept
    if result <=0:
        return render_template("Error.html", message ="The housing value is abnormal")
    else:
        return render_template("CalculationResult.html", result=result)


# Function: get data from the database
# No Parameter, get data and return in dataframe
def get_data_from_database():
    db = "housingAttribute.db"
    cursor = sl.connect(db)
    return pd.read_sql_query("SELECT * FROM housingPriceAttribute",cursor)

    # df = pd.read_csv(filename, header=0,sep=",")
    # conn = sl.connect(db)
    # curs= conn.cursor()
    # stmt1 = "SELECT * FROM housingPriceAttribute;"
    # df = curs.execute(stmt1)

# Function:open csv file and clean up data
# Parameter:the dataframe from the database
def open_file(df):
    df = df.dropna()
    # randomly 1500 samples
    df = df.sample(n=1500, replace=True)

    # replace all the strings that represent distances to sea by floats of hours
    df = df.replace("ISLAND",0)
    df = df.replace("NEAR OCEAN",0.2)
    df = df.replace("NEAR BAY",0.5)
    df = df.replace("<1H OCEAN",0.8)
    df = df.replace("INLAND",2)
    return df

# Function:get the coefficient and interception of the regression line
# Parameter:dataframe of all data and the attributes for training
def get_reg_equation(df,train):
    # set the linear regression model
    model = LinearRegression()
    # training the model
    model.fit(df[[train]],df[["median_house_value"]])
    return model.intercept_[0], model.coef_[0][0]

# Function:Visualize the graphs
# Parameter: dataframe, the attribute the user chooses, and whether it is for predict or just existing data.
def visualization(df, attribute, predict):
    if predict:
        y = df[["median_house_value"]]
        x = df[[attribute]]
        plt.figure()
        plt.xlabel(attribute)
        plt.ylabel("house value")
        plt.title("relationship between " + attribute + " and housing value predicted")
        plt.legend([attribute],loc="best")
        intercept, coef = get_reg_equation(df, attribute)
        y = x * coef + intercept
        plt.plot(x, y, c="cyan")
        # Change the image to base64 to present in html
        figfile = BytesIO()
        plt.savefig(figfile, format="png")
        figfile.seek(0)
        figfile_png = base64.b64encode(figfile.getvalue())
        figdata_str = str(figfile_png,"utf-8")
        html = "<img src=\"data:image/png;base64,{}\"/>".format(figdata_str)
        return html
    # data visualization for existing data
    else:
        y = df[["median_house_value"]]
        x = df[[attribute]]
        plt.figure()
        plt.scatter(x,y,alpha=1/3)
        plt.xlabel(attribute)
        plt.ylabel("house value")
        plt.title("relationship between " + attribute + " and housing value based on existing data")
        plt.legend([attribute],loc="best")

    # post on html
        figfile = BytesIO()
        plt.savefig(figfile,format="png")
        figfile.seek(0)
        figfile_png = base64.b64encode(figfile.getvalue())
        figdata_str = str(figfile_png, "utf-8")
        html = "<img src=\"data:image/png;base64,{}\"/>".format(figdata_str)
        return html

if __name__ == "__main__":
    # print(open_file(get_data_from_database()))
    app.secret_key = os.urandom(12)
    app.run(debug=True)
    # db = "housingAttribute.db"
    # conn = sl.connect(db)
    # df = open_file("California housing prices.csv")
    # df.to_sql("housingPriceAttribute, conn, if_exists="append", index=False)
    # conn.close()