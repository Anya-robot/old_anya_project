#include <Servo.h>

Servo lservo1, lservo2, lservo3, lservo4, rservo1, rservo2, rservo3, rservo4 ,hservo1;
int lpos1 = 0;
int lpos2 = 0;
int lpos3 = 0;
int lpos4 = 0;


int rpos1 = 0;
int rpos2 = 0;
int rpos3 = 0;
int rpos4 = 0;


int hpos1 = 0;

int lmotor1 = 2;
int lmotor2 = 3;
int lmotor3 = 4;
int lmotor4 = 5;

int rmotor1 = 7;
int rmotor2 = 9;
int rmotor3 = 10;
int rmotor4 = 11;

int hmotor1 = 13;



const int lservopin =  22;
const int rservopin =  23;

const int lservo1rest = 160; 
const int lservo2rest = 85;
const int lservo3rest = 170;  
const int lservo4rest = 90;

const int rservo1rest = 20; 
const int rservo2rest = 90;
const int rservo3rest = 50;  
const int rservo4rest = 50;

const int hservo1rest = 90;

int ldelta1 = 0;
int ldelta2 = 0;
int ldelta3 = 0;
int ldelta4 = 0;


int rdelta1 = 0;
int rdelta2 = 0;
int rdelta3 = 0;
int rdelta4 = 0;

int hdelta1 = 0;
char val;


void setup() {

  Serial.begin(9600);

  pinMode(lservopin, OUTPUT);
  pinMode(rservopin, OUTPUT);
//  digitalWrite(motorPin, HIGH);
  
// defining seervo motors

  
  lservo1.attach(lmotor1);  
  lservo2.attach(lmotor2);
  lservo3.attach(lmotor3);
  lservo4.attach(lmotor4);
  
  rservo1.attach(rmotor1);  
  rservo2.attach(rmotor2);
  rservo3.attach(rmotor3);
  rservo4.attach(rmotor4);

  hservo1.attach(hmotor1);


  lservo1.write(lservo1rest);
  lservo2.write(lservo2rest);
  lservo3.write(lservo3rest);
  lservo4.write(lservo4rest);
  
  rservo1.write(rservo1rest);
  rservo2.write(rservo2rest);
  rservo3.write(rservo3rest);
  rservo4.write(rservo4rest);


  hservo1.write(hservo1rest);
  
  delay(1000);
//  digitalWrite(motorPin, LOW);
}
void loop() {
  if(Serial.available()){
    while(Serial.available()==0);
    val=Serial.read();
    if(val=='h'){
      Serial.println("hi");
      delay(1000);
      hi();
    }
    if(val=='s'){
      Serial.println("selfie");
      delay(1000);
      selfie();
    }
    if(val=='n'){
      Serial.println("namaste");
      delay(1000);
      namaste();
    }
    if(val=='t'){
      Serial.println("test");
      delay(1000);
      test();
    }
    if(val=='z'){
      Serial.println("headright");
      
      headright();
    }
    if(val=='x'){
      Serial.println("headleft");
      
      headleft();
    }
    
  }
//  delay(3000);
//  namaste();
  
}


int hi(){

  rdelta1 = 60;
  rdelta2 = 25;
  rdelta3 = 120;
  rdelta4 = 120;

  delay(200);
  for (rpos1 = rservo1rest; rpos1 <= (rservo1rest+rdelta1); rpos1 += 1) { 
    rpos3 = map(rpos1, rservo1rest, (rservo1rest+rdelta1), rservo3rest, (rservo3rest+rdelta3));
    rservo1.write(rpos1); 
    rservo3.write(rpos3);              
    delay(25);                       
  }

  delay(500);  

//  for (rpos3 = rservo3rest; rpos3 <= (rservo3rest+rdelta3); rpos3 += 1) { 
//    
//    rservo3.write(rpos3);              
//    delay(5);                       
//  } 

  for (rpos4 = rservo4rest; rpos4 >= (rservo4rest-rdelta4); rpos4 -=1){
    rservo4.write(rpos4);
    delay(10);
  }

  
  for (rpos2 = rservo2rest; rpos2 <= (rservo2rest+rdelta2); rpos2 += 1) { 
    
    rservo2.write(rpos2);              
    delay(30);                       
  }
  for (rpos2 = (rservo2rest+rdelta2); rpos2 >= (rservo2rest-rdelta2); rpos2 -= 1) { 
    rservo2.write(rpos2);              
    delay(30);                       
  }
  for (rpos2 = (rservo2rest-rdelta2); rpos2 <= rservo2rest; rpos2 += 1) { 
    
    rservo2.write(rpos2);              
    delay(30);                       
  }
  delay(500);



//  for (rpos3 = (rservo3rest+rdelta3); rpos3 >= rservo3rest; rpos3 -= 1) { 
//  
//    rservo3.write(rpos3);              
//    delay(5);                       
//  } 
  
  for (rpos4 = (rservo4rest-rdelta4); rpos4 <= rservo4rest; rpos4 +=1){
    rservo4.write(rpos4);
    delay(10);
  }

  for (rpos1 = (rservo1rest+rdelta1); rpos1 >= rservo1rest; rpos1 -= 1) { 
    rpos3 = map(rpos1, (rservo1rest+rdelta1), rservo1rest, (rservo3rest+rdelta3), rservo3rest);
    rservo3.write(rpos3);
    rservo1.write(rpos1);             
    delay(25);                       
  }
  delay(1000);
  return 0;
}








