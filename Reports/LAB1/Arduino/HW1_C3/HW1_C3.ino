enum State {
    STOPPED,
    ADDING,
    COUNTDOWN
};

int timer = 0;
const int BUTTON_PIN = 2;
unsigned long previousTime = 0;
unsigned long previousPrintTime = 0;
unsigned long previousCountdownTime = 0;
int buttonState;
int lastButtonState = HIGH;
State currentState = STOPPED;

void setup() {
    pinMode(BUTTON_PIN, INPUT_PULLUP);
    Serial.begin(9600);
}

void loop() {
    unsigned long currentTime = millis();
    buttonState = digitalRead(BUTTON_PIN);

    //Check button state change from high to low (button press)
    if (buttonState == LOW && lastButtonState == HIGH) {
      previousTime = currentTime;
      if (currentState == STOPPED || currentState == COUNTDOWN) {
          currentState = ADDING;
      }
      timer++; 
    }
    lastButtonState = buttonState;

    //Only starts countdown when no button press detect in the last 3 seconds.
    if (currentState == ADDING && currentTime - previousTime >= 3000) {
      currentState = COUNTDOWN;
    }

    if (currentState == COUNTDOWN && currentTime - previousCountdownTime >= 1000 && timer > 0) {
      previousCountdownTime = currentTime;
      timer--;
    }

    if (currentTime - previousPrintTime >= 100) {
      Serial.println(timer);
      previousPrintTime = currentTime;
    }
}
