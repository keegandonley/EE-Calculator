"""
Calulates simple equations for use in basic electrical engineering
"""

def main():
    print("Welcome to EE Helper")
    print("Currently, I'm able to calculate Ohm's law!")
    units = ["Volts", "Amps", "Ohms"]

    v = raw_input("Enter the voltage: ")
    vunits = raw_input("Enter the units for Voltage (V, mV): ")
    while (vunits.upper() != "V" and vunits.upper() != "MV"):
        vunits = raw_input("Enter the units for Voltage (V, mV): ")
    if vunits.upper() == "MV" and v != "":
        v = float(v)/1000
    elif vunits.upper() == "V" and v != "":
        v = float(v)

    i = raw_input("Enter the current: ")
    iunits = raw_input("Enter the units for Amps (A, mA): ")
    while (iunits.upper() != "A" and iunits.upper() != "MA"):
        iunits = raw_input("Enter the units for Amps (A, mA): ")
    if iunits.upper() == "MA" and i != "":
        i = float(i)/1000
    elif iunits.upper() == "A" and i != "":
        i = float(i)

    r = raw_input("Enter the resistance: ")
    runits = raw_input("Enter the units for Resistance(Ohm, kOhm): ")
    while (runits.upper() != "OHM" and runits.upper() != "KOHM"):
        runits = raw_input("Enter the units for Resistance (Ohm, kOhm): ")
    if runits.upper() == "KOHM" and r != "":
        r = float(r)*1000
    elif runits.upper() == "OHM" and r != "":
        r = float(r)

    # Units and values are now validated
    missing = findSolve(v, i ,r)
    result = calulateMissing(missing, v, i, r)
    displayResults(units[missing], result, [v, i, r], units, missing)
    # print(units[missing], result)


def findSolve(v, i, r):
    if v == "":
        return(0)
    elif i == "":
        return(1)
    elif r == "":
        return(2)
    else:
        errorHandler("No values were left empty!")

def calulateMissing(missing, v, i, r):
    if missing == 0:
        return i*r
    elif missing == 1:
        return v/r
    elif missing == 2:
        return v/i
    else:
        errorHandler("Values are not properly set up!")

def displayResults(unit, answer, initialVals, units, missing):
    # print(units)
    # print(answer)
    # print(initialVals)
    print "--------------------"
    for i in range(len(initialVals)):
        if initialVals[i] != "":
            print units[i] + ": " + str(initialVals[i])
        else:
            print unit + ": " + str(answer)
    print "--------------------"
    initialVals[missing] = answer
    print "Power: " + str(initialVals[0]*initialVals[1]) + " Watts"
    print "--------------------"



def errorHandler(e):
    print("Oops! The follwing error occured:")
    print(e)
    rerun = raw_input("Would you like to start over? (Y/N) ")
    while rerun.upper() != "Y" and rerun.upper() != "N":
        rerun = raw_input("Would you like to start over? (Y/N) ")
    if rerun.upper() == "Y":
        main()
    else:
        exit()


main()
