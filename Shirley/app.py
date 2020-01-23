###########################################################
#    Imports
###########################################################
import numpy as np
import pandas as pd
import sqlalchemy
# from config import api_key
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template

#################################################
# Database Setup
#################################################
# create database connection
# reflect an existing database into a new model
# Save a reference to the table

username = 'postgres'
password = 'L3arn2019!'
engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/crash')

Base = automap_base()
Base.prepare(engine, reflect=True)
# Crashes = Base.classes.crashes
GeoCrash = Base.classes.geocrashes


#################################################
# Flask Setup
#################################################

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT']=0


#################################################
# Flask Routes -- for web pages
##################################################

@app.route("/")
def welcome():
    webpage = render_template('index.html')
    return webpage


@app.route("/summary.html")
def summary():
    webpage = render_template("summary.html")
    return webpage


@app.route("/Visual1.html")
def Visual1():
    webpage = render_template("Visual1.html", page_title = "Heatmap")
    return webpage


@app.route("/Visual2.html")
def Visual2():
    webpage = render_template("Visual2.html", page_title = "GeoMaps")
    return webpage


@app.route("/Visual3.html")
def Visual3():
    webpage = render_template("Visual3.html", page_title = "Timeline of Crashes")
    return webpage


@app.route("/Visual4.html")
def Visual4():
    webpage = render_template("Visual4.html", page_title = "Crashes By Operator")
    return webpage


@app.route("/data.html")
def data():
    webpage = render_template("data.html", page_title = "Data Sources")
    return webpage



#################################################
# Flask Routes -- for json data pages
##################################################

@app.route("/milData")
def milData():
    session = Session(engine)
    results = session.query(Crashes.index, Crashes.Ranking, Crashes.Total_Fatalities, Crashes.Operator, Crashes.Military).all()
    session.close()

    crash_history = []

    for index, Ranking, Total_Fatalities, Operator, Military in results:
        history_dict = {}
        history_dict["Index"] = index
        history_dict["Ranking"] = Ranking
        history_dict["Total_Fatalities"] = Total_Fatalities
        history_dict["Operator"] = Operator
        history_dict["Military"] = Military
        crash_history.append(history_dict)

    return jsonify(crash_history)


@app.route("/geoData")
def geoData():
    session = Session(engine)
    resultsG = session.query(GeoCrash.index, GeoCrash.Year, GeoCrash.Month, GeoCrash.Day, GeoCrash.Location, GeoCrash.Operator, GeoCrash.Military, GeoCrash.Aboard, GeoCrash.Fatalities, GeoCrash.Summary, GeoCrash.long, GeoCrash.lat).all()
    session.close()

    geo_data = []

    for index, Year, Month, Day, Location, Operator, Military, Aboard, Fatalities, Summary, long, lat in resultsG:
        geo_dict = {}
        geo_dict["Index"] = index
        geo_dict["Year"] = Year
        geo_dict["Month"] = Month
        geo_dict["Day"] = Day
        geo_dict["Location"] = Location
        geo_dict["Operator"] = Operator
        geo_dict["Military"] = Military
        geo_dict["Aboard"] = Aboard
        geo_dict["Fatalities"] = Fatalities
        geo_dict["Summary"] = Summary
        geo_dict["long"] = long
        geo_dict["lat"] = lat
        geo_data.append(geo_dict)

    return jsonify(geo_data)


if __name__ == '__main__':
    app.run(debug=True)