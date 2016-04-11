"""
Calulates simple equations for use in basic electrical engineering
"""

def main():
    print "Welcome!"
    print ""
    print "--------------------"
    print "1: Calculate using Ohm's Law"
    print "2: Calculate a resistor's value"
    print "--------------------"
    print ""
    choice = int(raw_input("Enter the value for which function you wish to perform: "))
    if choice == 1:
        calculateOhms()
    elif choice == 2:
        calculateResist()

def calculateOhms():
    print("Welcome to EE Helper")
    print("Let's calculate some values with Ohm's Law!")
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

    # Ask to restart
    rerun = raw_input("Would you like to start do another? (Y/N) ")
    while rerun.upper() != "Y" and rerun.upper() != "N":
        rerun = raw_input("Would you like to do another? (Y/N) ")
    if rerun.upper() == "Y":
        calculateOhms()
    else:
        exit()



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

def calculateResist():
    print("Calculating Resistance!")
    bands = []
    for i in range(4):
        print "Band " + str(i+1)
        color = raw_input("Enter the color of the band: ")
        bands.append(getColorVals(color, i+1))
    bandValue = 0
    bandValue = str(bands[0])+str(bands[1])
    bandValue = int(bandValue)*float(bands[2])
    print("--------------------")
    print str(bandValue) + " Ohms"
    print "Tolerance: " + str(bands[3])+"%"
    print("--------------------")

    # Ask to restart
    rerun = raw_input("Would you like to do another? (Y/N) ")
    while rerun.upper() != "Y" and rerun.upper() != "N":
        rerun = raw_input("Would you like to do another? (Y/N) ")
    if rerun.upper() == "Y":
        calculateResist()
    else:
        exit()


def getColorVals(color, bandNum):
    if bandNum == 1 or bandNum == 2:
        if color.lower() == "black":
            return 0
        elif color.lower() == "brown":
            return 1
        elif color.lower() == "red":
            return 2
        elif color.lower() == "orange":
            return 3
        elif color.lower() == "yellow":
            return 4
        elif color.lower() == "green":
            return 5
        elif color.lower() == "blue":
            return 6
        elif color.lower() == "purple" or color.lower() == "violet":
            return 7
        elif color.lower() == "grey":
            return 8
        elif color.lower() == "white":
            return 9
    elif bandNum == 3:
        if color.lower() == "black":
            return 1
        elif color.lower() == "brown":
            return 10
        elif color.lower() == "red":
            return 100
        elif color.lower() == "orange":
            return 1000
        elif color.lower() == "yellow":
            return 10000
        elif color.lower() == "green":
            return 100000
        elif color.lower() == "blue":
            return 1000000
        elif color.lower() == "purple" or color.lower() == "violet":
            return 10000000
        elif color.lower() == "gold":
            return 0.1
        elif color.lower() == "silver":
            return 0.01
    elif bandNum == 4:
        if color.lower() == "brown":
            return 1
        elif color.lower() == "red":
            return 2
        elif color.lower() == "green":
            return 0.5
        elif color.lower() == "blue":
            return 0.25
        elif color.lower() == "purple" or color.lower() == "violet":
            return 0.10
        elif color.lower() == "grey":
            return 0.05
        elif color.lower() == "gold":
            return 5
        elif color.lower() == "silver":
            return 10





main()
