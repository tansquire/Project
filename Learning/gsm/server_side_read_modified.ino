#include <SoftwareSerial.h>
//SoftwareSerial Serial1(2, 3);
#include <avr/wdt.h>
int8_t answer;
int count_rcv_A=0;
int count_rcv_B=0;
int count_rcv_C=0;
int count_rcv_D=0;
uint32_t prev_display_millis;
uint32_t display_interval=2000;
uint32_t prev_delete_millis;
uint32_t delete_interval=86400000;

void setup()
{
Serial.begin(9600); 
Serial1.begin(2400);    
Serial.println("Starting...");
power_on();

delay(500);

answer = sendATcommand("AT", "OK", 2000); 
if(answer==1)
Serial.println("ok");

delay(500);

answer = sendATcommand("AT+CSQ", "OK", 2000); 
if(answer==1)
Serial.println("good signal quality");

delay(500);

answer = sendATcommand("AT+CCID", "OK", 2000); 
if(answer==1)
Serial.println("SIM is plugged");

delay(500);

answer = sendATcommand("AT+CREG?", "OK", 2000); 
if(answer==1)
Serial.println("Registered to network");

delay(500);


answer = sendATcommand("AT+CNMI=2,2,0,0,0", "OK", 2000); 
if(answer==1)
Serial.println("Received message mode set");


//SendMessage();
delay(500);
}


void loop()
{

recvWithStartEndMarkers();

if(millis() -prev_delete_millis > delete_interval)
{
answer = sendATcommand("AT+CMGD=1,4", "OK", 2000); 
if(answer==1)
Serial.println("All message deleted");
else
Serial.println("Cant delete");
prev_delete_millis=millis();
}

if(millis() -prev_display_millis > display_interval)
{
Serial.print("Serial1 size");
Serial.println(Serial1.available());
Serial.print("Serial size");
Serial.println(Serial.available());
prev_display_millis=millis();
}

}

