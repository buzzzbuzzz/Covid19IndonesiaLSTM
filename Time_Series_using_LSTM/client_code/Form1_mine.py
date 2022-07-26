from ._anvil_designer import Form1_mineTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import plotly.graph_objects as go
import anvil.media


class Form1_mine(Form1_mineTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.button_1.enabled = False
    self.button_4.enabled = False
    self.button_5.enabled = False
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    #rms = anvil.server.call('LSTM_run', anvil.server.call('get_data'))
    rms, mape, figure, data, layout = anvil.server.call('LSTM_run', 'yes', self.text_box_1.text, self.text_box_2.text)
    #app_tables.table_use.add_row(name= "lossplot", media_obj=lossplot)
    #app_tables.table_use.add_row(name= "predtestplot", media_obj=predtestplot)
    self.RMSE_lbl.text = f"{rms}"
    self.MAPE_lbl.text = f"{mape}"
    #self.image_2.source = lossplot
    self.plot_1.figure = figure
    self.plot_1.data = data
    self.plot_1.layout = layout
    self.button_5.enabled = True
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    tsplot = anvil.server.call('LSTM_timeseriesplot', 'yes')
    self.image_1.source = tsplot
    
    tsmine = app_tables.table_use.get(name= "tsplot_mine")
    tsmine['media_obj'] = tsplot
    self.button_3.visible = True
    self.button_4.enabled = True

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    orig = app_tables.table_use.get(name = "tsplot_mine")['media_obj']
    anvil.media.download(anvil.BlobMedia('images/jpg', orig.get_bytes(), name="tsplot.jpg"))

  def button_4_click(self, **event_args):
    PACFplot = anvil.server.call('LSTM_PACFplot', 'yes')
    self.image_2.source = PACFplot
    PACFmine = app_tables.table_use.get(name= "PACFplot_mine")
    PACFmine['media_obj'] = PACFplot
    self.button_1.enabled = True
    pass

  def text_box_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def button_2_hide(self, **event_args):
    """This method is called when the Button is removed from the screen"""
    pass

  def plot_1_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass

  def button_5_click(self, **event_args):
    x_media, figure, data, layout = anvil.server.call('Pred_run', 'yes', self.text_box_1.text, self.text_box_2.text,self.text_box_3.text)
    self.plot_2.figure = figure
    self.plot_2.data = data
    self.plot_2.layout = layout
    
    preds = app_tables.table_use.get(name= "pred")
    preds['media_obj'] = x_media
    self.button_6.visible = True

  def button_6_click(self, **event_args):
    orig = app_tables.table_use.get(name = "pred")['media_obj']
    anvil.media.download(anvil.BlobMedia('text/csv', orig.get_bytes(), name="covidpred.csv"))


  def text_box_3_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass






