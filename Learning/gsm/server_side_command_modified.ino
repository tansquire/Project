#include <SoftwareSerial.h>
boolean started=false;
char smsbuffer[160];
char n[20];
int8_t answer;
SoftwareSerial mySerial(2,3);

void setup()
{
Serial.begin(9600); 
mySerial.begin(9600);    //use 2400 for SIM 900
Serial.println("Starting...");
power_on();
delay(500);

answer = sendATcommand("AT", "OK", 3000); 
if(answer==1)
Serial.println("ok");
delay(500);

answer = sendATcommand("AT+CSQ", "OK", 3000); 
if(answer==1)
Serial.println("good signal quality");
delay(500);

answer = sendATcommand("AT+CCID", "OK", 3000); 
if(answer==1)
Serial.println("SIM is plugged");
delay(500);

answer = sendATcommand("AT+CREG?", "OK", 3000); 
if(answer==1)
Serial.println("Registered to network");
delay(500);


answer = sendATcommand("AT+CNMI=2,2,0,0,0", "OK", 3000); 
if(answer==1)
Serial.println("Received message mode set");
Serial.println("Waiting to send sms..");
delay(500);

}

void loop()
{

recvOneChar();
       
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
      SendMessage_lw();  
      delay(1000);
      delete_sms();
      newData = false;
     
      }
      else if(receivedChar=='c')
      {
      SendMessage_cp();  
      delay(1000);
      delete_sms();
      newData = false;
      }
      else if(receivedChar=='s')
      {
      SendMessage_sc();  
      delay(1000);
      delete_sms();
      newData = false;
      }
      else if(receivedChar=='r')
      {
      SendMessage_rr();  
      delay(1000);
      delete_sms();
      newData = false;
      }
      else if(receivedChar=='x')
      {
      SendMessage_ao();  
      delay(1000);
      delete_sms();
      newData = false;
      }
      else if(receivedChar=='y')
      {
      SendMessage_ac();  
      delay(1000);
      delete_sms();
      newData = false;
      }
      else
      {
      newData = false;
      return;
      }
    }
}


int8_t sendATcommand(char* ATcommand, char* expected_answer, unsigned int timeout){

    uint8_t x=0,  answer=0;
    char response[100];
    unsigned long previous;

    memset(response, '\0', 100);    // Initialice the string

    delay(100);

    while( mySerial.available() > 0) mySerial.read();    // Clean the input buffer
    delay(1000);

    mySerial.println(ATcommand);    // Send the AT command 


    x = 0;
    previous = millis();

    // this loop waits for the answer
    do{
        if(mySerial.available() != 0){    // if there are data in the UART input buffer, reads it and checks for the asnwer
            response[x] = mySerial.read();
            x++;
            if (strstr(response, expected_answer) != NULL)    // check if the desired answer is in the response of the module
            {
                answer = 1;
            }
        }
    }while((answer == 0) && ((millis() - previous) < timeout));    // Waits for the asnwer with time out

    return answer;
}

void SendMessage_lw()
{
    Serial.print("Setting SMS mode...");
    answer=sendATcommand("AT+CMGF=1", "OK", 3000);    // sets the SMS mode to text
    if(answer==1)
    Serial.println("SMS mode set");
    else
    {
    Serial.println("Error setting SMS mode");
    }
    Serial.println("Sending SMS");
    answer = sendATcommand("AT+CMGS=\"+917602304567\"\r", ">", 3000);    // send the SMS number
    if (answer == 1)
    {
        mySerial.println("Arduino SMS");
        mySerial.write(0x1A);
        answer = sendATcommand("", "OK", 30000);
        if (answer == 1)
        {
            Serial.println("\nSMS sent to lake well");   
        }
        else
        {
            Serial.println("Please check balance");
        }
    }
    else
    {
        Serial.print("error ");
        Serial.println(answer, DEC);
        
    }
}

