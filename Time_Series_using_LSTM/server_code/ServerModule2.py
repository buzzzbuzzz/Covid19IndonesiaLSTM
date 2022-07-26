import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import io
import json
from datetime import datetime
import anvil.media
#import psycopg2 
import anvil.http
import matplotlib.pyplot as plt
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
######################### Plotting Dashboard#########################
@anvil.server.callable
def get_dash():
  return app_tables.covid_dash.search()

def csv_to_df(f):
  d=app_tables.data.get(file_name=f)['file']
  dfa=pd.read_csv(io.BytesIO(d.get_bytes()),sep=';')
  return dfa

# def csv(sa):
#   da=app_tables.data.get(file_name=sa)['file']
#   dfaa=pd.read_csv(io.BytesIO(da.get_bytes()),sep=',')
#   return dfaa

def prepare_cov_data():
  covup_df = csv_to_df('covid19')
  covup_df['Date']= pd.to_datetime(covup_df['Date'],format='%d/%m/%Y')
  return covup_df

# @anvil.server.callable
# def who_cov_dat():
#   who_df = csv('vacjuly')
#   return who_cov_dat

##################################################INDONESIA COVID-19#######################################
def create_plots():
  covup_df= prepare_cov_data()
  fig1 =px.line(covup_df,x='Date',y=covup_df["Positif_kumulatif"])
  fig1.update_xaxes(title_text='Date')
  fig1.update_yaxes(title_text='Cumulative Cases')  
  fig1.update_layout(
    template="plotly_white",
    xaxis_rangeslider_visible=True
    
  )
  fig1.show()
  return fig1
def create_plots2():
  covup_df= prepare_cov_data()
  fig2 = px.line(covup_df, x = "Date", y = "Sembuh_kumulatif")
  fig2.update_xaxes(title_text='Date')
  fig2.update_yaxes(title_text='Cumulative Cases')
  fig2.update_layout(
    template="plotly_white",
    xaxis_rangeslider_visible=True
  )
  fig2.show()
  return fig2
def create_plots3():
  covup_df= prepare_cov_data()
  fig3 =px.line(covup_df, x = "Date", y = "Meninggal_Dunia_kumulatif")
  fig3.update_xaxes(title_text='Date')
  fig3.update_yaxes(title_text='Cumulative Cases')
  fig3.update_layout(
    template="plotly_white",
    xaxis_rangeslider_visible=True

  )
  fig3.show()
  return fig3
def create_plots4():
  covup_df= prepare_cov_data()
  fig4 = go.Figure()
  fig4.add_trace(go.Scatter(x=covup_df['Date'], y=covup_df['New_Positive'],
                    mode='lines',
                    name='Active Case'))
  fig4.add_trace(go.Scatter(x=covup_df['Date'], y=covup_df['Sembuh'],
                    mode='lines',
                    name='Recover'))
  fig4.add_trace(go.Scatter(x=covup_df['Date'], y=covup_df['Meninggal_Dunia'],
                    mode='lines', name='Death'))
  fig4.update_xaxes(title_text='Date')
  fig4.update_yaxes(title_text='Daily Cases')
  
  fig4.update_layout(
    template="plotly_white",
    xaxis_rangeslider_visible=True
  )
  fig4.show()
  return fig4
@anvil.server.callable
def get_plots():
  result = {
    "plot1": create_plots(),
    "plot2": create_plots2(),
    "plot3": create_plots3(),
    "plot4": create_plots4(),
  }
  return result
#################################################################################################################
# @anvil.server.callable
# def create_plots5():
#   who_df= who_cov_dat()
#   fig5 =go.Figure([go.Bar(x=who_df["country"], y=who_df["totalvac"])])
#   fig5.update_xaxes(title_text='Country')
#   fig5.update_yaxes(title_text='Total Vaccination Given')
# #   fig5.update_layout(
# #     template="plotly_white",
# #     xaxis_rangeslider_visible=True

# #   )
#   fig5.show()
#   return fig5