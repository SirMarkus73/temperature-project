#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>

#define PIN_LED 2

// put function declarations here:
bool isWifiConnected();
void sendTemperature(int temperature);
void printWifiConnectionLoader();

// Constants
const char *ssid = "sr73";
const char *password = "zdf09876";
const String apiHost = "192.168.117.3:9000";
const String apiUrl = "http://" + apiHost;

const float minTemperature = 20.4;
const float maxTemperature = 30.2;

// Variables
int temperature = 20;

void setup()
{
  Serial.begin(115200);
  pinMode(PIN_LED, OUTPUT);
  WiFi.begin(ssid, password);
  Serial.print("Connecting to wifi.");
  while (!isWifiConnected())
  {
    printWifiConnectionLoader();
  }

  Serial.println("\nConnected to the WiFi network");
  analogWrite(PIN_LED, HIGH);
}

void loop()
{
  temperature = random(minTemperature, maxTemperature);
  Serial.printf("Random temperature generated: %d\n", temperature);
  if (isWifiConnected())
  {
    sendTemperature(temperature);
    delay(5000);
  }
  else
  {
    Serial.print("No Wifi connection, reconnecting...");
    analogWrite(PIN_LED, LOW);
    WiFi.reconnect();

    while (!isWifiConnected())
    {
      printWifiConnectionLoader();
    }
    analogWrite(PIN_LED, HIGH);
    Serial.println("\nConnected to the WiFi network");
  }
}

// put function definitions here:

bool isWifiConnected()
{
  return WiFi.status() == WL_CONNECTED;
}

void sendTemperature(int temperature)
{
  HTTPClient http;

  http.begin(apiUrl + "/temperature?temperature=" + String(temperature));
  http.addHeader("Content-Type", "application/json");
  int httpResponseCode = http.POST("");
  Serial.printf("Sending POST to %s \n", (apiUrl + "/temperature").c_str());

  if (httpResponseCode > 0)
  {
    String response = http.getString();
    printf("ResponseCode: %d, Response %s\n", httpResponseCode, response.c_str());
  }
  else
  {
    Serial.printf("Error on sending POST: %d\n", httpResponseCode);
  }

  http.end();
}

void printWifiConnectionLoader()
{
  analogWrite(PIN_LED, HIGH);
  delay(300);
  analogWrite(PIN_LED, LOW);
  Serial.print(".");
  delay(300);
}