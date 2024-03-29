#include <RadioHead.h>
#include <RHGenericSPI.h>
#include <RH_NRF51.h>
#include <RHCRC.h>
#include <RHRouter.h>
#include <RH_RF95.h>
#include <RHSoftwareSPI.h>
#include <RHDatagram.h>
#include <RH_CC110.h>
#include <RH_E32.h>
#include <RHHardwareSPI.h>
#include <RH_RF24.h>
#include <RH_RF22.h>
#include <RHSPIDriver.h>
#include <RH_MRF89.h>
#include <RHEncryptedDriver.h>
#include <RHGenericDriver.h>
#include <RH_NRF24.h>
#include <RHReliableDatagram.h>
#include <RHTcpProtocol.h>
#include <RH_Serial.h>
#include <RH_ASK.h>
#include <RHNRFSPIDriver.h>
#include <RH_TCP.h>
#include <RH_RF69.h>
#include <RHMesh.h>
#include <RH_NRF905.h>

/*
  LoRa Simple Arduino Server :
  Support Devices: 
  * LoRa Mini
  * LoRa Shield + Arduino;
  * LoRa GPS Shield + Arduino. 
  
  Example sketch showing how to create a simple messageing server, 
  with the RH_RF95 class. RH_RF95 class does not provide for addressing or
  reliability, so you should only use RH_RF95 if you do not need the higher
  level messaging abilities.

  It is designed to work with the other example LoRa Simple Client

  modified 16 11 2016
  by Edwin Chen <support@dragino.com>
  Dragino Technology Co., Limited
*/

#include <SPI.h>
#include <RH_RF95.h>

// Singleton instance of the radio driver
RH_RF95 rf95;

int led = A2;
float frequency = 868.0;
char input1;

void setup() 
{
  pinMode(led, OUTPUT);     
  Serial.begin(9600);
  while (!Serial) ; // Wait for serial port to be available
  //Serial.println("Start Sketch");
  if (!rf95.init())
    Serial.println("init failed");
  // Setup ISM frequency
  rf95.setFrequency(frequency);
  // Setup Power,dBm
  rf95.setTxPower(13);
  // Defaults BW Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on
  //Serial.print("Listening on frequency: ");
  //Serial.println(frequency);
}

void loop()
{
  if (rf95.available())
  {
    // Should be a message for us now   
    uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];
    uint8_t len = sizeof(buf);
    if (rf95.recv(buf, &len))
    {
      digitalWrite(led, HIGH);
     // RH_RF95::printBuffer("request: ", buf, len);
     //Serial.println("got request");
      //Serial.println((char*)buf);
     Serial.print(*(buf+1));
     Serial.print(*(buf+2));
     Serial.println(*(buf+3));
     delay(1);
      

input1=Serial.read();
//if(input1 == 'c') 
//{
 //Serial.println(*((char*)buf+2));
 //Serial.println(*(buf+2));
          
  //Serial.println(*(buf+2));
  //delay(1); // delay in between reads for stability
//}









      
     // Serial.print("RSSI: ");
     // Serial.println(rf95.lastRssi(), DEC);
      
      // Send a reply

uint8_t data[3];
  data[0]=8;
  data[1]=0;
  data[2]=0;




  if(input1 == 'a')
  data[1]=1;

  if(input1 == 'b') 
  data[1]=2;


      
      rf95.send(data, sizeof(data));
      rf95.waitPacketSent();
      //Serial.println("Sent a reply");
      digitalWrite(led, LOW);
    }
    else
    {
      Serial.println("recv failed");
    }
  }
}


