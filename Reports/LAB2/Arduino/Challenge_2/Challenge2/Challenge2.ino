enum State {
    WAIT,
    ADD,
    SUBTRACT,
    VIBRATION 
};

int timeLeft = 0;
const int ADD_BUTTON_PIN = 2;
const int RESET_BUTTON_PIN = 3;
const int PWM_pin = 4;
unsigned long previousTime = 0;
unsigned long previousPrintTime = 0;
unsigned long previousCountdownTime = 0;
int addButtonState;
int resetButtonState;
int lastAddButtonState = HIGH;  
int lastResetButtonState = HIGH;  
State currentState = WAIT;

void setup() {
  pinMode(ADD_BUTTON_PIN, INPUT_PULLUP);
  pinMode(RESET_BUTTON_PIN, INPUT_PULLUP);
  pinMode(PWM_pin, OUTPUT);
  Serial.begin(9600);
  setupMotor();
  setupDisplay();
}

void loop() {
    unsigned long currentTime = millis();
    addButtonState = digitalRead(ADD_BUTTON_PIN);
    resetButtonState = digitalRead(RESET_BUTTON_PIN);

    if (lastAddButtonState == HIGH && addButtonState == LOW) {
      if (currentState == WAIT || currentState == SUBTRACT){
          currentState = ADD;
          previousTime = currentTime;  // Reset the timing for the ADD action
      }
    } else if (lastAddButtonState == LOW && addButtonState == HIGH) {
        if (currentState == ADD && timeLeft > 0) {
            // Only transition to SUBTRACT if the timer has been incremented
            currentState = SUBTRACT;
        }
    }

  if (lastResetButtonState == HIGH && resetButtonState == LOW) {
      // If RESET button is pressed
      timeLeft = 0;
      currentState = WAIT;
      String timerString = String(timeLeft);
      writeDisplay(timerString.c_str(), 0, true);
      analogWrite(PWM_pin, 0); 
  }

// State actions
switch (currentState) {
    case ADD:
        if (currentTime - previousTime >= 300) {
            String timerString = String(timeLeft);
            writeDisplay(timerString.c_str(), 0, true);
            timeLeft += 1;
            previousTime = currentTime;  // Reset the timing for the ADD action
        }
        break;
    case SUBTRACT:
        addButtonState = digitalRead(ADD_BUTTON_PIN);
        if (currentTime - previousCountdownTime >= 300) {
            addButtonState = digitalRead(ADD_BUTTON_PIN);
            timeLeft -= 1;
            String timerString = String(timeLeft );
            writeDisplay(timerString.c_str(), 0, true);
            
            if (timeLeft == 0) {
                currentState = VIBRATION;
            }else if (addButtonState == LOW) {
              currentState = ADD;
              break;
            }
            previousCountdownTime = currentTime;  // Reset the timing for the SUBTRACT action
        }
        break;


        case VIBRATION:
            analogWrite(PWM_pin, 255); 
            break;
        case WAIT:
            analogWrite(PWM_pin, 0); 
            break;
    }

    lastAddButtonState = addButtonState;
    lastResetButtonState = resetButtonState;
}

