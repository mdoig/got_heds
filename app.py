# Set up app
from flask import Flask, render_template, redirect
import os, hed_scrape

app = Flask(__name__)

# Create route
@app.route('/')
def home():
    # The hed_scrape module and scrape_heds() function scrapes the hrefs and the headline text
    links = hed_scrape.scrape_heds()

    # Render the info in links to the html file
    return render_template('index.html', links=links)

# Define port
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)