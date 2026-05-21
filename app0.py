# ==========================================
#        EWA BILL GENERATOR
# ==========================================

ELECTRICITY_RATE = 0.032

WATER_RATE = 0.775
SANITARY_RATE = 0.155

ELECTRICITY_ADMIN = 1.000
WATER_ADMIN = 1.000

MUNICIPALITY_FEE = 5.000


def generate_ewa_bill(
    prev_elec,
    curr_elec,
    prev_water,
    curr_water,
    days=30
):

    # =====================================
    # CONSUMPTION
    # =====================================
    elec_consumption = curr_elec - prev_elec
    water_consumption = curr_water - prev_water

    # =====================================
    # ELECTRICITY
    # =====================================
    elec_charge = elec_consumption * ELECTRICITY_RATE
    elec_total = elec_charge + ELECTRICITY_ADMIN

    # =====================================
    # WATER
    # =====================================
    water_charge = water_consumption * WATER_RATE
    sanitary_fee = water_consumption * SANITARY_RATE

    water_total = (
        water_charge
        + sanitary_fee
        + WATER_ADMIN
    )

    # =====================================
    # GRAND TOTAL
    # =====================================
    grand_total = (
        elec_total
        + water_total
        + MUNICIPALITY_FEE
    )

    # =====================================
    # DISPLAY BILL
    # =====================================

    print("\n")
    print("=" * 55)
    print("               EWA ELECTRICITY & WATER BILL")
    print("=" * 55)

    print(f"\nBilling Period : {days} Days")

    print("\n---------------------------------------------")
    print("ELECTRICITY")
    print("---------------------------------------------")

    print(f"Previous Reading      : {prev_elec}")
    print(f"Current Reading       : {curr_elec}")
    print(f"Consumption           : {elec_consumption} kWh")
    print(f"Rate                  : {ELECTRICITY_RATE:.3f} BD")
    print(f"Energy Charge         : {elec_charge:.3f} BD")
    print(f"Administration Fees   : {ELECTRICITY_ADMIN:.3f} BD")

    print(f"\nElectricity Total     : {elec_total:.3f} BD")

    print("\n---------------------------------------------")
    print("WATER")
    print("---------------------------------------------")

    print(f"Previous Reading      : {prev_water}")
    print(f"Current Reading       : {curr_water}")
    print(f"Consumption           : {water_consumption} m3")

    print(f"\nWater Charge")
    print(f"{water_consumption} × {WATER_RATE:.3f} = {water_charge:.3f} BD")

    print(f"\nSanitary Fee")
    print(f"{water_consumption} × {SANITARY_RATE:.3f} = {sanitary_fee:.3f} BD")

    print(f"\nAdministration Fees   : {WATER_ADMIN:.3f} BD")

    print(f"\nWater Total           : {water_total:.3f} BD")

    print("\n---------------------------------------------")
    print("OTHER CHARGES")
    print("---------------------------------------------")

    print(f"Municipality Fees     : {MUNICIPALITY_FEE:.3f} BD")

    print("\n=============================================")
    print(f"TOTAL AMOUNT DUE      : {grand_total:.3f} BD")
    print("=============================================")

    print("\nPride in what we do.. Proud to serve..")
    print("=" * 55)


# ==========================================
# USER INPUT
# ==========================================

prev_elec = float(input("Enter previous electricity reading : "))
curr_elec = float(input("Enter current electricity reading  : "))

prev_water = float(input("Enter previous water reading       : "))
curr_water = float(input("Enter current water reading        : "))

generate_ewa_bill(
    prev_elec,
    curr_elec,
    prev_water,
    curr_water
)
