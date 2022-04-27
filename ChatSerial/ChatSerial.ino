#include <SoftwareSerial.h>
SoftwareSerial otroArduino(2,3);

void setup() {
  Serial.begin(9600);
  Serial.println(">>Inicializando Sistema");
  while (!Serial){
    ;
  }
  otroArduino.begin(9600);
}

void loop() {
  if(Serial.available()){
    String miPC=Serial.readString();
    otroArduino.println(miPC);
    Serial.println("Tu: "+miPC);
  }
  if(otroArduino.available()){
    String msjArd=otroArduino.readString();
    Serial.println("Usuario: "+msjArd);  
  }
}