void SendMessage_cp()
{
    Serial.print("Setting SMS mode...");
    answer=sendATcommand("AT+CMGF=1", "OK", 3000);    // sets the SMS mode to text
    if(answer==1)
    Serial.println("SMS mode set");
    else
    {
    Serial.println("Error setting SMS mode");
    }
    Serial.println("Sending SMS");
    answer = sendATcommand("AT+CMGS=\"+917602304567\"\r", ">", 3000);    // send the SMS number
    if (answer == 1)
    {
        mySerial.println("Arduino SMS");
        mySerial.write(0x1A);
        answer = sendATcommand("", "OK", 30000);
        if (answer == 1)
        {
            Serial.println("\nSMS sent to children Park");   
        }
        else
        {
            Serial.println("Please check balance");
        }
    }
    else
    {
        Serial.print("error ");
        Serial.println(answer, DEC);
        
    }
}
void SendMessage_sc()
{
    Serial.print("Setting SMS mode...");
    answer=sendATcommand("AT+CMGF=1", "OK", 3000);    // sets the SMS mode to text
    if(answer==1)
    Serial.println("SMS mode set");
    else
    {
    Serial.println("Error setting SMS mode");
    }
    Serial.println("Sending SMS");
    answer = sendATcommand("AT+CMGS=\"+917602304567\"\r", ">", 3000);    // send the SMS number
    if (answer == 1)
    {
        mySerial.println("Arduino SMS");
        mySerial.write(0x1A);
        answer = sendATcommand("", "OK", 30000);
        if (answer == 1)
        {
            Serial.println("\nSMS sent to stuff club");   
        }
        else
        {
            Serial.println("Please check balance");
        }
    }
    else
    {
        Serial.print("error ");
        Serial.println(answer, DEC);
        
    }
}
void SendMessage_rr()
{
    Serial.print("Setting SMS mode...");
    answer=sendATcommand("AT+CMGF=1", "OK", 3000);    // sets the SMS mode to text
    if(answer==1)
    Serial.println("SMS mode set");
    else
    {
    Serial.println("Error setting SMS mode");
    }
    Serial.println("Sending SMS");
    answer = sendATcommand("AT+CMGS=\"+917358699052\"\r", ">", 3000);    // send the SMS number
    if (answer == 1)
    {
        mySerial.println("@start#");
        mySerial.write(0x1A);
        answer = sendATcommand("", "OK", 30000);
        if (answer == 1)
        {
            Serial.println("\nSMS sent to children Park");   
        }
        else
        {
            Serial.println("Please check balance");
        }
    }
    else
    {
        Serial.print("error ");
        Serial.println(answer, DEC);
        
    }
}

void SendMessage_ao()
{
    Serial.print("Setting SMS mode...");
    answer=sendATcommand("AT+CMGF=1", "OK", 3000);    // sets the SMS mode to text
    if(answer==1)
    Serial.println("SMS mode set");
    else
    {
    Serial.println("Error setting SMS mode");
    }
    Serial.println("Sending SMS");
    answer = sendATcommand("AT+CMGS=\"+919952987526\"\r", ">", 3000);    // send the SMS number
    if (answer == 1)
    {
        mySerial.println("@open#");
        mySerial.write(0x1A);
        answer = sendATcommand("", "OK", 30000);
        if (answer == 1)
        {
            Serial.println("\nSMS sent to actuator for open");   
        }
        else
        {
            Serial.println("Please check balance");
        }
    }
    else
    {
        Serial.print("error ");
        Serial.println(answer, DEC);
        
    }
}

void SendMessage_ac()
{
    Serial.print("Setting SMS mode...");
    answer=sendATcommand("AT+CMGF=1", "OK", 3000);    // sets the SMS mode to text
    if(answer==1)
    Serial.println("SMS mode set");
    else
    {
    Serial.println("Error setting SMS mode");
    }
    Serial.println("Sending SMS");
    answer = sendATcommand("AT+CMGS=\"+919952987526\"\r", ">", 3000);    // send the SMS number
    if (answer == 1)
    {
        mySerial.println("@close#");
        mySerial.write(0x1A);
        answer = sendATcommand("", "OK", 30000);
        if (answer == 1)
        {
            Serial.println("\nSMS sent to actuator for close");   
        }
        else
        {
            Serial.println("Please check balance");
        }
    }
    else
    {
        Serial.print("error ");
        Serial.println(answer, DEC);
        
    }
}

void delete_sms()

{
answer = sendATcommand("AT+CMGD=1,4", "OK", 3000); 
if(answer==1)
Serial.println("All message deleted");
else
{
Serial.println("Cant delete");

}
}

void power_on()
{

    uint8_t answer=0;

    // checks if the module is started
    answer = sendATcommand("AT", "OK", 3000);
    if (answer == 0)
    {
        
        while(answer == 0){     // Send AT every two seconds and wait for the answer
            answer = sendATcommand("AT", "OK", 3000);    
        }
    }
    Serial.println("modem ready");

}

