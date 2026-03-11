import numpy as np 


GazDict = { "C1": {"Pc":45.99e5,"Tc":190.56,"w":0.011},      # Methane
            "C2": {"Pc":48.72e5,"Tc":305.32,"w":0.099},      # Ethane
            "C3": {"Pc":42.48e5,"Tc":369.83,"w":0.152},      # Propane
            "iC4":{"Pc":36.40e5,"Tc":407.80,"w":0.184},      # iso-Butane
            "C4": {"Pc":37.96e5,"Tc":425.12,"w":0.193},      # n-Butane
            "iC5":{"Pc":33.80e5,"Tc":460.40,"w":0.227},      # iso-Pentane
            "C5": {"Pc":33.70e5,"Tc":469.70,"w":0.251},      # n-Pentane
            "C6": {"Pc":30.25e5,"Tc":507.60,"w":0.301},      # n-Hexane
            "C7": {"Pc":27.40e5,"Tc":540.20,"w":0.349},      # n-Heptane
            "C8": {"Pc":24.90e5,"Tc":568.70,"w":0.397},      # n-Octane
            "C9": {"Pc":23.00e5,"Tc":594.60,"w":0.444},      # n-Nonane
            "C10":{"Pc":21.10e5,"Tc":617.70,"w":0.490},      # n-Decane
            "C11":{"Pc":19.50e5,"Tc":639.00,"w":0.530},
            "C12":{"Pc":18.20e5,"Tc":658.00,"w":0.574},
            "C13":{"Pc":17.10e5,"Tc":675.00,"w":0.617},
            "C14":{"Pc":16.10e5,"Tc":692.00,"w":0.656},
            "C15":{"Pc":15.20e5,"Tc":706.00,"w":0.697},
            "C16":{"Pc":14.50e5,"Tc":720.00,"w":0.739},
            "C17":{"Pc":13.80e5,"Tc":733.00,"w":0.773},
            "C18":{"Pc":13.20e5,"Tc":746.00,"w":0.800},
            
            "N2": {"Pc":33.98e5,"Tc":126.20,"w":0.037},      # Nitrogen
            "CO2":{"Pc":73.80e5,"Tc":304.20,"w":0.225},      # Carbon dioxide
            "H2S":{"Pc":89.60e5,"Tc":373.20,"w":0.100},      # Hydrogen sulfide
            "H2": {"Pc":12.80e5,"Tc":33.20,"w":-0.220},      # Hydrogen
            "He": {"Pc":2.27e5,"Tc":5.20,"w":-0.390},        # Helium
            "Ar": {"Pc":48.60e5,"Tc":150.90,"w":-0.004},     # Argon
            "O2": {"Pc":50.40e5,"Tc":154.60,"w":0.022},      # Oxygen
            "CO": {"Pc":34.90e5,"Tc":132.90,"w":0.048},      # Carbon monoxide
            
            "H2O":{"Pc":220.60e5,"Tc":647.10,"w":0.344},     # Water
            "NH3":{"Pc":113.30e5,"Tc":405.50,"w":0.256},     # Ammonia
            
            "C2H4":{"Pc":50.40e5,"Tc":282.30,"w":0.086},     # Ethylene
            "C3H6":{"Pc":46.00e5,"Tc":365.60,"w":0.142},     # Propylene
            "C4H8":{"Pc":40.00e5,"Tc":419.50,"w":0.190},     # Butene
            
            "C6H6":{"Pc":48.94e5,"Tc":562.02,"w":0.212},     # Benzene
            "Toluene":{"Pc":41.00e5,"Tc":591.80,"w":0.263},
            "Ethylbenzene":{"Pc":36.00e5,"Tc":617.20,"w":0.305},
            "Xylene":{"Pc":35.00e5,"Tc":616.00,"w":0.320},
            
            "MeOH":{"Pc":80.90e5,"Tc":512.60,"w":0.565},     # Methanol
            "EtOH":{"Pc":61.40e5,"Tc":514.00,"w":0.645},     # Ethanol
            
            "Acetone":{"Pc":47.00e5,"Tc":508.10,"w":0.307},
            "Propionaldehyde":{"Pc":45.00e5,"Tc":497.00,"w":0.280},
            
            "SF6":{"Pc":37.60e5,"Tc":318.70,"w":0.286},
            "SO2":{"Pc":78.80e5,"Tc":430.70,"w":0.256},
            
            "R134a":{"Pc":40.60e5,"Tc":374.20,"w":0.327},
            "R22":{"Pc":49.90e5,"Tc":369.30,"w":0.221},
            "R32":{"Pc":58.20e5,"Tc":351.30,"w":0.276},
            
            "Ne": {"Pc":26.70e5,"Tc":44.40,"w":-0.030},
            "Kr": {"Pc":55.00e5,"Tc":209.40,"w":0.000},
            "Xe": {"Pc":58.40e5,"Tc":289.70,"w":0.003}

}

    



class AntoineSaturatedParameters : 
    def __init__ (self, A , B , C): 
        self.A = A 
        self.B = B 
        self.C = C 
    def Psat (self, Tsat): 
        return (10 ** (self.A - self.B/(Tsat + self.C)))
    def Tsat (self, Psat): 
        return (self.B/(self.A - np.log10(Psat))) - self.C 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
