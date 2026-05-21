# ==========================================
#        EWA BILL GENERATOR
# ==========================================

ELECTRICITY_RATE = 0.032

WATER_RATE = 0.775
SANITARY_RATE = 0.155

ELECTRICITY_ADMIN = 1.000
WATER_ADMIN = 1.000

MUNICIPALITY_FEE = 5.000


# ==========================================
# USER INPUT
# ==========================================

prev_elec = float(input("Enter previous electricity reading : "))
curr_elec = float(input("Enter current electricity reading  : "))

prev_water = float(input("Enter previous water reading       : "))
curr_water = float(input("Enter current water reading        : "))
