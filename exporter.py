import os
import pandas as pd


OUTPUT_FOLDER = "output"


def create_output_folder():

    if not os.path.exists(OUTPUT_FOLDER):

        os.makedirs(OUTPUT_FOLDER)


def export_csv(products):

    create_output_folder()

    df = pd.DataFrame(products)

    path = os.path.join(
        OUTPUT_FOLDER,
        "products.csv"
    )

    df.to_csv(

        path,

        index=False,

        encoding="utf-8"

    )

    return path


def export_excel(products):

    create_output_folder()

    df = pd.DataFrame(products)

    path = os.path.join(
        OUTPUT_FOLDER,
        "products.xlsx"
    )

    df.to_excel(

        path,

        index=False,

        engine="openpyxl"

    )

    return path