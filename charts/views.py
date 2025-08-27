# charts/views.py
from django.shortcuts import render
from .models import Product
import plotly.graph_objs as go
import plotly.io as pio
import json

def dashboard(request):
    qs = Product.objects.all().order_by('name')
    context = {
        'names': [p.name for p in qs],
        'clicks': [p.clicks for p in qs],
        'sales': [p.sales for p in qs],
        'click_sales_ratio': [round(p.click_sales_ratio, 3) for p in qs],
        'total_profit': [float(p.total_profit) for p in qs],
        'profit_per_click': [round(p.profit_per_click, 2) for p in qs],
    }
    return render(request, 'charts/dashboard.html', context)

def dashboard_plotly(request):
    products = Product.objects.all().order_by('name')
    product_list = list(products)

    # Veri listeleri
    names       = [p.name for p in product_list]
    clicks      = [p.clicks for p in product_list]
    sales       = [p.sales for p in product_list]
    profits     = [float(p.total_profit) for p in product_list]
    ratios      = [round(p.click_sales_ratio, 3) for p in product_list]
    ppc         = [round(p.profit_per_click, 2) for p in product_list]
    unit_profit = [float(p.unit_profit) for p in product_list]

    # --- Var olan grafikler ---
    top_profit_products = sorted(product_list, key=lambda p: float(p.total_profit), reverse=True)[:5]
    top_profit_names  = [p.name for p in top_profit_products]
    top_profit_values = [float(p.total_profit) for p in top_profit_products]

    fig_top_profit = go.Figure()
    fig_top_profit.add_bar(x=top_profit_names, y=top_profit_values,
                           marker_color='rgba(241, 196, 15, 0.6)')
    fig_top_profit.update_layout(title='En Yüksek Kâr Getiren 5 Ürün',
                                 yaxis_title='Toplam Kâr (₺)', height=350)

    top_click_products = sorted(product_list, key=lambda p: p.clicks, reverse=True)[:5]
    top_click_names  = [p.name for p in top_click_products]
    top_click_values = [p.clicks for p in top_click_products]

    fig_top_clicks = go.Figure()
    fig_top_clicks.add_bar(x=top_click_names, y=top_click_values,
                           marker_color='rgba(52, 152, 219, 0.6)')
    fig_top_clicks.update_layout(title='En Çok Tıklanan 5 Ürün',
                                 yaxis_title='Tıklama', height=350)

    # --- Yeni scatter grafikleri ---
    fig_scatter_cp = go.Figure()
    fig_scatter_cp.add_trace(go.Scatter(
        x=clicks, y=profits, mode='markers',
        marker=dict(size=10, color='rgba(46, 204, 113,0.6)'),
        text=names
    ))
    fig_scatter_cp.update_layout(title='Tıklama vs Toplam Kâr',
                                 xaxis_title='Tıklama', yaxis_title='Toplam Kâr')

    fig_scatter_su = go.Figure()
    fig_scatter_su.add_trace(go.Scatter(
        x=sales, y=unit_profit, mode='markers',
        marker=dict(size=10, color='rgba(231, 76, 60,0.6)'),
        text=names
    ))
    fig_scatter_su.update_layout(title='Satış vs Birim Kâr',
                                 xaxis_title='Satış', yaxis_title='Birim Kâr')

    # --- Histogram grafikleri ---
    fig_hist_ppc = go.Figure()
    fig_hist_ppc.add_histogram(x=ppc, marker_color='rgba(155, 89, 182,0.6)')
    fig_hist_ppc.update_layout(title='Kâr / Click Dağılımı',
                               xaxis_title='Kâr/Click', yaxis_title='Frekans')

    fig_hist_unit = go.Figure()
    fig_hist_unit.add_histogram(x=unit_profit, marker_color='rgba(52, 73, 94,0.6)')
    fig_hist_unit.update_layout(title='Birim Kâr Dağılımı',
                                xaxis_title='Birim Kâr', yaxis_title='Frekans')

    # Tablo verisi
    table_data = [
        {
            'id'   : p.product_id,
            'name' : p.name,
            'clicks': p.clicks,
            'sales': p.sales,
            'ratio': f"{p.click_sales_ratio:.3f}",
            'cost': f"{p.cost:.2f}",
            'sales_price': f"{p.sales_price:.2f}",
            'unit_profit': f"{p.unit_profit:.2f}",
            'total_profit': f"{p.total_profit:.2f}",
            'ppc': f"{p.profit_per_click:.2f}",
        }
        for p in product_list
    ]

    context = {
        'top_profit': json.dumps(fig_top_profit, cls=pio.utils.PlotlyJSONEncoder),
        'top_clicks': json.dumps(fig_top_clicks, cls=pio.utils.PlotlyJSONEncoder),
        'scatter_cp': json.dumps(fig_scatter_cp, cls=pio.utils.PlotlyJSONEncoder),
        'scatter_su': json.dumps(fig_scatter_su, cls=pio.utils.PlotlyJSONEncoder),
        'hist_ppc':   json.dumps(fig_hist_ppc,   cls=pio.utils.PlotlyJSONEncoder),
        'hist_unit':  json.dumps(fig_hist_unit,  cls=pio.utils.PlotlyJSONEncoder),
        'table_data': table_data,
    }
    return render(request, 'charts/dashboard_plotly.html', context)
