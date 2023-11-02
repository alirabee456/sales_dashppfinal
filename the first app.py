

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd





data=pd.read_excel("C:/Users/fawzy/Desktop/rev/sales.xlsx")





d=data[['Sales','Discounts']].groupby(data['Product']).sum().reset_index().sort_values(by='Sales',ascending=True)










fig=px.bar(d,y='Product',x='Sales',title='sum of Sales by product')





s=data['Discounts'].groupby(data['Discount Band']).sum().reset_index().iloc[0:3,:]





def W(df):
    if df['Country']=='Canada':
        return 'CAN'
    elif df['Country']=='France':
        return 'FRA'
    elif df['Country']=='United States of America':
        return 'USA'
    elif df['Country']=='Germany':
        return 'DEU'
    else:
        return 'MEX'
data['iso_alpha']=data.apply(W,axis=1)




d1=data.groupby(['Country','iso_alpha'])['Profit'].sum().reset_index()






fig1=px.scatter_geo(d1,locations='iso_alpha',projection='orthographic',color='Country',hover_data='Profit',size='Profit',title="sum of profits by country")




f=data['Sales'].groupby(data['Date']).sum().reset_index()






fig2=px.line(f,x='Date',y='Sales',title='sum of sales by months')





r=data['Profit'].groupby(data['Date']).sum().reset_index()






fig3=px.line(r,x='Date',y='Profit',title='sum of profits by months')






e=data['Sales'].groupby(data['Segment']).sum().reset_index().sort_values(by='Sales',ascending=False)




fig4=px.bar(e,x='Segment',y='Sales',title='sum of sales by segment')






import dash_bootstrap_components as dbc
total_sales=round((data['Sales'].sum()/1000000),2)
total_units=round((data['Units Sold'].sum()/1000000),2)
total_cogs=round((data['COGS'].sum()/1000000),2)
total_profits=round((data['Profit'].sum()/1000000),2)
profit_percentage=round(((data['Profit'].sum()/data['Sales'].sum())*100),2)

app = Dash(__name__)
server=app.server
app.layout=html.Div(children=[
    
    html.H1(children='Sales dashboard',style={'text-align': 'center'}),
        html.Div(children=''''''),
    dbc.Card(dbc.CardBody([html.H4('sum of sales',className='card-title',style={'font-size': '24px'}),
                          html.H2(f" {total_sales}M")],style={'width': '18rem', 'position': 'absolute', 'top': '30px', 'left': '100px', 'padding': '10px','border-radius': '10px'}
)
        
    ),
     dbc.Card(dbc.CardBody([html.H4('sum of units sold',className='card-title',style={'font-size': '24px'}),
                          html.H2(f" {total_units}M")],style={'width': '18rem', 'position': 'absolute', 'top': '30px', 'left': '400px', 'padding': '10px','border-radius': '10px'}
)
        
    ),
     dbc.Card(dbc.CardBody([html.H4('sum of COGS',className='card-title',style={'font-size': '24px'}),
                          html.H2(f" {total_cogs}M")],style={'width': '18rem', 'position': 'absolute', 'top': '30px', 'left': '700px', 'padding': '10px','border-radius': '10px'}
)
        
    ),
     dbc.Card(dbc.CardBody([html.H4('sum of profits',className='card-title',style={'font-size': '24px'}),
                          html.H2(f" {total_profits}M")],style={'width': '18rem', 'position': 'absolute', 'top': '30px', 'left': '1000px', 'padding': '10px','border-radius': '10px'}
)
        
    ),
     dbc.Card(dbc.CardBody([html.H4('profits%',className='card-title',style={'font-size': '24px'}),
                          html.H2(f" {profit_percentage}%")],style={'width': '18rem', 'position': 'absolute', 'top': '30px', 'left': '1300px', 'padding': '10px','border-radius': '10px'}
)
        
    ),
    dcc.Graph(id='my graph',figure=fig,style={'width':'25%','height':'300px','backgroundColor':'#566573',
                                                                                          'position':'absolute','top':'500px','left':'50px','borderRadius':'50px','overflow':'hidden'}),
    dcc.Graph(id='second',figure=px.pie(s,names='Discount Band',values='Discounts',title="sum of discount by dicount band"),style={'width':'20%','height':'300px','backgroundColor':'#566573',
                                                                                          'position':'absolute','top':'170px','left':'50px','borderRadius':'50px','overflow':'hidden'}),
    
     dcc.Graph(id='second1',figure=fig1,style={'width':'30%','height':'300px','backgroundColor':'#566573','position':'absolute','top':'170px','left':'400px','borderRadius':'50px','overflow':'hidden'}),
     dcc.Graph(id='second2',figure=fig2,style={'width':'40%','height':'300px','backgroundColor':'#566573','position':'absolute','top':'170px','left':'900px','borderRadius':'50px','overflow':'hidden'}),
     dcc.Graph(id='second3',figure=fig3,style={'width':'40%','height':'300px','backgroundColor':'#566573','position':'absolute','top':'500px','left':'930px','borderRadius':'50px','overflow':'hidden'}),
     dcc.Graph(id='second4',figure=fig4,style={'width':'25%','height':'300px','backgroundColor':'#566573','position':'absolute','top':'500px','left':'480px','borderRadius':'50px','overflow':'hidden'})



    
    ],style={'backgroundColor':'gold'})

if __name__=='__main__':
    app.run(debug=False)

 