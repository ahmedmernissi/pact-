int ventilo = 26; //Le pin 26 correspond à la sortie A0 de la carte
int res = 25;
int vib = 21;

void setup() {

ledcAttachPin(ventilo, 1); //On relie la sortie A0 au canal PWM 1
ledcSetup(1, 5000, 8); //On configure le canal PWM 1 avec une fréquence de 5000 Hz et une résolution de 8 bits
ledcAttachPin(res, 2); //On relie la sortie A0 au canal PWM 1
ledcSetup(2, 5000, 8);
ledcAttachPin(vib, 0); //On relie la sortie A0 au canal PWM 1
ledcSetup(0, 5000, 8);
}

void loop() {
  
  

    ledcWrite(1, 255);
    ledcWrite(2, 255);
    ledcWrite(0, 156);                                                               
    delay(5000);
    ledcWrite(1, 0);
    ledcWrite(2, 0);
    ledcWrite(0, 0);
    delay(10000);

    

}
