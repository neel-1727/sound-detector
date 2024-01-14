def on_forever():
    if pins.digital_read_pin(DigitalPin.P0) == 1:
        basic.show_string("Voice In!!")
    else:
        pass
basic.forever(on_forever)
