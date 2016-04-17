int ir[4] = {0,0,0,0};

void setup() {
  // put your setup code here, to run once:
  pinMode(7, INPUT);
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(10, INPUT);
  Serial.begin(9600);
}

void loop() {
  int ir[4] = {0,0,0,0};
  int j = 7;
  for(int i=0;i<4;i++) {
    ir[i] = digitalRead(j++);
  }
  String s = "";
  if (!ir[0])
    s.concat("1");
  if (!ir[1])
    s.concat("2");
  if (!ir[2])
    s.concat("3");
  if (!ir[3])
    s.concat("4");
  
  if (s.length() == 0)
    Serial.println("0");
  else
    Serial.println(s);
  delay(1000);
}
