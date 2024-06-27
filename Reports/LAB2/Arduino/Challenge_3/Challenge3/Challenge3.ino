enum State {
    WAIT,
    ADD,
    SUBTRACT,
    VIBRATION
};

int timeLeft = 0;
// const int ADD_BUTTON_PIN = 2;
// const int RESET_BUTTON_PIN = 3;
const int PWM_pin = 4;
unsigned long previousTime = 0;
unsigned long previousPrintTime = 0;
unsigned long previousCountdownTime = 0;
int currentGesture = -1;
int previousGesture = -1;
State currentState = WAIT;
int ax = 0;
int ay = 0;
int az = 0;
int sampleTime = 0;

void setup() {
  // pinMode(ADD_BUTTON_PIN, INPUT_PULLUP);
  // pinMode(RESET_BUTTON_PIN, INPUT_PULLUP);
  pinMode(PWM_pin, OUTPUT);
  Serial.begin(9600);
  setupMotor();
  setupDisplay();
  setupAccelSensor();
}

void loop() {
  if (sampleSensors() ){
    Serial.print(ax);
    Serial.print(",");
    Serial.print(ay);
    Serial.print(",");
    Serial.println(az);
    currentGesture= detectGesture(ax, ay, az, previousGesture);
    unsigned long currentTime = millis();

    if (currentGesture== 1) {
      if (currentState == WAIT || currentState == SUBTRACT){
          currentState = ADD;
          previousTime = currentTime;  // Reset the timing for the ADD action
      }
    } else if (currentGesture == 0) {
        if (currentState == ADD && timeLeft > 0) {
            // Only transition to SUBTRACT if the timer has been incremented
            currentState = SUBTRACT;
        }
    }

  if (currentGesture == 2) {
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
        currentGesture= detectGesture(ax, ay, az,  previousGesture);
        if (currentTime - previousCountdownTime >= 300) {
            currentGesture= detectGesture(ax, ay, az, previousGesture);
            timeLeft -= 1;
            String timerString = String(timeLeft );
            writeDisplay(timerString.c_str(), 0, true);
            
            if (timeLeft == 0) {
                currentState = VIBRATION;
            }else if (currentGesture == 1) {
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

}
 previousGesture= currentGesture; 
}


int axbefore = 0;
int axcurrent  = 0;
int aybefore = 0;
int aycurrent = 0;
int azbefore = 0;
int azcurrent = 0;

int detectGesture(float ax, float ay, float az, int previousGesture) {
    static unsigned long previousTime = 0;
    static float axPrevious = 0, ayPrevious = 0, azPrevious = 0;

    unsigned long currentTime = millis();
    float axDiff = abs(ax - axPrevious);
    float ayDiff = abs(ay - ayPrevious);
    float azDiff = abs(az - azPrevious);

    if (currentTime - previousTime >= 5) {
        if (az >= 400 && axDiff <= 25 && ayDiff <= 25 && azDiff <= 25) {
            axPrevious = ax; ayPrevious = ay; azPrevious = az;
            previousTime = currentTime;
            return 0;  
        }
        else if (az <= 290 && axDiff <= 25 && ayDiff <= 25 && azDiff <= 25) {
            axPrevious = ax; ayPrevious = ay; azPrevious = az;
            previousTime = currentTime;
            return 1;  
        }
        else if (axDiff > 40 || ayDiff > 40 || azDiff > 40) {
            axPrevious = ax; ayPrevious = ay; azPrevious = az;
            previousTime = currentTime;
            return 2;  
        }

        axPrevious = ax; ayPrevious = ay; azPrevious = az;
        previousTime = currentTime;
    }

    return  previousGesture; // No change detected, return previous state
}

