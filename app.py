# Import tools

from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

#  set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#  *******************
#  Set up Flask routes
#  *******************

#  Function to Displays home page
#  *****************************
@app.route("/")
def index():
    # find "mars" collection
    mars = mongo.db.mars.find_one()

    # return an HTML template using "index.html" file
    # Python command mars = mars to use MongoDB collection "mars" 
    return render_template("index.html",mars=mars)

#  Function to Displays scrapipython ng data
#  **********************************
#  Defines the route "/scrape"
#  ***************************
@app.route("/scrape")
#  Defines the "scrape" function
# ****************************** 
def scrape():
#  Assign a variable "mars" to point to MongoDB
   mars = mongo.db.mars
#  Assign a variable "mars_data" to hold the newly scraped data   
   mars_data = scraping.scrape_all()
# Update the database using the update() function 
#  parameters for update() "query_parameter" = {} (empty json object) 
#                          "data"  = mars_data
#                          "upsert" = True (add a new document if does not exists )
   mars.update({}, mars_data, upsert=True)
   
#  add redirect after successful scraping the data - navigate back route('/')
   return redirect('/', code=302)

# Flask to run the code
if __name__ == "__main__":
   app.run()