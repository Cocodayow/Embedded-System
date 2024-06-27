enum State {
    STOPPED,
    RUNNING,
    PAUSED
};

int counter = 0;
int BUTTON_PIN = 2;
unsigned long previousTime = 0;
unsigned long previousPrintTime = 0;
int buttonState;
int lastButtonState = HIGH;
State currentState = STOPPED;

void setup() {
    pinMode(BUTTON_PIN, INPUT_PULLUP);
    Serial.begin(9600);
}

void loop() {
    unsigned long currentTime = millis();
    buttonState = digitalRead(BUTTON_PIN); //0 or 1, low or high, pressed or released

    //if button changed from high to low
    if (buttonState == LOW && lastButtonState == HIGH) {
      switch (currentState) {
        case STOPPED: //initial state, leave once detects a press
            currentState = RUNNING;
            break;
        case RUNNING:
            currentState = PAUSED;
            break;
        case PAUSED:
            currentState = RUNNING;
            break;
      }
    }
    
    lastButtonState = buttonState;
    //while in running state, update counter every second until reads a another change in state from high->low/another 
    if (currentState == RUNNING && currentTime - previousTime >= 1000) {
        counter++;
        previousTime = currentTime;
    }

    if (currentTime - previousPrintTime >= 100) {
        Serial.println(counter);
        previousPrintTime = currentTime;
    }
}
