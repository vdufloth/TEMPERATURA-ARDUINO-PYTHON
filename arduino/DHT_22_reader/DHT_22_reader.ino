#include "DHT.h"

//Constants
#define DHTPIN 2     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino


//Variables
int chk;
float hum;  //Stores humidity value
float temp; //Stores temperature value

void setup()
{
    Serial.begin(9600);
    dht.begin();

}

void loop()
{
    hum = dht.readHumidity();
    temp= dht.readTemperature();
    Serial.print(hum); //HUMIDITY
    Serial.print(";");
    Serial.print(temp); //TEMPERATURE
    Serial.println(";");
    delay(300000); //Delay 2 sec.
}
