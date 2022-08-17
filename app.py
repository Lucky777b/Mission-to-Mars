# Import tools
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping_mars

# Set up Flask 
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define the route for the HTML page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index2.html", mars=mars)

# Set up Scrape Route
# Scrape updated data from homepage of web app 
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping_mars.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

# Tell Flask to run 
if __name__ == "__main__":
   app.run()