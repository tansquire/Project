void setup()
{
Serial.begin(9600);
}

void loop()
{
for(long x=0; x<20; x++)

{
Serial.println(x);
delay(1000);
}

}
