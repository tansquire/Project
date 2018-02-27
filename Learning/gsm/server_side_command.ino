#include <avr/wdt.h>
#include "SIM900.h"
#include <SoftwareSerial.h>
#include "sms.h"
int count_sent_A=0;
int count_sent_B=0;
int count_sent_C=0;
int count_sent_D=0;
int count_sent_Actuator=0;

SMSGSM sms;
int numdata;
boolean started=false;
char smsbuffer[160];
char n[20];

void setup()
{
    
     Serial.begin(9600);
     Serial.println("GSM Shield testing.");
     if (gsm.begin(2400)) 
     {
          Serial.println("\nstatus=READY");
          started=true;
     } else Serial.println("\nstatus=IDLE");

     if(started) 
     {
         
          //if (sms.SendSMS("3471234567", "Arduino SMS"))
          //Serial.println("\nSMS sent OK");
     }

}

void loop()
{
     if(started)
     {
       recvOneChar();
       
     }
}


void recvOneChar() 
{
char receivedChar;
boolean newData = false;
    if (Serial.available() > 0) 
    {
        receivedChar = Serial.read();
        newData = true;
    }
     if (newData == true) 
    {
      if(receivedChar=='l')
      {
        
      if (sms.SendSMS("+917602304567", "Arduino SMS"))
      Serial.println("\nSMS sent to lake well");
      sms.DeleteSMS(1);
      newData = false;
     
      }
      else if(receivedChar=='c')
      {
      if (sms.SendSMS("+917602304567", "Arduino SMS"))
      Serial.println("\nSMS sent to children park");
      sms.DeleteSMS(1);
      newData = false;
      }
      else if(receivedChar=='s')
      {
      if (sms.SendSMS("+917602304567", "Arduino SMS"))
      Serial.println("\nSMS sent to stuff club");
      sms.DeleteSMS(1);
      newData = false;
      }
      else if(receivedChar=='r')
      {
      if (sms.SendSMS("+917602304567", "Arduino SMS"))
      Serial.println("\nSMS sent to RR sump");
      sms.DeleteSMS(1);
      newData = false;
      }
      else if(receivedChar=='x')
      {
      if (sms.SendSMS("+917602304567", "Arduino SMS"))
      Serial.println("\nSMS sent for actuator open");
      sms.DeleteSMS(1);
      newData = false;
      }
      else if(receivedChar=='y')
      {
      if (sms.SendSMS("+917602304567", "Arduino SMS"))
      Serial.println("\nSMS sent for actuator close");
      sms.DeleteSMS(1);
      newData = false;
      }
      else
      {
      newData = false;
      return;
      }
    }
}
