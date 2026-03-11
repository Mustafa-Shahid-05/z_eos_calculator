
# Import ...
import numpy as np
from scipy.optimize import fsolve

# Van Der Waals 

class VanDerWaals : 
    def __init__ (self , Pc , Tc , R = 8.314): 
        self.Pc = Pc 
        self.Tc = Tc 
        self.R  = R
        self.a  = 0.421875 * ((R * Tc)**2/Pc)
        self.b  = 0.125 * (R*Tc/Pc)
    def pressure (self , T , v): 
        P_rep = (self.R * T)/(v - self.b)
        P_att = self.a / (v**2)
        P = P_rep - P_att 
        return P 
    def temperature (self,P , v): 
        def f(T): 
            P_rep = (self.R * T)/(v - self.b)
            P_att = self.a / (v**2)
            return P_rep - P_att - P 
        T_guess = P * v / self.R  
        return fsolve (f , T_guess)[0] 
    def ZFactors(self, P, T):
        A = (self.a * P) / (self.R**2 * T**2)
        B = (self.b * P) / (self.R * T)
        # Correct Form: Z^3 - (1 + B)Z^2 + AZ - AB = 0
        coef = [1, -(1 + B), A, -A * B]
        roots = np.roots(coef)
        return np.sort(np.real(roots[np.isreal(roots)]))
            
    def volumes(self, P, T):
        Zs = self.ZFactors(P, T)
        v = Zs * self.R * T / P
        return v
        
# Redlich Kwong (RK) 1945

class RedlichKwong : 
    def __init__ (self , Pc , Tc , R = 8.314): 
        self.Pc = Pc 
        self.Tc = Tc 
        self.R  = R
        self.a  = 0.42748 * ((R * Tc)**2/Pc)
        self.b  = 0.08846 * (R * Tc/Pc)
    def alpha(self,T): 
        return self.a / np.sqrt (T/self.Tc)
    def pressure (self,T , v):
        alpha_T = self.alpha(T)
        P_rep = (self.R * T)/(v - self.b)
        P_att = alpha_T / (v * (v+self.b))
        P = P_rep - P_att
        return P 
    def temperature (self , P , v): 
        def f(T): 
            alpha_T = self.alpha(T)
            P_rep = (self.R * T)/(v - self.b)
            P_att = alpha_T / (v*(v+self.b))
            return P_rep - P_att - P
        T_guess = P * v / self.R
        return fsolve(f , T_guess)[0]
    def ZFactors(self, P, T):
        
        A = (self.a * P) / (self.R**2 * T**2.5) 
        B = (self.b * P) / (self.R * T)
        #  Z^3 - Z^2 + (A - B - B^2)Z - AB = 0
        coef = [1, -1, (A - B - B**2), -A * B]
        roots = np.roots(coef)
        return np.sort(np.real(roots[np.isreal(roots)]))
    def volumes(self, P, T):
        Zs = self.ZFactors(P, T)
        v = Zs * self.R * T / P
        return v
    
# Soave Redlich Kwong (SRK) 1972

class SoaveRedlichKwong : 
    def __init__ (self,Pc , Tc ,w , R = 8.314):
        self.Pc = Pc
        self.Tc = Tc 
        self.w  = w
        self.R  = R 
        self.m  = 0.480 + 1.574*w - 0.176 *w**2
        self.a  = 0.42748 *((R*Tc)**2/Pc)
        self.b  = 0.08664  * (R*Tc/Pc)
    def alpha(self,T): 
        return self.a * (1 + self.m*(1-np.sqrt(T/self.Tc)))**2
    def pressure (self , T , v): 
        alpha_T = self.alpha(T)
        P_rep = (self.R * T)/(v - self.b)
        P_att = alpha_T / (v*(v+self.b))
        P = P_rep - P_att
        return P 
    def temperature (self , P , v): 
        def f(T): 
            alpha_T = self.alpha(T)
            P_rep = (self.R * T)/(v - self.b)
            P_att = alpha_T / (v*(v+self.b))
            return P_rep - P_att - P
        T_guess = P * v / self.R
        return fsolve(f , T_guess)[0]
    def ZFactors(self, P, T):
        alpha_T = self.alpha(T)
        A = (alpha_T * P) / (self.R**2 * T**2)
        B = (self.b * P) / (self.R * T)
        # Correct Form: Z^3 - Z^2 + (A - B - B^2)Z - AB = 0
        coef = [1, -1, (A - B - B**2), -A * B]
        roots = np.roots(coef)
        return np.sort(np.real(roots[np.isreal(roots)]))
    def volumes(self, P, T):
        Zs = self.ZFactors(P, T)
        v = Zs * self.R * T / P
        return v
    

# Peng_Robinson 1976 

class PengRobinsonEOS : 
    def __init__ (self,Pc,Tc,w,R = 8.314):
        self.Pc = Pc
        self.Tc = Tc
        self.R  = R
        self.w  = w
        self.m  = 0.37464 + 1.54226*w - 0.26992*w**2
        if w > 0.49 :
            self.m  = 0.379642 + 1.48503*w - 0.1644*(w**2) + 0.016667*(w**3)
        self.a  = 0.45724 *((R*Tc)**2/Pc)
        self.b  = 0.0778  * (R*Tc/Pc)
        
    def alpha(self,T): 
        return (1 + self.m*(1-np.sqrt(T/self.Tc)))**2
    def pressure(self , T , v): 
        a_T = self.a*self.alpha(T)
        P_rep = (self.R * T)/(v - self.b)
        P_att = (a_T)/(v*(v+self.b) + self.b*(v - self.b))
        P = P_rep - P_att
        return P 
    def temperature (self, P , v): 
        def f(T):
            a_T = self.a*self.alpha(T)
            P_rep = (self.R * T)/(v - self.b)
            P_att = (a_T)/(v*(v+self.b) + self.b*(v - self.b))
            return P_rep - P_att - P 
        T_guess = P * v / self.R 
        return fsolve (f , T_guess)[0]
    def ZFactors (self , P , T): 
        # Z3 - (1-B) Z2 + (A - 3B2 - 2B) Z - (AB - B2 - B3)
        a_T = self.a * self.alpha(T)
        A = (a_T *P)/((self.R**2) * (T**2))
        B = (self.b * P)/(self.R * T )
        coef = [ 1 , - (1-B) , (A - 3*B**2 -2*B) , - (A*B - B**2 - B**3) ]
        
        roots = np.roots (coef)
        real_roots = np.real(roots[np.isreal(roots)])
        Zs = np.sort (real_roots)
        return Zs
    def volumes(self, P, T):
        Zs = self.ZFactors(P, T)
        v = Zs * self.R * T / P
        return v

    
'''
NOTE: 
    All The units should be in SI !!
'''
    
'''
# Example Usage 
## Cas de N2 : 
PRN2 = PengRobinsonEOS(Pc = 33.98e5 , Tc = 126.2 , w = 0.037 )
Z1 = PRN2.Zfactors(P = 1.013e5 , T = 273.15)
Z2 = PRN2.Zfactors(P = 5e5 , T = 273.15)
Z3 = PRN2.Zfactors(P = 50e5 , T = 273.15)

print (Z1[0])
print (Z2[0])
print (Z3[0])
'''
        
            
# Created by SHAHID Mustafa :) 
    

   
















