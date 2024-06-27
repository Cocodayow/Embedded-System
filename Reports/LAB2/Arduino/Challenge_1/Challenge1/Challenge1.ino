int previousState = -1;
int currentState = -1;
int ax = 0;
int ay = 0;
int az = 0;
int sampleTime = 0;
unsigned long previousTime = 0;
void setup() {
    Serial.begin(9600);
    setupDisplay();
    setupAccelSensor();
}

void loop() {
    if (sampleSensors() ) {  // Checks if it's time to sample the sensors
        // Serial.print(ax);
        // Serial.print(",");
        // Serial.print(ay);
        // Serial.print(",");
        // Serial.println(az);
        currentState = detectGesture(ax, ay, az, previousState);
        if (currentState != previousState) {
            switch (currentState) {
                case 0:
                  Serial.println("UP");
                    writeDisplay("Up     ", 0, true);
                    break;
                case 1:
                   Serial.println("DOWN");
                    writeDisplay("Down   ", 0, true);
                    break;
                case 2:
                    Serial.println("SHAKING");
                    writeDisplay("Shaking", 0, true);
                    break;
            }
            previousState = currentState; 
        }
    }
}
int axbefore = 0;
int axcurrent  = 0;
int aybefore = 0;
int aycurrent = 0;
int azbefore = 0;
int azcurrent = 0;

int detectGesture(float ax, float ay, float az, int previousState) {
    static unsigned long previousTime = 0;
    static float axPrevious = 0, ayPrevious = 0, azPrevious = 0;

    unsigned long currentTime = millis();
    float axDiff = abs(ax - axPrevious);
    float ayDiff = abs(ay - ayPrevious);
    float azDiff = abs(az - azPrevious);

    if (currentTime - previousTime >= 5) {
        if (az >= 400 || ax >= 390 && axDiff <= 10 && ayDiff <= 10 && azDiff <= 10) {
            axPrevious = ax; ayPrevious = ay; azPrevious = az;
            previousTime = currentTime;
            return 0;  
        }
        else if (az <= 285 && axDiff <= 10 && ayDiff <= 10 && azDiff <= 10) {
            axPrevious = ax; ayPrevious = ay; azPrevious = az;
            previousTime = currentTime;
            return 1;  
        }
        else if (axDiff > 20 || ayDiff > 20 || azDiff > 20) {
            axPrevious = ax; ayPrevious = ay; azPrevious = az;
            previousTime = currentTime;
            return 2;  
        }

        axPrevious = ax; ayPrevious = ay; azPrevious = az;
        previousTime = currentTime;
    }

    return previousState; // No change detected, return previous state
}
