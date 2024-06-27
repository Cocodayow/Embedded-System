const int BUTTON_1_PIN = 2;
const int BUTTON_2_PIN = 3;
const int BUTTON_3_PIN = 4;
const int BUTTON_4_PIN = 5;

enum ACTIONS{
  NONE, DOWN1, UP1, DOWN2, UP2, DOWN3, UP3, DOWN4, UP4
};

void setup()  {
  Serial.begin(9600);
  pinMode(BUTTON_1_PIN, INPUT_PULLUP);
  pinMode(BUTTON_2_PIN, INPUT_PULLUP);
  pinMode(BUTTON_3_PIN, INPUT_PULLUP);
  pinMode(BUTTON_4_PIN, INPUT_PULLUP);
}
bool button_1_pressed = false;
bool button_2_pressed = false;
bool button_3_pressed = false;
bool button_4_pressed = false;

void loop() {
  int btn1 = digitalRead(BUTTON_1_PIN);
  int btn2 = digitalRead(BUTTON_2_PIN);
  int btn3 = digitalRead(BUTTON_3_PIN);
  int btn4 = digitalRead(BUTTON_4_PIN);

  if(button_1_pressed && btn1==HIGH){ // RELEASED
    Serial.write((uint8_t)UP1);
    button_1_pressed = false;
  }else if(!button_1_pressed && btn1==LOW){
    Serial.write((uint8_t)DOWN1);
    button_1_pressed = true;
  }

  if(button_2_pressed && btn2==HIGH){ // RELEASED
    Serial.write((uint8_t)UP2);
    button_2_pressed = false;
  }else if(!button_2_pressed && btn2==LOW){
    Serial.write((uint8_t)DOWN2);
    button_2_pressed = true;
  }

  if(button_3_pressed && btn3==HIGH){ // RELEASED
    Serial.write((uint8_t)UP3);
    button_3_pressed = false;
  }else if(!button_3_pressed && btn3==LOW){
    Serial.write((uint8_t)DOWN3);
    button_3_pressed = true;
  }

  if(button_4_pressed && btn4==HIGH){ // RELEASED
    Serial.write((uint8_t)UP4);
    button_4_pressed = false;
  }else if(!button_4_pressed && btn4==LOW){
    Serial.write((uint8_t)DOWN4);
    button_4_pressed = true;
  }
}