int selfie(){

  ldelta1 = 120;
  ldelta2 = 25;
  ldelta3 = 1;
  ldelta4 = 85;


  lservo3.write(170);

  delay(200);
  for (lpos1 = lservo1rest; lpos1 >= (lservo1rest-ldelta1); lpos1 -= 1) { 
    
    lservo1.write(lpos1);              
    delay(25);                       
  }

  for (lpos2 = lservo2rest; lpos2 >= (lservo2rest-ldelta2); lpos2 -= 1) { 
    
    lservo2.write(lpos2);              
    delay(15);                       
  }  


  for (lpos3 = lservo3rest; lpos3 >= (lservo3rest-ldelta3); lpos3 -= 1) { 
    lservo3.write(lpos3);              
    delay(5);                       
  }
  for (lpos4 = lservo4rest; lpos4 >= (lservo4rest-ldelta4); lpos4 -=1){
    lservo4.write(lpos4);
    delay(10);
  }

  
  delay(5000);



  for (lpos4 = (lservo4rest-ldelta4); lpos4 <= lservo4rest; lpos4 +=1){
    lservo4.write(lpos4);
    delay(10);
  }
  for (lpos2 = (lservo2rest-ldelta2); lpos2 <= lservo2rest; lpos2 += 1) { 
    
    lservo2.write(lpos2);              
    delay(15);                       
  } 
  

  for (lpos1 = (lservo1rest-ldelta1); lpos1 <= lservo1rest; lpos1 += 1) { 

    lpos3 = map(lpos1, (lservo1rest-ldelta1), lservo1rest, (lservo3rest-ldelta3), lservo3rest);
    
    lservo1.write(lpos1);   
    lservo3.write(lpos3);           
    delay(25);  
//    if (pos1 > 130)
//    {
//      digitalWrite(motorPin, LOW);                 
//    }
  }
  return 0;
}

int namaste(){
  
  rdelta1 = 40;
  rdelta2 = 30;
  rdelta3 = 85;


  ldelta1 = 40;
  ldelta2 = 35;
  ldelta3 = 95;

  delay(200);
  for (rpos1 = rservo1rest; rpos1 <= (rservo1rest+rdelta1); rpos1 += 1) { 
    lpos1 = map(rpos1, rservo1rest, (rservo1rest+rdelta1), lservo1rest, (lservo1rest-ldelta1));
    rservo1.write(rpos1);              
    lservo1.write(lpos1);
    delay(25);                       
  }

//  for (rpos3 = rservo3rest; rpos3 <= (rservo3rest+rdelta3); rpos3 += 1) { 
//    
//    rservo3.write(rpos3);              
//    delay(5);                       
//  }        


//  for (lpos1 = lservo1rest; lpos1 >= (lservo1rest-ldelta1); lpos1 -= 1) { 
//    
//    lservo1.write(lpos1);              
//    delay(25);                       
//  }

  for (lpos3 = lservo3rest; lpos3 >= (lservo3rest-ldelta3); lpos3 -= 1) { 
    rpos3 = map(lpos3, lservo3rest, (lservo3rest-ldelta3), rservo3rest, (rservo3rest+rdelta3));
    lservo3.write(lpos3);  
    rservo3.write(rpos3);            
    delay(5);                       
  }

  for (rpos2 = rservo2rest; rpos2 >= (rservo2rest-rdelta2); rpos2 -= 1) { 
    lpos2 = map(rpos2, rservo2rest, (rservo2rest-rdelta2), lservo2rest, (lservo2rest+ldelta2));
    rservo2.write(rpos2);              
    lservo2.write(lpos2);
    delay(30);                       
  }

//  for (lpos2 = lservo2rest; lpos2 <= (lservo2rest+ldelta2); lpos2 += 1) { 
//    
//    lservo2.write(lpos2);              
//    delay(15);                       
//  }

  delay(2000);
  
  for (rpos2 = (rservo2rest-rdelta2); rpos2 <= rservo2rest; rpos2 += 1) { 
    lpos2 = map(rpos2, (rservo2rest-rdelta2), rservo2rest, (lservo2rest+ldelta2), lservo2rest);
    rservo2.write(rpos2);              
    lservo2.write(lpos2);
    delay(30);                       
  }

//  for (lpos2 = (lservo2rest+ldelta2); lpos2 >= lservo2rest; lpos2 -= 1) { 
//    lservo2.write(lpos2);              
//    delay(15);                       
//  }

//  for (rpos3 = (rservo3rest+rdelta3); rpos3 >= rservo3rest; rpos3 -= 1) { 
//  
//    rservo3.write(rpos3);              
//    delay(5);                       
//  } 
  
  

  for (rpos1 = (rservo1rest+rdelta1); rpos1 >= rservo1rest; rpos1 -= 1) { 
    rpos3 = map(rpos1, (rservo1rest+rdelta1), rservo1rest, (rservo3rest+rdelta3), rservo3rest);
    lpos1 = map(rpos1, (rservo1rest+rdelta1), rservo1rest, (lservo1rest-ldelta1), lservo1rest);
    lpos3 = map(rpos1, (rservo1rest+rdelta1), rservo1rest, (lservo3rest-ldelta3), lservo3rest);
    rservo1.write(rpos1);
    lservo1.write(lpos1);  
    rservo3.write(rpos3);
    lservo3.write(lpos3);      
    delay(25);                       
  }


//  for (lpos3 = (lservo3rest-ldelta3); lpos3 <= lservo3rest; lpos3 += 1) { 
//    lservo3.write(lpos3);              
//    delay(5);                       
//  }
//
//  for (lpos1 = (lservo1rest-ldelta1); lpos1 <= lservo1rest; lpos1 += 1) { 
//    
//    lservo1.write(lpos1);              
//    delay(25);                       
//  } 




  return 0;
}
int test(){

  

  for (lpos2 = lservo2rest; lpos2 <= lservo2rest+60; lpos2 += 1) { 
    
    lservo2.write(lpos2);              
    delay(15);                       
  }
  for (lpos2 = lservo2rest+60; lpos2 >= lservo2rest; lpos2 -= 1) { 
    lservo2.write(lpos2);              
    delay(15);                       
  }
}



