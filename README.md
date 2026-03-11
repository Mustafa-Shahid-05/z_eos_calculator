# Z-Factor EOS Calculator

A Python desktop application for calculating the compressibility factor (Z) and molar volume of real gases using classical cubic Equations of State (EOS).  
The application provides a simple and intuitive graphical interface built with PyQt, making thermodynamic calculations fast and accessible.

## Features

- Clean graphical interface built with **PyQt5 + Qt Designer**
- Supports **50+ gases** with their critical properties and acentric factors
- Calculates **Compressibility Factor (Z)**
- Computes **molar volume**
- Automatically identifies **vapor and liquid roots**
- Implements **four classical cubic equations of state**

### Implemented EOS

- Van der Waals (1873)
- Redlich–Kwong (1949)
- Soave–Redlich–Kwong (1972)
- Peng–Robinson (1976)

## Input Parameters

The user can select a gas and provide:

- Pressure
- Temperature

The program then computes the compressibility factor and corresponding molar volume using the selected equation of state.

## Technologies Used

- Python
- NumPy
- SciPy
- PyQt5
- Qt Designer

## Project Structure
