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
float frequency = 868.0;
int open = 8;
int close = 9;
int opened = 4;
int remote = 3;
int closed = 5;


void setup() 
{
  pinMode(open, OUTPUT); 
   pinMode(close, OUTPUT); 
   pinMode(opened, INPUT);
    pinMode(remote, INPUT);
    pinMode(closed, INPUT);
  Serial.begin(9600);
  while (!Serial) ; 
  Serial.println("Start LoRa Client");
  if (!rf95.init())
    Serial.println("init failed");
  
  rf95.setFrequency(frequency);
  
  rf95.setTxPower(13);
  
}

void loop()
{

  Serial.println("Sending to LoRa Server");
  
  uint8_t data[4];
  data[0]=1;

if(digitalRead(remote))

  data[1]=7;
  else
  data[1]=6;
  delay(1);        

if(digitalRead(opened))

  data[2]=7;
  else
  data[2]=6;
  delay(1);   

if(digitalRead(closed))

  data[3]=7;
  else
  data[3]=6;
  delay(1);  

 
  
  rf95.send(data, sizeof(data));
  
  rf95.waitPacketSent();
  
  uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];
  uint8_t len = sizeof(buf);

  if (rf95.waitAvailableTimeout(3000))
  { 
   
    if (rf95.recv(buf, &len))
   {
      Serial.println("got reply");


     Serial.print(*buf);
      Serial.print(*(buf+1));
     Serial.print(*(buf+2));
    


  if(*(buf+1) == 1)
{
   digitalWrite(close, LOW); 
   delay(5);
   digitalWrite(open, HIGH);
}
if(*(buf+2) == 1)
{
digitalWrite(open, LOW);
delay(5);
digitalWrite(close, HIGH);
}

 
      Serial.print("RSSI: ");
      Serial.println(rf95.lastRssi(), DEC); 

     
    }
    else
    {
      Serial.println("recv failed");
    }
  }
  else
  {
    Serial.println("No reply, is LoRa server running?");
  }
  delay(5000);
}


