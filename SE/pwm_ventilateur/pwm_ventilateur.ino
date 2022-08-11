int vib = 26; //Le pin 26 correspond à la sortie A0 de la carte

void setup() {

ledcAttachPin(vib, 1); //On relie la sortie A0 au canal PWM 1
ledcSetup(1, 5000, 8); //On configure le canal PWM 1 avec une fréquence de 5000 Hz et une résolution de 8 bits
}

void loop() {
  
  for (int i=256; i>200; i=i-1) { //On descend pas en dessous d'un rapport cyclique de 39% qui correspond à la tension seuil
    
    ledcWrite(1, i); 
    delay(300); //On attend 100 ms entre chaque itération
  } 

  for (int i=200; i<=255; i++) { 

    ledcWrite(1, i);  
    delay(300); 
  }

}
