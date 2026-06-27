import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def scrape_products(website):

    products = []

    # ---------------- Books ---------------- #

    if website == "books":

        url = "https://books.toscrape.com/catalogue/page-1.html"

        response = requests.get(url, headers=HEADERS)

        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all(
            "article",
            class_="product_pod"
        )

        for book in books:

            title = book.h3.a["title"]

            price = book.find(
                "p",
                class_="price_color"
            ).text.strip()

            availability = book.find(
                "p",
                class_="instock availability"
            ).text.strip()

            rating = book.p["class"][1]

            image = (
                "https://books.toscrape.com/" +
                book.img["src"].replace("../", "")
            )

            link = (
                "https://books.toscrape.com/catalogue/" +
                book.h3.a["href"]
            )

            products.append({

                "name": title,
                "price": price,
                "rating": rating,
                "availability": availability,
                "image": image,
                "link": link

            })

    # ---------------- Quotes ---------------- #

    elif website == "quotes":

        url = "https://quotes.toscrape.com/"

        response = requests.get(url, headers=HEADERS)

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:

            products.append({

                "name": quote.find("small").text,
                "price": "-",
                "rating": "★★★★★",
                "availability": "Available",
                "image": "https://quotes.toscrape.com/static/img/logo.png",
                "link": url

            })

    # ---------------- DummyJSON ---------------- #

    elif website == "dummy":

        response = requests.get(
            "https://dummyjson.com/products"
        )

        data = response.json()["products"]

        for item in data:

            products.append({

                "name": item["title"],
                "price": f"${item['price']}",
                "rating": round(item["rating"], 1),
                "availability": f"{item['stock']} in stock",
                "image": item["thumbnail"],
                "link": "https://dummyjson.com"

            })

    return products