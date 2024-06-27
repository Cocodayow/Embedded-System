int red = 2;
int blue = 6;
int yellow = 4;

void setup() {
  pinMode(red, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(yellow, OUTPUT);
}

void loop() {
  digitalWrite(red, HIGH);
  delay(500); 
  digitalWrite(red, LOW);
  delay(500);  

  digitalWrite(blue, HIGH);
  delay(100);  
  digitalWrite(blue, LOW);
  delay(100); 

  digitalWrite(yellow, HIGH);
  delay(50);   
  digitalWrite(yellow, LOW);
  delay(50);  
  
  digitalWrite(red, HIGH);
  delay(1000); 
  digitalWrite(red, LOW);
  delay(100);   

  digitalWrite(blue, HIGH);
  delay(200);  
  digitalWrite(blue, LOW);
  delay(50);    

  digitalWrite(yellow, HIGH);
  delay(20);    
  digitalWrite(yellow, LOW);
  delay(10);    
}
