def PressureConverter(value, from_unit, to_unit):

    # constants
    atm_pa = 101325
    psi_pa = 6894.757

    # convert input → Pa
    to_pa = {
        "pa": 1,
        "kpa": 1e3,
        "mpa": 1e6,
        "bars": 1e5,
        "atm": atm_pa,
        "psia": psi_pa
    }

    # handle psig separately
    if from_unit.lower() == "psig":
        value_pa = (value + 14.6959) * psi_pa
    else:
        value_pa = value * to_pa[from_unit.lower()]

    # convert Pa → output unit
    from_pa = {
        "pa": 1,
        "kpa": 1e-3,
        "mpa": 1e-6,
        "bars": 1e-5,
        "atm": 1/atm_pa,
        "psia": 1/psi_pa
    }

    if to_unit.lower() == "psig":
        psia = value_pa / psi_pa
        return psia - 14.6959
    else:
        return value_pa * from_pa[to_unit.lower()]

def TemperatureConverter(value, from_unit, to_unit):

   

    # Convert → Kelvin
    if from_unit == "K":
        K = value
    elif from_unit == "°C":
        K = value + 273.15
    elif from_unit == "°F":
        K = (value + 459.67) * 5/9
    elif from_unit == "°R":
        K = value * 5/9
    else:
        raise ValueError("Unknown temperature unit")

    # Kelvin → target
    if to_unit == "K":
        return K
    elif to_unit == "°C":
        return K - 273.15
    elif to_unit == "°F":
        return K * 9/5 - 459.67
    elif to_unit == "°R":
        return K * 9/5
    else:
        raise ValueError("Unknown temperature unit")
    
    
    