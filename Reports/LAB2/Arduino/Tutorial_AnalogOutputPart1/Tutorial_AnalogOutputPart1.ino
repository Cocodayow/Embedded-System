int PWM_pin = 3; // refer to Arduino Nano’s Documentation for the pins that supports PWM
void setup () {
     pinMode(PWM_pin, OUTPUT);
}

void loop() {
     analogWrite(PWM_pin, 0);
     delay(2000);
     analogWrite(PWM_pin,127);
     delay(2000);
     analogWrite(PWM_pin, 255);
     delay(2000);
     analogWrite(PWM_pin, 90);
     delay(2000);
}
