radio.set_group(1)
radio.set_transmit_serial_number(True)

learnedSerial = [control.device_serial_number()]
learning = 0

def on_received_value(name, value):
    global learnedSerial, learning
    console.log_value(name, value)
    console.log_value("serial", radio.received_packet(RadioPacketProperty.SERIAL_NUMBER))
    if name == "learn" and learning == 1:
        if value == 1:
            learnedSerial.push(radio.received_packet(RadioPacketProperty.SERIAL_NUMBER))
            learning = 0
            basic.clear_screen()
            console.log(learnedSerial)

    learning = 1
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_event_long)

def on_button_pressed_a():
    radio.send_value("alarm", 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_value("alarm", 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.on_received_value(on_received_value)