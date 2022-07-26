from ._anvil_designer import dashboardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Form1 import Form1
from ..Form1_mine import Form1_mine
import anvil.media

class dashboard(dashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.ass()
    # Any code you write here will run when the form opens.
    plots = anvil.server.call('get_plots')
    self.plot_1.figure=plots['plot1']
    self.plot_2.figure=plots['plot2']
    self.plot_3.figure=plots['plot3']
    self.plot_4.figure=plots['plot4']
#     fig1 = anvil.server.call('create_plots')
#     self.plot_1.figure=fig1
#     fig2 = anvil.server.call('create_plots2')
#     self.plot_2.figure=fig2
#     fig3 = anvil.server.call('create_plots3')
#     self.plot_3.figure=fig3
#     fig4 = anvil.server.call('create_plots4')
#     self.plot_4.figure=fig4

#     fig5 = anvil.server.call('create_plots5')
#     self.plot_5.figure=fig5
#     mxpos= anvil.server.call('info_dat')
#     self.highest_pos_lbl.text =mxpos
#     fig4 = anvil.server.call('create_plots4')
#     self.plot_4.figure=fig4
################### Dashboard Info ############################################
  def ass(self):
    # self.plot_1.data = go.Bar(y=[100,400,200,300,500])
    dfa= anvil.server.call('get_dash')
    conf = sorted(dfa, key=lambda x: x['tanggal'], reverse=True)[0]
    conf1 = sorted(dfa, key=lambda x: x['tanggal'], reverse=True)[1]
    self.confirmcase_lbl.text ="{:,d}".format(conf['confirm'])
    self.activecase_lbl.text ="{:,d}".format(conf['active'])
    self.recovercase_lbl.text ="{:,d}".format(conf['recovered'])
    self.deathcase_lbl.text ="{:,d}".format(conf['Death'])
    self.tanggal_lbl.text =conf['tanggal']
#   Menghitung kenaikan kasus
    diffs_conf =(conf['confirm'],lambda x: x[0] - x[1])
    self.conf_selisih_lbl.text ="{:,d} Cases".format(conf['confirm']-conf1['confirm'])
    self.recover_selisih_lbl.text ="{:,d} Case".format(conf['recovered']-conf1['recovered'])
    self.death_selisih_lbl.text ="{:,d} Case".format(conf['Death']-conf1['Death'])
    self.activecase_selisih_lbl.text ="{:,d} Case".format(conf['active']-conf1['active'])
###################################################################################    

  
###################LAST PANEL##########################
#     media_obj = anvil.server.call('make_plot')
#     self.image_1.source = media_obj
#     self.download_link.url = media_obj

  def plot_1_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass

  def plot_2_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass

  def plot_3_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass


  def plot_4_click(self, points, **event_args):
    print(f"User hovered over x:{points[0]['y']}")
    passd








 





#######################################################