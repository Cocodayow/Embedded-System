const int X_PIN = A1; 
const int Y_PIN = A2; 
const int Z_PIN = A3;

extern int ax;
extern int ay;
extern int az;

void setupAccelSensor(){
  // Initialize accelerometer pins as input
  pinMode(X_PIN, INPUT);
  pinMode(Y_PIN, INPUT);
  pinMode(Z_PIN, INPUT);
}

void readAccelSensor(){
  ax = analogRead(X_PIN);
  ay = analogRead(Y_PIN);
  az = analogRead(Z_PIN);
}
