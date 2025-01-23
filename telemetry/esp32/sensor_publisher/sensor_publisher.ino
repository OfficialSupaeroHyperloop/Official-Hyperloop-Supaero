#include <Config.h>
#include <Helpers.h>
#include <Logging.h>
#include <MqttClient.h>
#include <MqttClientSetup.h>
#include <Outbox.h>
#include <TypeDefs.h>
#include <espMqttClient.h>
//#include <espMqttClientAsync.h>
//#include <AsyncTCP.h>
#include <Wire.h>
#include <WiFi.h>

#define WIFI_SSID "ferrohotspot"
#define WIFI_PASSWORD "12123434"

#define MQTT_HOST IPAddress(10, 70, 4, 38)
#define MQTT_PORT 1883
#define MQTT_USER "sensor"
#define MQTT_PASS "121234"

const int trigPin = 32;
const int echoPin = 33;

#define SOUND_SPEED 0.034
#define CM_TO_INCH 0.393701

long duration;
float distanceM;

// char *user = "sensor";
// char *password = "121234";

espMqttClient mqttClient;
bool reconnectMqtt = false;
uint32_t lastReconnect = 0;

// espMqttClient& setCredentials(const char* user, const char* password);

void connectToWiFi() { //connects to wifi
  Serial.println("Connecting to Wi-Fi...");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
}

void connectToMqtt() { // connect to MQTT. Print "connecting failed", if unsuccesful.
  Serial.println("Connecting to MQTT...");
  if (!mqttClient.connect()) {
    reconnectMqtt = true;
    lastReconnect = millis();
    Serial.println("Connecting failed.");
  } else {
    reconnectMqtt = false;
  }
}

void WiFiEvent(WiFiEvent_t event) { // Print WiFi connected when connected to a WiFi. Print own IP Address too.
  Serial.printf("[WiFi-event] event: %d\n", event);
  switch(event) {
  case SYSTEM_EVENT_STA_GOT_IP:
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
    connectToMqtt();
    break;
  case SYSTEM_EVENT_STA_DISCONNECTED:
    Serial.println("WiFi lost connection");
    break;
  default:
    break;
  }
}

void onMqttConnect(bool sessionPresent) { //Print "Connected to MQTT" when succesfully connected to MQTT.
  Serial.println("Connected to MQTT.");
  Serial.print("Session present: ");
  Serial.println(sessionPresent);
  uint16_t packetIdSub = mqttClient.subscribe("foo/bar", 2);
  Serial.print("Subscribing at QoS 2, packetId: ");
  Serial.println(packetIdSub);
  mqttClient.publish("foo/bar", 0, true, "test 1");
  Serial.println("Publishing at QoS 0");
  uint16_t packetIdPub1 = mqttClient.publish("foo/bar", 1, true, "test 2");
  Serial.print("Publishing at QoS 1, packetId: ");
  Serial.println(packetIdPub1);
  uint16_t packetIdPub2 = mqttClient.publish("foo/bar", 2, true, "test 3");
  Serial.print("Publishing at QoS 2, packetId: ");
  Serial.println(packetIdPub2);
}

void onMqttDisconnect(espMqttClientTypes::DisconnectReason reason) { //MQTT disconnected, print with reason.
  Serial.printf("Disconnected from MQTT: %u.\n", static_cast<uint8_t>(reason));

  if (WiFi.isConnected()) {
    reconnectMqtt = true;
    lastReconnect = millis();
  }
}

void onMqttSubscribe(uint16_t packetId, const espMqttClientTypes::SubscribeReturncode* codes, size_t len) { // Subscribe to a topic.
  Serial.println("Subscribe acknowledged.");
  Serial.print("  packetId: ");
  Serial.println(packetId);
  for (size_t i = 0; i < len; ++i) {
    Serial.print("  qos: ");
    Serial.println(static_cast<uint8_t>(codes[i]));
  }
}

void onMqttUnsubscribe(uint16_t packetId) { // Unsubscribe from a topic.
  Serial.println("Unsubscribe acknowledged.");
  Serial.print("  packetId: ");
  Serial.println(packetId);
}

void onMqttMessage(const espMqttClientTypes::MessageProperties& properties, const char* topic, const uint8_t* payload, size_t len, size_t index, size_t total) { // Publish successful
  (void) payload;
  Serial.println("Publish received.");
  Serial.print("  topic: ");
  Serial.println(topic);
  Serial.print("  qos: ");
  Serial.println(properties.qos);
  Serial.print("  dup: ");
  Serial.println(properties.dup);
  Serial.print("  retain: ");
  Serial.println(properties.retain);
  Serial.print("  len: ");
  Serial.println(len);
  Serial.print("  index: ");
  Serial.println(index);
  Serial.print("  total: ");
  Serial.println(total);
}

void onMqttPublish(uint16_t packetId) { //Publish start
  Serial.println("Publish acknowledged.");
  Serial.print("  packetId: ");
  Serial.println(packetId);
}

void floatToByteArray(float value, byte* buffer) {
  union {
    float f;
    uint32_t i;
  } u;
  
  u.f = value;
  for (int i = 0; i < sizeof(u.i); ++i) {
    byte b = u.i >> ((sizeof(u.i) - 1 - i) * CHAR_BIT);
    buffer[i] = b & 0xFF; // Mask to ensure we get a single byte
  }
}

void setup() {
  Serial.begin(115200);

  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input

  Serial.println();
  Serial.println();

  WiFi.setAutoConnect(false);
  WiFi.setAutoReconnect(true);
  WiFi.onEvent(WiFiEvent);

  mqttClient.onConnect(onMqttConnect);
  mqttClient.onDisconnect(onMqttDisconnect);
  mqttClient.onSubscribe(onMqttSubscribe);
  mqttClient.onUnsubscribe(onMqttUnsubscribe);
  mqttClient.onMessage(onMqttMessage);
  mqttClient.onPublish(onMqttPublish);
  mqttClient.setServer(MQTT_HOST, MQTT_PORT);

  connectToWiFi();
}

void loop() {
  
  static uint32_t currentMillis = millis();

  if (reconnectMqtt && currentMillis - lastReconnect > 5000) {
    connectToMqtt();
  }

    // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);

  distanceM = duration * SOUND_SPEED/2;

  float myFloat = distanceM; // The float to be converted

  constexpr size_t BUFFER_SIZE = 7;
  char myByteBuffer[BUFFER_SIZE]; 
  dtostrf(myFloat, BUFFER_SIZE - 1 /*width, including the decimal dot and minus sign*/, 2 /*precision*/, myByteBuffer);
  mqttClient.publish("sensor/distance", 1, true, myByteBuffer);
  delay(1000);
  //Serial.println(pubid);
}
