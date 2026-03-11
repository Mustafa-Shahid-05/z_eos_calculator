# main file 

import sys
from PyQt5.QtWidgets import QMainWindow , QApplication 
from PyQt5 import QtCore
from PyQt5.uic import loadUi
import numpy as np
from VanDerWaalsEOS import PengRobinsonEOS , SoaveRedlichKwong , RedlichKwong , VanDerWaals
from GazProperties import GazDict
from Converters import PressureConverter , TemperatureConverter





class MainWindow (QMainWindow): 
    def __init__ (self): 
        super().__init__()
        
        loadUi("mainUi.ui",self)
        self.setFixedSize(self.size())
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        
        for gas in GazDict.keys(): 
            self.GazCombo.addItem(gas)
            
        self.calcBtn.clicked.connect(self.calcZ)
    
    
        
    def calcZ (self): 
        Pinput = float(self.Pinput.text())
        Tinput = float (self.Tinput.text())
        P_from_unit = self.PunitCombo.currentText()
        P_to_unit = "pa"
        
        P = PressureConverter(Pinput, P_from_unit, P_to_unit)
        
        T_from_unit = self.TunitCombo.currentText()
        T_to_unit = "K"
        
        T = TemperatureConverter(Tinput, T_from_unit, T_to_unit)
        
        Gaz = self.GazCombo.currentText()
        Pc , Tc , w = GazDict[Gaz]["Pc"] , GazDict[Gaz]["Tc"] , GazDict[Gaz]["w"]
        
        EosDict = {"Peng-Robinson": lambda : PengRobinsonEOS(Pc , Tc , w),
                   "Soave–Redlich–Kwong": lambda : SoaveRedlichKwong(Pc , Tc , w) ,
                   "Redlich–Kwong":lambda : RedlichKwong(Pc , Tc , w), 
                   "Van Der Waals": lambda : VanDerWaals(Pc, Tc)
            }
        selected_eos = self.EOSCombo.currentText()
        EOS = EosDict[selected_eos]()
        
        z = EOS.ZFactors(P , T)
        z = z[z>0]
        
        
        
        self.output_box.append (f"gaz : {Gaz}")
        self.output_box.append (f"Pc = {PressureConverter(Pc , "pa" , P_from_unit):.2f} {P_from_unit}")
        self.output_box.append (f"Tc = {TemperatureConverter(Tc , "K" , T_from_unit):.2f} {T_from_unit}")
        
        if len(z) == 1: 
            self.output_box.append(f"Z  = {z[0]:.4f}")
        else:
            zl = float(np.min(z))
            zv = float(np.max(z))
            self.output_box.append(f"Liquid phase : z = {zl:.4f}")
            self.output_box.append(f"Vapor  phase : z = {zv:.4f}")
        self.output_box.append("-"*30)
        

             
    




def window (): 
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

window()