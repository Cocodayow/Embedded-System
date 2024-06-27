const int MOTOR_PIN = 3;
void setupMotor(){
  pinMode(MOTOR_PIN, OUTPUT);
}
void activateMotor(int motorPower){
  analogWrite(MOTOR_PIN, motorPower);
}
void deactivateMotor() {
  analogWrite(MOTOR_PIN, 0); 
}