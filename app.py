from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def dashboard():

    df = pd.read_csv('sales_data.csv')

    total_sales = df['Sales'].sum()

    product_sales = df.groupby('Product')['Sales'].sum().reset_index()

    fig = px.bar(
        product_sales,
        x='Product',
        y='Sales',
        title='Product Wise Sales'
    )

    graph_html = fig.to_html(full_html=False)

    return render_template(
        'dashboard.html',
        total_sales=total_sales,
        graph_html=graph_html
    )

if __name__ == '__main__':
    app.run(debug=True)