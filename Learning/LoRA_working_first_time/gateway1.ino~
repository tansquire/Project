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


#include <SPI.h>
#include <RH_RF95.h>

RH_RF95 rf95;

int led = A2;
float frequency = 868.0;
char input1;

void setup() 
{
  pinMode(led, OUTPUT);     
  Serial.begin(9600);
  while (!Serial) ; 
  if (!rf95.init())
    Serial.println("init failed");
  
  rf95.setFrequency(frequency);
  
  rf95.setTxPower(13);
  
}

void loop()
{
  if (rf95.available())
  {
    
    uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];
    uint8_t len = sizeof(buf);
    if (rf95.recv(buf, &len))
    {
      digitalWrite(led, HIGH);
     
     Serial.print(*(buf+1));
     Serial.print(*(buf+2));
     Serial.print(*(buf+3));
     delay(1);
      

input1=Serial.read();
uint8_t data[3];
  data[0]=8;
  data[1]=0;
  data[2]=0;

 if(input1 == 'a')
  data[1]=1;

  if(input1 == 'b') 
  data[2]=1;


      
      rf95.send(data, sizeof(data));
      rf95.waitPacketSent();
      
      digitalWrite(led, LOW);
    }
    else
    {
      Serial.println("recv failed");
    }
  }
}


