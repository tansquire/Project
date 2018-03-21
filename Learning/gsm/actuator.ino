#include "SIM900.h"
#include <SoftwareSerial.h>
#include "sms.h"
SMSGSM sms;
int numdata;
boolean started=false;
char smsbuffer[160];
char n[20];
uint32_t prev_start_sending_millis;
uint32_t start_sending_interval=90000;
bool start_sending=false;
uint32_t prev_command_millis;
uint32_t command_interval=30000;
int open = 13;
int close = 9;
int opened = 4;
int remote = 6;
int closed = 5;
int x;
char data[5];
char message[30];

void setup()
{
     pinMode(open, OUTPUT); 
     pinMode(close, OUTPUT); 
     pinMode(opened, INPUT);
     pinMode(remote, INPUT);
     pinMode(closed, INPUT);
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
  if(digitalRead(remote))
  data[0]='7';
  else 
  data[0]='6';


  if(digitalRead(opened))
  data[1]='7';
  else 
  data[1]='6';

  if(digitalRead(closed))
  data[2]='7';
  else 
  data[2]='6';

  data[3]='\0';
  
  

        Serial.print("data= ");
        Serial.println(data);
        sprintf(message,"@actuatorp%sq#",data);
        Serial.print("message= ");
        Serial.println(message);
        
        gsm.readSMS(smsbuffer, 160, n, 20);
        if(strstr(smsbuffer,"@mobile#")!=NULL && start_sending==false)
        {
        *smsbuffer='\0';
        Serial.println("got expected");
        if(sms.SendSMS("+917602304567", message))
        Serial.println("\nSMS sent OK");
        sms.DeleteSMS(1);
        }

        if(strstr(smsbuffer,"@open#")!=NULL)
        {
         //open logic here
        *smsbuffer='\0';
        x=1;
        start_sending=true;
        prev_start_sending_millis=millis();
        }

        if(strstr(smsbuffer,"@close#")!=NULL)
        {
        //close logic here
        *smsbuffer='\0';
        x=2;
        start_sending=true;
        prev_start_sending_millis=millis();
        }
        
        if(millis() -prev_start_sending_millis > start_sending_interval)
        start_sending=false;
        
        if(start_sending && millis() -prev_command_millis > command_interval)
        {
        if(sms.SendSMS("+917602304567", message))
        Serial.println("\nSMS sent OK");
        sms.DeleteSMS(1);
        prev_command_millis=millis();
        }

        *smsbuffer='\0';

 if(!digitalRead(opened) && digitalRead(remote))
  {
  if(x==1)
 {
  digitalWrite(close, LOW);
  delay(5);
  digitalWrite(open, HIGH);
  x=0;

}
  }
else
digitalWrite(open, LOW);



 if(!digitalRead(closed) && digitalRead(remote))
  {
  if(x==2)
 {
   digitalWrite(open, LOW);
   delay(5);
   digitalWrite(close, HIGH);
   x=0;

}
  }
else
digitalWrite(close, LOW);


    
     }
}
