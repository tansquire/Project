#include "SIM900.h"
#include <SoftwareSerial.h>
#include "sms.h"
SMSGSM sms;
int numdata;
boolean started=false;
char smsbuffer[160];
char n[20];


void setup()
{
    
     Serial.begin(9600);
     Serial.println("GSM Shield testing.");
     if (gsm.begin(9600)) 
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
       
        sms.DeleteSMS(1);
    
     }
}
