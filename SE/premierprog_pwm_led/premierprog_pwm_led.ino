int led = 13; //la led rouge est sur le pin 13

void setup() {

ledcAttachPin(led, 0); //on relie la led au canal PWM 0
ledcSetup(0, 5000, 8); //on configure le canal PWM 0 avec une fréquence de 5000 Hz et une résolution de 8 bits
}

void loop() {

  for (int i=0; i<=255; i++) { //on initialise i à 0 et on incrémente i à chaque tour de boucle

    ledcWrite(0, i); //chaque tour de boucle le rapport cyclique augmente de 0,4%
    delay(20); //on attend 20 ms entre chaque tour de boucle
  }
  for (int i=256; i>0; i=i-1) { //on initialise i à 256 et on décrémente i à chaque tour de boucle
    
    ledcWrite(0, i); //chaque tour de boucle le rapport cyclique diminue de 0,4%
    delay(20); //on attend 20 ms
  } 
}