void SendMessage()
{
    Serial.print("Setting SMS mode...");
    answer=sendATcommand("AT+CMGF=1", "OK", 3000);    // sets the SMS mode to text
    if(answer==1)
    Serial.println("SMS mode set");
    else
    {
    Serial.println("Error setting SMS mode");
    softwareReset( WDTO_60MS);
    }
    Serial.println("Sending SMS");
    answer = sendATcommand("AT+CMGS=\"+917602304567\"\r", ">", 3000);    // send the SMS number
    if (answer == 1)
    {
        Serial1.println("Test sms-Sketch is ready to run");
        Serial1.write(0x1A);
        answer = sendATcommand("", "OK", 30000);
        if (answer == 1)
        {
            Serial.println("Initial SMS Sent ");    
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
        softwareReset( WDTO_60MS);
    }
}


void recvWithStartEndMarkers() 
{
const byte numChars = 100;
char receivedChars[numChars];
char message[numChars];
boolean newData = false;


    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '@';
    char endMarker = '#';
    char rc;
    int c;
 
    while (Serial1.available() > 0 && newData == false) 
    {
        rc = Serial1.read();

        if (recvInProgress == true) 
        {
            if (rc != endMarker) 
            {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) 
                {
                    ndx = numChars - 1;
                }
            }
            else 
            {
                receivedChars[ndx] = '\0'; // terminate the string
                c=ndx;
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) 
        {
            recvInProgress = true;
        }
    }


if (newData == true) 
    {
        Serial.print(c);
        if ((c==18||c==17||c==16||c==15||c==14||c==13) && strstr(receivedChars, "deviceA") != NULL && strstr(receivedChars, "p") != NULL && strstr(receivedChars, "q")!=NULL && strstr(receivedChars, "a") != NULL && strstr(receivedChars, "b") != NULL)
        {
        Serial.print("Serial1 size");
        Serial.println(Serial1.available());
        Serial.print("Serial size");
        Serial.println(Serial.available());
        count_rcv_A++;
        Serial.print("SMS No--");
        Serial.print(count_rcv_A);
        Serial.print("---");
        Serial.println(receivedChars); 
        
        newData = false;
        }

        else if ((c==18||c==17||c==16||c==15||c==14||c==13) && strstr(receivedChars, "deviceB") != NULL && strstr(receivedChars, "p") != NULL && strstr(receivedChars, "q")!= NULL && strstr(receivedChars, "a") != NULL && strstr(receivedChars, "b") != NULL)
        {
        Serial.print("Serial1 size");
        Serial.println(Serial1.available());
        Serial.print("Serial size");
        Serial.println(Serial.available());
        count_rcv_B++;
        Serial.print("SMS No--");
        Serial.print(count_rcv_B);
        Serial.print("---");
        Serial.println(receivedChars); 
        newData = false;
        }
        else if ((c==18||c==17||c==16||c==15||c==14||c==13) && strstr(receivedChars, "deviceC") != NULL && strstr(receivedChars, "p") != NULL && strstr(receivedChars, "q")!= NULL && strstr(receivedChars, "a") != NULL && strstr(receivedChars, "b") != NULL)
        {
        Serial.print("Serial1 size");
        Serial.println(Serial1.available());
        Serial.print("Serial size");
        Serial.println(Serial.available());
        count_rcv_C++;
        Serial.print("SMS No--");
        Serial.print(count_rcv_C);
        Serial.print("---");
        Serial.println(receivedChars); 
        newData = false;
        }
         else if ((c==18||c==17||c==16||c==15||c==14||c==13) && strstr(receivedChars, "deviceD") != NULL && strstr(receivedChars, "p") != NULL && strstr(receivedChars, "q")!= NULL && strstr(receivedChars, "a") != NULL && strstr(receivedChars, "b") != NULL)
        {
        Serial.print("Serial1 size");
        Serial.println(Serial1.available());
        Serial.print("Serial size");
        Serial.println(Serial.available());
        count_rcv_D++;
        Serial.print("SMS No--");
        Serial.print(count_rcv_D);
        Serial.print("---");
        Serial.println(receivedChars); 
        newData = false;
        }

         else if (c==13 && strstr(receivedChars, "actuator") != NULL && strstr(receivedChars, "p") != NULL && strstr(receivedChars, "q")!= NULL)
        {
        Serial.print("Serial1 size");
        Serial.println(Serial1.available());
        Serial.print("Serial size");
        Serial.println(Serial.available());
        Serial.print("SMS No--");
        Serial.print("---");
        Serial.println(receivedChars); 
        newData = false;
        }

        else
        {
        Serial.println("Non-sense data found, I am restarting");
        softwareReset( WDTO_60MS);
        }
      
      }

}

int8_t sendATcommand(char* ATcommand, char* expected_answer, unsigned int timeout)
{

    uint8_t x=0,  answer=0;
    char response[100];
    unsigned long previous;

    memset(response, '\0', 100);    // Initialice the string

    delay(100);

    while( Serial1.available() > 0) Serial1.read();    // Clean the input buffer
    delay(1000);

    Serial1.println(ATcommand);    // Send the AT command 


    x = 0;
    previous = millis();

    // this loop waits for the answer
    do{
        if(Serial1.available() != 0){    // if there are data in the UART input buffer, reads it and checks for the asnwer
            response[x] = Serial1.read();
            x++;
            if (strstr(response, expected_answer) != NULL)    // check if the desired answer is in the response of the module
            {
                answer = 1;
            }
        }
    }while((answer == 0) && ((millis() - previous) < timeout));    // Waits for the asnwer with time out

    return answer;
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

void delete_sms()

{
answer = sendATcommand("AT+CMGD=1,4", "OK", 3000); 
if(answer==1)
Serial.println("All message deleted");
else
{
Serial.println("Cant delete");
softwareReset( WDTO_60MS);
}
}


void softwareReset( uint8_t prescaller) 
{

  wdt_enable( prescaller);
  
  while(1) {}
}




