from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Form1 import Form1
from ..Form1_mine import Form1_mine
from ..dashboard import dashboard
class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.ass()
#     self.plot_cov()
  def navigate(self, active_link, form):
    for i in [self.dashb,self.link_2, self.link_3]:
      i.foreground = 'theme:Primary 700'
    active_link.foreground = 'theme:Secondary 500'
    self.content_panel.clear()
    self.content_panel.add_component(form, full_width_row=True)
  
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""    
    open_form('Form3', my_parameter="an_argument")
    self.link_1.foreground = 'theme:Secondary 500'

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.navigate(self.link_2, Form1())
    
  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.navigate(self.link_3, Form1_mine())

  def link_6_click(self, **event_args):
    self.navigate(self.link_2, Form1()) 
    
  
  def link_7_click(self, **event_args):
    self.navigate(self.dashb,dashboard())   
    
  def link_8_click(self, **event_args):
    self.navigate(self.dashb,dashboard())   

    
  def plot_1_click(self, points, **event_args):
    # self.plot_1.data = go.Bar(y=[100,400,200,300,500])
    pass
################### Dashboard Info ############################################
  def ass(self):
    dfa = anvil.server.call('get_dash')
    conf = sorted(dfa, key=lambda x: x['tanggal'], reverse=True)[0]
    conf1 = sorted(dfa, key=lambda x: x['tanggal'], reverse=True)[1]
    self.confirmcase_lbl.text ="{:,d}".format(conf['confirm'])
    self.activecase_lbl.text ="{:,d}".format(conf['active'])
    self.recovercase_lbl.text ="{:,d}".format(conf['recovered'])
    self.deathcase_lbl.text ="{:,d}".format(conf['Death'])
    self.tanggal_lbl.text =conf['tanggal']
#   Menghitung kenaikan kasus
    diffs_conf =(conf['confirm'],lambda x: x[0] - x[1])
    self.conf_selisih_lbl.text ="{:,d} Confirm Cases".format(conf['confirm']-conf1['confirm'])
    self.recover_selisih_lbl.text ="{:,d} Recovered Case".format(conf['recovered']-conf1['recovered'])
    self.death_selisih_lbl.text ="{:,d} Death Case".format(conf['Death']-conf1['Death'])
    self.activecase_selisih_lbl.text ="{:,d} Active Case".format(conf['active']-conf1['active'])
###################################################################################    


  def deathcase_lbl_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    pass

# Covid-19 Plot
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    cov_pos_plot = anvil.server.call('positive_cum', 'yes')
    self.image_3.source = cov_pos_plot
    
    covcummine = app_tables.table_use.get(name= "cov_pos_plot_mine")
    covcummine['media_obj'] = cov_pos_plot
    self.button_1.visible = True
    
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    tsplot = anvil.server.call('LSTM_timeseriesplot', 'yes')
    self.image_1.source = tsplot
    
    tsmine = app_tables.table_use.get(name= "tsplot_mine")
    tsmine['media_obj'] = tsplot
    self.button_3.visible = True

























