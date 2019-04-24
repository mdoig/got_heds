from flask import Flask, render_template, redirect
import hed_scrape

app = Flask(__name__)

@app.route('/')
def home():
    links = hed_scrape.scrape_heds()

    return render_template('index.html', links=links)

# if __name__ == '__main__':
#     app.run(debug=True)