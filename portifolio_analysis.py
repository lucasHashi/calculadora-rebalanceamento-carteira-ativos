import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

pio.templates.default = "plotly_white"


def load_portifolio_analysis(df_stocks_and_grades):
    st.write('# Portifolio analysis')

    st.write('## Investments by sector and sub sector')

    # fig_sunburst_stocks = load_sunburst_figure(df_stocks_and_grades)
    # st.write(fig_sunburst_stocks)
    
    fig_treemap_stocks = load_treemap_figure(df_stocks_and_grades)
    st.write(fig_treemap_stocks)


def load_sunburst_figure(df):

    df_stocks_hierarchy = calculate_stocks_hierarchy(df)
    st.write(df_stocks_hierarchy)

    fig_sunburst_stocks = go.Figure(go.Sunburst(
        labels=df_stocks_hierarchy['labels'],
        parents=df_stocks_hierarchy['parents'],
        values=df_stocks_hierarchy['values']
    ))

    return fig_sunburst_stocks


def load_treemap_figure(df):
    fig_treemap_stocks = px.treemap(
        df,
        path=['sector', 'sub_sector', 'stock'],
        values='grade',
        hover_name='investment',
    )

    df_stocks_hierarchy = calculate_stocks_hierarchy(df)

    fig_treemap_stocks = go.Figure(
        go.Treemap(
            labels=df_stocks_hierarchy['labels'],
            parents=df_stocks_hierarchy['parents'],
            values=df_stocks_hierarchy['values'],
            customdata = df_stocks_hierarchy['values_text'],
            hovertemplate='<b>%{label} </b> <br>%{customdata}',
        )
    )

    return fig_treemap_stocks


def calculate_stocks_hierarchy(df):
    sectors_duplicated = list(df.loc[df['sector'] == df['sub_sector'], 'sector'])
    df['sector'] = df['sector'].apply(lambda sector: sector + '.' if sector in sectors_duplicated else sector)

    labels = ['Stocks'] + list(df['sector']) + list(df['sub_sector']) + list(df['stock'])
    
    parents = ['']
    parents = parents + ['Stocks'] * len(list(df['sector']))
    parents = parents + list(df['sector'])
    parents = parents + list(df['sub_sector'])

    values = [0] * (len(df) * 2 + 1)
    values = values + list(df['investment'])

    values_text = [df['investment'].sum()]
    values_text = values_text + [df[(df['sector'] == stock) | (df['sub_sector'] == stock) | (df['stock'] == stock)]['investment'].sum() for stock in labels[1:]]
    values_text = ["R$ " + "%.2f" % value for value in values_text]

    df_stocks_hierarchy = pd.DataFrame({'labels': labels, 'parents': parents, 'values': values, 'values_text': values_text})
    df_stocks_hierarchy.drop_duplicates(subset=['parents', 'labels'], inplace=True)
    df_stocks_hierarchy.reset_index(drop=True, inplace=True)

    return df_stocks_hierarchy
