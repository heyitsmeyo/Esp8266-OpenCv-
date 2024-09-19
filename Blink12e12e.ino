/*
  ESP8266 Blink by Simon Peter
  Blink the blue LED on the ESP-01 module
  This example code is in the public domain

  The blue LED on the ESP-01 module is connected to GPIO1
  (which is also the TXD pin; so we cannot use Serial.print() at the same time)

  Note that this sketch uses LED_BUILTIN to find the pin with the internal LED
*/

#include<ESP8266WiFi.h> 

char* ssid = "";
char* password = "";


WiFiServer server(3030);



void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);  // Initialize the LED_BUILTIN pin as an output


WiFi.begin(ssid , password);

while (WiFi.status() != WL_CONNECTED){
  delay(1000);
  Serial.print("connecting to WIFI ....");

  
}
  Serial.print("connected " );
  Serial.print("ip is "  ); 
  Serial.print(WiFi.localIP()) ;
  server.begin();
  Serial.print("\n Server started");
}
void loop() {

  WiFiClient  client = server.available() ;
  if (client){
    while(client.connected()){
      if(client.available()){
        char received = client.read();
        if(received == '1') {
           digitalWrite(LED_BUILTIN, HIGH);
        }
        else if (received == '0') {
          digitalWrite(LED_BUILTIN, LOW) ;
        }
      }
    }
    client.stop();
  }
                  
}
