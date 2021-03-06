#!/usr/bin/env python
# -*- coding: utf-8 -*-

import HistAcad
try:
  import pygtk
  pygtk.require('2.0')
except:
  pass
try:
  import gtk
  import gtk.glade
except:
  print('GTK not available')
  sys.exit(1)

class GUI:

  def __init__(self):
    self.gladefile = "main.glade"
    self.builder = gtk.Builder()
    self.builder.add_from_file(self.gladefile)
    self.builder.connect_signals(self)
    
    self.window = self.builder.get_object("mainWindow")
    self.help = self.builder.get_object("helpWindow")
    self.opt1 = self.builder.get_object("opt1Window")
    self.opt2 = self.builder.get_object("opt2Window")
    self.papa = self.builder.get_object("papaLabel")
    self.prom = self.builder.get_object("promLabel")
    self.data = self.builder.get_object("dataLabel")
    self.error = self.builder.get_object("errorLabel")
    
    self.promBtn = self.builder.get_object("promCheck")             
    self.optb1 = self.builder.get_object("opt1Button")
    self.optb2 = self.builder.get_object("opt2Button")
    self.optb3 = self.builder.get_object("opt3Button")
    self.adj = gtk.Adjustment(1, 1, 8, 1, 1)
    self.adjCred1 = gtk.Adjustment(0, 0, 10, 1, 1)
    self.adjCred2 = gtk.Adjustment(0, 0, 10, 1, 1)
    self.adjCred3 = gtk.Adjustment(0, 0, 10, 1, 1)
    self.adjCred4 = gtk.Adjustment(0, 0, 10, 1, 1)
    self.adjCred5 = gtk.Adjustment(0, 0, 10, 1, 1)
    self.adjCred6 = gtk.Adjustment(0, 0, 10, 1, 1)
    self.adjCred7 = gtk.Adjustment(0, 0, 10, 1, 1)
    self.adjCred8 = gtk.Adjustment(0, 0, 10, 1, 1)    
    self.adjNota1 = gtk.Adjustment(0.0, 0.0, 5.0, 0.1, 0.1)
    self.adjNota2 = gtk.Adjustment(0.0, 0.0, 5.0, 0.1, 0.1)
    self.adjNota3 = gtk.Adjustment(0.0, 0.0, 5.0, 0.1, 0.1)
    self.adjNota4 = gtk.Adjustment(0.0, 0.0, 5.0, 0.1, 0.1)
    self.adjNota5 = gtk.Adjustment(0.0, 0.0, 5.0, 0.1, 0.1)
    self.adjNota6 = gtk.Adjustment(0.0, 0.0, 5.0, 0.1, 0.1)
    self.adjNota7 = gtk.Adjustment(0.0, 0.0, 5.0, 0.1, 0.1)
    self.adjNota8 = gtk.Adjustment(0.0, 0.0, 5.0, 0.1, 0.1)
    self.spinBtn = self.builder.get_object("nButton")
    self.spinBtn.configure(self.adj, 1, 0)
    
    self.builder.get_object("credEntry1").configure(self.adjCred1, 0, 0)
    self.builder.get_object("credEntry2").configure(self.adjCred2, 1, 0)
    self.builder.get_object("credEntry3").configure(self.adjCred3, 1, 0)
    self.builder.get_object("credEntry4").configure(self.adjCred4, 1, 0)
    self.builder.get_object("credEntry5").configure(self.adjCred5, 1, 0)
    self.builder.get_object("credEntry6").configure(self.adjCred6, 1, 0)
    self.builder.get_object("credEntry7").configure(self.adjCred7, 1, 0)
    self.builder.get_object("credEntry8").configure(self.adjCred8, 1, 0)
    self.builder.get_object("notaEntry1").configure(self.adjNota1, 0.1, 1)
    self.builder.get_object("notaEntry2").configure(self.adjNota2, 0.1, 1)
    self.builder.get_object("notaEntry3").configure(self.adjNota3, 0.1, 1)
    self.builder.get_object("notaEntry4").configure(self.adjNota4, 0.1, 1)
    self.builder.get_object("notaEntry5").configure(self.adjNota5, 0.1, 1)
    self.builder.get_object("notaEntry6").configure(self.adjNota6, 0.1, 1)
    self.builder.get_object("notaEntry7").configure(self.adjNota7, 0.1, 1)
    self.builder.get_object("notaEntry8").configure(self.adjNota8, 0.1, 1)
    
    self.nombre = []
    self.pregrado = ''
    self.codigos = []
    self.asignaturas = []
    self.creditos = []
    self.n = []
    self.notas = []
    
    self.filepath = None
    self.flag = False
    
    self.window.show()

  def on_mainWindow_destroy(self, object, data=None):
    print "Quit main window"
    gtk.main_quit()
    
  def on_goButton_clicked(self, object, data=None):
    print "Init button pressed"
    if self.optb1.get_active():
      self.error.set_text('')
      self.builder.get_object("codLabel").set_text('')
      self.builder.get_object("codEntry1").hide()
      self.spinBtn.set_value(1)
      for self.c in range(2, 9):
        self.builder.get_object("codEntry{}".format(str(self.c))).hide()
        self.builder.get_object("credEntry{}".format(str(self.c))).hide()
        self.builder.get_object("notaEntry{}".format(str(self.c))).hide()
        self.builder.get_object("n{}Label".format(str(self.c))).set_text('')

        self.builder.get_object("codEntry{}".format(str(self.c))).set_text('')
        self.builder.get_object("credEntry{}".format(str(self.c))).set_value(0)
        self.builder.get_object("notaEntry{}".format(str(self.c))).set_value(0.0)
      
      self.builder.get_object("hbuttonbox5").show()
      self.builder.get_object("hbuttonbox4").show()
      self.builder.get_object("errorLabel").show()
      self.builder.get_object("hseparator1").show()
      
      self.opt1.show()      
    elif self.optb2.get_active(): self.opt2.show()
    elif self.optb3.get_active():
      self.builder.get_object("hbuttonbox5").hide()
      self.builder.get_object("hbuttonbox4").hide()
      self.builder.get_object("errorLabel").hide()
      self.builder.get_object("hseparator1").hide()

      self.opt1.show()
    
  def on_opt1Window_delete_event(self, object, data=None):
    print "Quit option 1 menu"
    self.opt1.hide()
    return True
    
  def on_opt2Window_delete_event(self, object, data=None):
    print "Quit option 2 menu"
    self.opt2.hide()
    return True

  def gtk_widget_show(self, object, data=None):
    print "Help menu selected"
    self.help.show() 
    
  def on_helpWindow_delete_event(self, object, data=None):
    print "Quit help menu"
    self.help.hide()
    return True
    
  def on_cancelButton_clicked(self, button):
    print "Quit file chooser"
    self.fileDialog.hide()
    return True
    
  def on_nButton_value_changed(self, object):
    print "Spinbutton value changed"
    for self.c in range(1, self.spinBtn.get_value_as_int() + 1):
      if self.promBtn.get_active():
        self.builder.get_object("codEntry{}".format(str(self.c))).show()
      self.builder.get_object("credEntry{}".format(str(self.c))).show()
      self.builder.get_object("notaEntry{}".format(str(self.c))).show()
      self.builder.get_object("n{}Label".format(str(self.c))).set_text(str(self.c))
    for self.c in range(self.spinBtn.get_value_as_int() + 1, 9):
      if self.promBtn.get_active():
        self.builder.get_object("codEntry{}".format(str(self.c))).hide()
      self.builder.get_object("credEntry{}".format(str(self.c))).hide()
      self.builder.get_object("notaEntry{}".format(str(self.c))).hide()
      self.builder.get_object("n{}Label".format(str(self.c))).set_text('')
      self.builder.get_object("codEntry{}".format(str(self.c))).set_text('')
      self.builder.get_object("credEntry{}".format(str(self.c))).set_value(0)
      self.builder.get_object("notaEntry{}".format(str(self.c))).set_value(0.0)
          
  def on_browseButton_clicked(self, object):
    print "File Dialog opened"
    self.fileChooser = gtk.FileChooserDialog("Seleccione un archivo:", None, gtk.FILE_CHOOSER_ACTION_OPEN, (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OK, gtk.RESPONSE_OK))
    self.response = self.fileChooser.run()
    if self.response == gtk.RESPONSE_OK:
      self.filepath = self.fileChooser.get_filename()
      self.fileChooser.destroy()
      print "Selected filepath: %s" % self.filepath
      if HistAcad.Formato(self.filepath):
        self.error.set_text('')
        self.nombre, self.pregrado, self.codigos, self.asignaturas, self.creditos, self.n, self.notas = HistAcad.Importar('Output')
        self.papa.set_text("PAPA: " + str(HistAcad.PAPA(self.creditos, self.notas)))
        self.prom.set_text("Promedio: " + str(HistAcad.Promedio(self.codigos, self.creditos, self.n, self.notas)))
        self.data.set_text(self.nombre + "\n" + self.pregrado)
        self.flag = True
      else:
        self.error.set_text("Error: Seleccione otro archivo")
        self.data.set_text("")
        self.papa.set_text("PAPA: 0.0")
        self.prom.set_text("Promedio: N/A")          
    else:
      self.fileChooser.destroy()
    self.filepath = None
    return True
  	        
  def on_promCheck_toggled(self, button):
    if self.promBtn.get_active():
      self.builder.get_object("codLabel").show()
      for self.c in range(1, self.spinBtn.get_value_as_int() + 1):
        self.builder.get_object("codEntry{}".format(str(self.c))).show()
    else:
      self.builder.get_object("codLabel").hide()
      for self.c in range(1, self.spinBtn.get_value_as_int() + 1):
        self.builder.get_object("codEntry{}".format(str(self.c))).hide()
        self.builder.get_object("codEntry{}".format(str(self.c))).set_text('')
        
  def on_clearButton_clicked(self, button):
    self.nombre, self.pregrado, self.codigos, self.asignaturas, self.creditos, self.n, self.notas = '', '', [], [], [], [], []
    self.data.set_text('')
    self.error.set_text('')
    self.papa.set_text('PAPA: 0.0')
    if self.promBtn.get_active():
      self.prom.set_text('Promedio: 0.0')
    elif not self.promBtn.get_active():
      self.prom.set_text('Promedio: N/A')
    for self.c in range(1, 9):
      self.builder.get_object("codEntry{}".format(str(self.c))).set_text('')
      self.builder.get_object("credEntry{}".format(str(self.c))).set_value(0)
      self.builder.get_object("notaEntry{}".format(str(self.c))).set_value(0.0)
   
  def on_calcButton_clicked(self, button):
    print "Calc button pressed"
    self.cods = []
    self.creds = []
    self.grads = []
    if self.opt1Button.get_active():
      for self.c in range(1, 9):
        self.cod = self.builder.get_object("codEntry{}")
  	    self.cred = self.builder.get_object("credEntry{}".format(str(self.c)))
  	    self.grad = self.builder.get_object("notaEntry{}".format(str(self.c)))
  	    if self.cred.get_value() > 0 or self.grad.get_value() > 0.0:
  	      self.cods.append(self.cod.get_text())
  	      self.creds.append(self.cred.get_value_as_int())
  	      self.grads.append(self.grad.get_value())
  	      print self.cods, self.creds, self.grads
  	      if self.promBtn.get_active():
  	        if any(c.isalpha() for c in self.cod.get_text()) and self.cod.get_text() != '':
  	          self.flag = False
  	        else:
  	          self.flag = True
  	      else:
  	        self.papa.set_text("PAPA: " + str(HistAcad.Proyectar(self.creditos, self.creds, self.notas, self.grads)))
    elif self.opt3Button.get_active():
      for self.c in range(1, 9):
        # self.cod = self.builder.get_object("codEntry{}".format(str(self.c)))
  	    self.cred = self.builder.get_object("credEntry{}".format(str(self.c)))
  	    self.grad = self.builder.get_object("notaEntry{}".format(str(self.c)))
  	    if self.cred.get_value() > 0 or self.grad.get_value() > 0.0:
  	      self.cods.append(self.cod.get_text())
  	      self.creds.append(self.cred.get_value_as_int())
  	      self.grads.append(self.grad.get_value())
  	      print self.cods, self.creds, self.grads
  	      if self.promBtn.get_active():
  	        if any(c.isalpha() for c in self.cod.get_text()) and self.cod.get_text() != '':
  	          self.flag = False
  	        else:
  	          self.flag = True
  	      else:
  	        self.papa.set_text("PAPA: " + str(HistAcad.PAPA(self.creds, self.grads)))
 	    
if __name__ == "__main__":
  main = GUI()
  gtk.main()
