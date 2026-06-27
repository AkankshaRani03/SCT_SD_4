from flask import Flask, render_template, request, send_file
from scraper import scrape_products
from exporter import export_csv, export_excel

app = Flask(__name__)

products_cache = []


@app.route("/")
def home():
    return render_template(
        "index.html",
        products=[],
        stats={}
    )


@app.route("/search", methods=["POST"])
def search():

    global products_cache

    website = request.form.get("website")

    products_cache = scrape_products(website)

    prices = []

    for product in products_cache:

        try:
            prices.append(
                float(
                    str(product["price"])
                    .replace("$", "")
                    .replace("₹", "")
                    .replace(",", "")
                )
            )

        except:
            pass

    stats = {

        "count": len(products_cache),

        "average":

        round(
            sum(prices) / len(prices),
            2
        )

        if prices else 0,

        "highest":

        max(prices)
        if prices else 0,

        "lowest":

        min(prices)
        if prices else 0

    }

    return render_template(

        "index.html",

        products=products_cache,

        stats=stats

    )


@app.route("/download/csv")
def download_csv():

    path = export_csv(products_cache)

    return send_file(

        path,

        as_attachment=True

    )


@app.route("/download/excel")
def download_excel():

    path = export_excel(products_cache)

    return send_file(

        path,

        as_attachment=True

    )

print(app.url_map)
if __name__ == "__main__":

    app.run(

        debug=True

    )