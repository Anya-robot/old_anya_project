
#include <Servo.h>

Servo myservo,myservo1;  


int pos1 = 0;    

void setup() {
  myservo.attach(9);
  myservo1.attach(11);  
  
}

void loop() {

    
  myservo.write(150); 
  delay(200);
  for (pos1 = 160; pos1 >= 50; pos1 -= 1) { 
    
    myservo1.write(pos1);              
    delay(25);                       
  }

  delay(5000);  
  for (pos1 = 50; pos1 <= 160; pos1 += 1) { 
    myservo1.write(pos1);              
    delay(25);                       
  }          
}
