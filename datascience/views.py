from flask import render_template

from datascience import app, cache
from .tasks.task1 import print_array
from .tasks.task2 import create_general_table, create_summary_table
from .tasks.task4 import create_products_table, aggregate_per_category_1_and_brand, find_top_5, list_cat_m_without_discounts


@app.route('/')
def index():

    return render_template("index.html")


@app.route('/task1')
def do_task1():
    output = print_array()

    return render_template("task1.html",
                           first_line=output[0],
                           second_line=output[1])


@app.route('/task2')
def do_task2():
    general_table = create_general_table()
    summary_table = create_summary_table(general_table)

    return render_template("task2.html",
                           general_table=general_table.to_html(),
                           summary_table=summary_table.to_html())



@app.route('/task4')
@cache.cached(timeout=3600)
def do_task4():
    products = create_products_table()
    aggregated = aggregate_per_category_1_and_brand(products)
    top_5 = find_top_5(products)
    list_cat_m = list_cat_m_without_discounts(products)

    return render_template("task4.html",
                           aggregated=aggregated.to_html(bold_rows=False),
                           top_5=top_5.to_html(bold_rows=False),
                           list_cat_m=list_cat_m)
