from flask import Flask, render_template, redirect
import os, hed_scrape

app = Flask(__name__)

@app.route('/')
def home():
    links = hed_scrape.scrape_heds()

    return render_template('index.html', links=links)

if __name__ == '__main__':
    # app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)