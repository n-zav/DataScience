import pandas as pd


def create_products_table():
    """
    reads data from a file
    """

    products = pd.read_csv("http://www.semtrack.de/e?i=f654793ba2b71c63e9288fa3c02be7662c5d91c1",
                           sep=None,
                           engine='python')

    return products


def aggregate_per_category_1_and_brand(products):
    """
    Aggregates number of products per category_1 and brand
    """
    aggregated = products.groupby(['category_1', 'brand']).size()

    return aggregated.to_frame()


def find_top_5(products):
    """
    Finds top 5 most expensive products with name, price and description
    """
    top_5 = products[['product_name', 'price', 'description']]
    top_5 = top_5.sort(columns='price', ascending=False)[:5]

    return top_5


def list_cat_m_without_discounts(products):
    """
    creates a list of cat_m not offering discounts
    """
    grouped = products.fillna(0)
    grouped = grouped.loc[grouped['discount'] == 0]
    grouped = grouped['cat_m'].drop_duplicates()
    list_cat_m = list(grouped)

    return list_cat_m
