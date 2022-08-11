int vib = 26; //Le pin 26 correspond à la sortie A0 de la carte
int ch = 25;
int vent = 21;
int command = 0;
int i = 0;
int count =0;
void setup() {

Serial.begin(76800); 
ledcAttachPin(vib, 1); //On relie la sortie A0 au canal PWM 1
ledcAttachPin(ch, 2);
ledcAttachPin(vent, 3);
ledcSetup(1, 5000, 8);//On configure le canal PWM 1 avec une fréquence de 5000 Hz et une résolution de 8 bits
ledcSetup(2, 5000, 8);
ledcSetup(3, 5000, 8);
}

void vibration1() {  //La fonction effectue deux vibrations courtes
    ledcWrite(1, 256/5);
}
void vibration2() {  //La fonction effectue deux vibrations courtes
    ledcWrite(1, 2*256/5);
}
void vibration3() {  //La fonction effectue deux vibrations courtes
    ledcWrite(1, 3*256/5);
}
void vibration4() {  //La fonction effectue deux vibrations courtes
    ledcWrite(1, 4*256/5);
}
void vibration5() {  //La fonction effectue deux vibrations courtes
    ledcWrite(1, 256);

}

void chauffage() { //La fonction effectue une longue vibration
  ledcWrite(2, 256/5);
}
void chauffage2() { //La fonction effectue une longue vibration
  ledcWrite(2, 2*256/5);
}
void chauffage3() { //La fonction effectue une longue vibration
  ledcWrite(2, 3*256/5);
}
void chauffage4() { //La fonction effectue une longue vibration
  ledcWrite(2, 4*256/5);
}
void chauffage5() { //La fonction effectue une longue vibration
  ledcWrite(2, 256);
}

void ventilo1() { //La fonction effectue une longue vibration
  ledcWrite(3, 256/5);
  delay(10000);
  ledcWrite(3, 0); 
}

void ventilo2() { //La fonction effectue une longue vibration
  ledcWrite(3, 2*256/5);
}
void ventilo3() { //La fonction effectue une longue vibration
  ledcWrite(3, 3*256/5);
}
void ventilo4() { //La fonction effectue une longue vibration
  ledcWrite(3, 4*256/5);
}
void ventilo5() { //La fonction effectue une longue vibration
  ledcWrite(3, 256);
}

boolean parse_cmd(byte letter) {
    

    if (letter=='a') { //Si le caractère recu est l on enclenche une longue vibration et on écrit OK
      Serial.write("OK");
      command=0;
      return true;
    }
    else if (letter=='b') { //Si le caractère recu est l on enclenche une longue vibration et on écrit OK
      Serial.write("OK");
      command=1;
      return true;
    }
    else if (letter=='c') { //Si le caractère recu est l on enclenche une longue vibration et on écrit OK
      Serial.write("OK");
      command=2;
      return true;
    }
    else if (letter=='d') { //Si le caractère recu est l on enclenche une longue vibration et on écrit OK
      Serial.write("OK");
      command=3;
      return true;
    }
    else if (letter=='e') { //Si le caractère recu est l on enclenche une longue vibration et on écrit OK
      Serial.write("OK");
      command=4;
      return true;
    }
    else if (letter=='f') { //Si le caractère recu est l on enclenche une longue vibration et on écrit OK
      Serial.write("OK");
      command=5;
      return true;
    }
    else if (letter=='g') { //Si le caractère recu est l on enclenche une longue vibration et on écrit OK
      Serial.write("OK");
      command=10;
      return true;
    }
    else if (letter=='h') { //Si le caractère recu est l on enclenche une longue vibration et on écrit OK
      Serial.write("OK");
      command=11;
      return true;
    }
    else if (letter=='i') { //Si le caractère recu est l on enclenche une longue vibration et on écrit OK
      Serial.write("OK");
      command=12;
      return true;
    }
    else if (letter=='j') { //Si le caractère recu est l on enclenche une longue vibration et on écrit OK
      Serial.write("OK");
      command=13;
      return true;
    }
    else if (letter=='k') { //Si le caractère recu est l on enclenche une longue vibration et on écrit OK
      Serial.write("OK");
      command=14;
      return true;
    }
    else if (letter=='l') { //Si le caractère recu est l on enclenche une longue vibration et on écrit OK
      Serial.write("OK");
      command=15;
      return true;
    }
    else if (letter=='m') { //Si le caractère recu est l on enclenche une longue vibration et on écrit OK
      Serial.write("OK");
      command=20;
      return true;
    }
    else if (letter=='n') { //Si le caractère recu est l on enclenche une longue vibration et on écrit OK
      Serial.write("OK");
      command=21;
      return true;
    }
    else if (letter=='o') { //Si le caractère recu est l on enclenche une longue vibration et on écrit OK
      Serial.write("OK");
      command=22;
      return true;
    }
    else if (letter=='p') { //Si le caractère recu est l on enclenche une longue vibration et on écrit OK
      Serial.write("OK");
      command=23;
      return true;
    }
    else if (letter=='q') { //Si le caractère recu est l on enclenche une longue vibration et on écrit OK
      Serial.write("OK");
      command=24;
      return true;
    }
    else if (letter=='r') { //Si le caractère recu est l on enclenche une longue vibration et on écrit OK
      Serial.write("OK");
      command=25;
      return true;
    }
    
    else if (letter=='\n'){
      return false;
    } //On distingue le cas du retour a la ligne des autres caracteres

    else {
      Serial.write("BAD"); //Pour tout autre caractere on ecrit KO
      return false;
    }
  }

void apply_cmd() {

  if (command/10<1){
    if (command == 1){
      chauffage();
    }
    else if (command ==2) {
      chauffage2();
    }
    else if (command ==3) {
      chauffage3();
    }
    else if (command ==4) {
      chauffage4();
    }
    else if (command ==5) {
      chauffage5();
    }
    else if (command==0) {
      ledcWrite(2, 0);
      
    }
  }

  else if (command/10<2){
    if (command == 11){
      ventilo1();
    }
    else if (command ==12) {
      ventilo2();
    }
    else if (command ==13) {
      ventilo3();
    }
    else if (command ==14) {
      ventilo4();
    }
    else if (command ==15) {
      ventilo5();
    }
    else if (command == 10){
      ledcWrite(3, 0);
    }
  }  
  else if (command/10<3){
    if (command == 21){
      vibration1();
    }
    else if (command ==22) {
      vibration2();
    }
    else if (command ==23) {
      vibration3();
    }
    else if (command ==24) {
      vibration4();
    }
    else if (command ==25) {
      vibration5();
    }
    else if (command==20) {
      ledcWrite(1, 0);
    }
    
  }
}

void loop() {
  count +=1;

  if(Serial.available()) {
     if ( parse_cmd(Serial.read())) {
        apply_cmd();
     }
  }
  if (count==3){
    delay (10000);
    ledcWrite(2, 0);
    ledcWrite(3, 0);
    ledcWrite(1, 0);
    
  }
  
}
