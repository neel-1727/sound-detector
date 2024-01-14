basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P0) == 1) {
        basic.showString("Voice In!!")
    } else {
    	
    }
})
