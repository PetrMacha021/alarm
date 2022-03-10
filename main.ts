radio.setGroup(1);
radio.setTransmitSerialNumber(true);

let learnedSerial: Array<number> = []

function send() {
    radio.sendValue("alarm", 1);
    console.log("sent alarm");
}

function stop() {
    radio.sendValue("alarm", 0);
    console.log("sent stop");
}

function receivedValue(name: string, value: number) {
    console.logValue(name, value);
    const serial: number = radio.receivedPacket(RadioPacketProperty.SerialNumber);
    if (name == "learn" && value == 1) {
        learnedSerial.push(serial);
        console.logValue("serial", serial);
    } else if (name == "alarm") {
        if (value == 1) {
            music.playTone(Note.C, 0);
        } else if (value == 0) {
            music.stopAllSounds();
        }
    }
}

radio.onReceivedValue(receivedValue);

input.onButtonPressed(Button.A, send);
input.onButtonPressed(Button.B, stop);