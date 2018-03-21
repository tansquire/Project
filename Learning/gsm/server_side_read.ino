#include "SIM900.h"
#include <SoftwareSerial.h>
#include "sms.h"
//SoftwareSerial Serial1(2, 3);
SMSGSM sms;
int numdata;
boolean started=false;
char smsbuffer[160];
char n[20];
char x;


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
         
         // if (sms.SendSMS("+917602304567", "Modem is ready"))
         // Serial.println("\nSMS sent OK");
          Serial.println("now i will be inside loop");
     }

}

void loop()
{
     if(started)
     {
  
        gsm.readSMS(smsbuffer, 160, n, 20);
        if(strstr(smsbuffer,"@")!=NULL && strstr(smsbuffer,"#")!=NULL)
        {
        *smsbuffer='\0';
        Serial.println("got expected");
        Serial.println("going to delete");
        x=sms.DeleteSMS(1);
        if(x==1)
        Serial.println("deleted");
        }
        
        *smsbuffer='\0';

        
    
     }
}
