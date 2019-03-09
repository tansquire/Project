#include <SPI.h>
#include <RH_RF95.h>

// Singleton instance of the radio driver
RH_RF95 rf95;
int led = A2;
const int analogOutPin = 1;
int sensorValue = 0;        
int outputValue = 0;  
float frequency = 434.0;

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
    char value[50];
    char value1[50];
    int count;
    int i = 0;
    int j = 0;
    int n=0;
    unsigned int n1;
    bool isNeg;
    
  if (rf95.available())
  {
    // Should be a message for us now   
    uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];
    uint8_t len = sizeof(buf);
    if (rf95.recv(buf, &len))
    {
      digitalWrite(led, HIGH);
      //RH_RF95::printBuffer("request: ", buf, len);
     // Serial.println(len);
      //Serial.print("got request: ");
      //Serial.println((char*)buf);
     // Serial.print("RSSI: ");
     // Serial.println(rf95.lastRssi(), DEC);
      
      if(strstr((char*)buf, "deviceD") != NULL && strstr((char*)buf, "p") != NULL && strstr((char*)buf, "<") != NULL && strstr((char*)buf, ">") != NULL)
      {
      
      //Serial.println(*((char*)buf+8));
      while((*((char*)buf+i))!='<')
      {
       i++;
      }
      

      while((*((char*)buf+j))!='>')
      {
       j++;
      }
      //Serial.println(i);
      //Serial.println(j);
      for(n=i+1;n<=j-1;n++)
      value[n-i-1]=*((char*)buf+n);
      value[n-i-1] = '\0';
      //Serial.println(value);
      count = Toint(value,j-i-1);
      //Serial.println(count+1);
      float count1=(((count-204)*1024.0/819)*255/1024);
      float count2=count1*20.0*0.833/255.0;
      //Serial.println((int)count2);
      Serial.println(count2);
      //analogWrite(analogOutPin, (int)count1);

  


      
      }
      else
      Serial.println("bad data received");
      // Send a reply
      uint8_t data[] = "And hello back to you";
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

 

  int Toint(char str[],int len)
{
 
    int i, num = 0;
 
    for (i = 0; i < len; i++)
    {
        num = num + ((str[len - (i + 1)] - '0') * pow(10, i));
    }
 
   return num;
}