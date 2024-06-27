const int BUTTON_PIN = 3; 
const int LED_PIN = LED_BUILTIN;
void setup()
{
     //initialize button_pin as an input
     pinMode(BUTTON_PIN, INPUT_PULLUP);
     //initialize digital pin LED_BUILTIN as an output
     pinMode(LED_PIN, OUTPUT);
}

// void loop()
// {
//      // if the button is pushed down, turn on the LED
//      if (digitalRead(BUTTON_PIN) == LOW) {
//           digitalWrite(LED_PIN, HIGH);     
//      }
//      // if the button isn't pushed down, turn the LED off
//      else {
//           digitalWrite(LED_PIN, LOW); // turn the LED off
//      }
// }
void loop()
{
     // if the button is pushed down, turn on the LED
     if (digitalRead(BUTTON_PIN) == LOW) {
          digitalWrite(LED_BUILTIN, HIGH);     
     }
     // if the button isn't pushed down, turn the LED off
     else {
          digitalWrite(LED_BUILTIN, LOW); // turn the LED off
     }
}

