var ohmsLaw = {
    values: {
        voltageMult: 0,
        currentMult: 0,
        resistanceMult: 0,
        power: 0,
    },
    getMultiplierString: function getMultiplier(variable, unit) {
        console.log(variable);
        console.log(unit);
        switch(variable) {
            case "Voltage":
                ohmsLaw.values.voltageMult = ohmsLaw.getMultiplierVal(unit)
                break;
            case "Current":
                ohmsLaw.values.currentMult = ohmsLaw.getMultiplierVal(unit)
                break;
            case "Resistance":
                ohmsLaw.values.resistanceMult = ohmsLaw.getMultiplierVal(unit)
                break;
            case "Power":
                ohmsLaw.values.power = ohmsLaw.getMultiplierVal(unit)
                break;
        }
        var calculated = ohmsLaw.calculateVals();

    },
    getMultiplierVal: function getMultiplierVal(unit) {
        if (/(^milli|^Milli)/.test(unit)) {
            return 0.001
        } else if (/(^kilo|^Kilo)/.test(unit)) {
            return 1000
        } else if (/(^mega|^Mega)/.test(unit)) {
            return 1000000
        } else {
            return 1
        }

    },
    calculateVals: function calculateVals() {
        var numCompleted = 0;
        var keys = Object.keys(ohmsLaw.values);
        for (var i = 0; i < keys.length; i++ ) {
            if (ohmsLaw.values[keys[i]] !== 0) {
                numCompleted++
            }
        }
        if (numCompleted >= 2) {
            ohmsLaw.runCalculation();
        }

    },
    runCalculation: function runCalculation() {
        // Get values from text boxes
        var voltage = $('#voltage-input').val() * ohmsLaw.values.voltageMult;
        var current = $('#current-input').val() * ohmsLaw.values.currentMult;
        var resistance = $('#resistance-input').val() * ohmsLaw.values.resistanceMult;
        var power = $('#power-input').val() | 0;


        // Do calculations
        if (power !== 0) {
            if (voltage === 0) {
                voltage = power/current
            } else {
                current = power/current
            }
        }
        if (voltage === 0) {
            voltage = current*resistance
        } else if (current === 0) {
            current = voltage/resistance
        } else if (resistance === 0) {
            resistance = voltage/current
        }
        if (power === 0) {
            power = voltage*current
        }


        // Send converted values to text boxes
        $('#voltage-input').val(voltage);
        $('#current-input').val(current);
        $('#resistance-input').val(resistance);
        $('#power-input').val(power);

    }
};

$(document).ready(function(){
    $('.dropdown-menu-volts li a').on('click', function(){
        ohmsLaw.getMultiplierString("Voltage", $(this).text());
    });

    $('.dropdown-menu-current li a').on('click', function(){
        ohmsLaw.getMultiplierString("Current", $(this).text());
    });

    $('.dropdown-menu-resistance li a').on('click', function(){
        ohmsLaw.getMultiplierString("Resistance", $(this).text());
    });


})
