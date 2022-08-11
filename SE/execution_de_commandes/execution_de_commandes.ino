int vib = 26; 
int vib1 = 25;
int vib2 = 34;




void setup() {
 
ledcAttachPin(vib, 0); 
ledcSetup(0, 5000, 8);
ledcAttachPin(vib1, 1); 
ledcSetup(1, 5000, 8);
ledcAttachPin(vib, 2); 
ledcSetup(2, 5000, 8);
}



void loop() {

  ledcWrite(0, 255); 
    
  ledcWrite(1, 255); 
   
  ledcWrite(2, 0); 

}
