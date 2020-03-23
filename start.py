from flask import Flask, escape, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route('/corona')
def corona():
    URL = "https://www.sst.dk/da/corona/tal-og-overvaagning"
    webpage = requests.get(URL)
    soup = BeautifulSoup(webpage.content, "html.parser")
    html_tables = soup.findAll(class_ = "table-responsive")
    paragraphs = ""
    for table in html_tables:
        paragraphs = paragraphs + str(table)
    return paragraphs


if __name__ == "__main__":
    app.run(debug=True, host="localhost")