int shakehand(){

  rdelta1 = 70;
  rdelta2 = 25;
  rdelta3 = 30;
  rdelta4 = 1;

  delay(200);
  for (rpos1 = rservo1rest; rpos1 <= (rservo1rest+rdelta1); rpos1 += 1) { 
    rpos3 = map(rpos1, rservo1rest, (rservo1rest+rdelta1), rservo3rest, (rservo3rest+rdelta3));
    rservo1.write(rpos1);              
    delay(25);                       
  }

  delay(1000);  

//  for (rpos3 = rservo3rest; rpos3 <= (rservo3rest+rdelta3); rpos3 += 1) { 
//    
//    rservo3.write(rpos3);              
//    delay(5);                       
//  } 

  for (rpos3 = (rservo3rest+rdelta3); rpos3 <= (rservo3rest+rdelta3+30); rpos3 += 1) { 
    
    rservo3.write(rpos3);              
    delay(25);                       
  } 
  delay(500);
   for (rpos3 = (rservo3rest+rdelta3+30); rpos3 <= (rservo3rest+rdelta3); rpos3 += 1) { 
    
    rservo3.write(rpos3);              
    delay(25);                       
  } 
  delay(500);
  for (rpos3 = (rservo3rest+rdelta3); rpos3 <= (rservo3rest+rdelta3+30); rpos3 += 1) { 
    
    rservo3.write(rpos3);              
    delay(25);                       
  } 
  delay(500);
   for (rpos3 = (rservo3rest+rdelta3+30); rpos3 <= (rservo3rest+rdelta3); rpos3 += 1) { 
    
    rservo3.write(rpos3);              
    delay(25);                       
  } 
  delay(500);

  
  
  delay(1000);



//  for (rpos3 = (rservo3rest+rdelta3); rpos3 >= rservo3rest; rpos3 -= 1) { 
//  
//    rservo3.write(rpos3);              
//    delay(5);                       
//  } 
  


  for (rpos1 = (rservo1rest+rdelta1); rpos1 >= rservo1rest; rpos1 -= 1) { 
    rpos3 = map(rpos1, (rservo1rest+rdelta1), rservo1rest, (rservo3rest+rdelta3), rservo3rest);
    rservo3.write(rpos3);
    rservo1.write(rpos1);             
    delay(25);                       
  }
  delay(1000);
  return 0;
}




int headleft(){

  hdelta1 = 45;
  


  for (hpos1 = hservo1rest; hpos1 <= (hservo1rest+hdelta1); hpos1 += 1) { 
    
    hservo1.write(hpos1);              
    delay(50);                       
  }

  delay(1000);  
  for (hpos1 = (hservo1rest+hdelta1); hpos1 >= hservo1rest; hpos1 -= 1) { 
    
    hservo1.write(hpos1);              
    delay(50);                       
  }

 
  return 0;
}


int headright(){

  hdelta1 = 45;
  


  for (hpos1 = hservo1rest; hpos1 >= (hservo1rest-hdelta1); hpos1 -= 1) { 
    
    hservo1.write(hpos1);
    
    delay(50);                       
  }

  delay(1000);  
  for (hpos1 = (hservo1rest-hdelta1); hpos1 <= hservo1rest; hpos1 += 1) { 
    
    hservo1.write(hpos1); 
             
    delay(50);                       
  }

 
  return 0;
}
