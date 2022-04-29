#include <SoftwareSerial.h>
SoftwareSerial otroArduino(2,3);

void setup() {
  Serial.begin(57600);
  Serial.println(">>Inicializando Sistema");
  while (!Serial){
    ;
  }
  otroArduino.begin(57600);
}

void loop() {
  if(Serial.available()){
    String miPC=Serial.readString();
    otroArduino.println(miPC);
    //Serial.println("Tu: "+miPC);
  }
  if(otroArduino.available()){
    String msjArd=otroArduino.readString();
    Serial.println(msjArd)
    //Serial.println("Usuario: "+msjArd);  
  }
}
