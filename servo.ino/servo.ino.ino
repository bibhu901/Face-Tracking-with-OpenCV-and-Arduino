

#include<Servo.h>

Servo x, y;
int width = 640, height = 480;  // total resolution of the video
int xpos = 90, ypos = 90;  // initial positions of both Servos
void setup() {

  Serial.begin(9600);
  x.attach(9);
  y.attach(10);
  x.write(xpos);
  y.write(ypos);
}
const int angle = 1;   // degree of increment or decrement

void loop() {
  if (Serial.available() > 0)
  {
    int x_mid, y_mid;
    if (Serial.read() == 'X')
    {
      x_mid = Serial.parseInt();  // x-coordinate of center of the face
      if (Serial.read() == 'Y')
        y_mid = Serial.parseInt(); //y-coordinate of center of the face
    }
    /* Move the servos if face is outside the allowed region
    */
    if (x_mid > width / 2 + 30)
      xpos -= angle;
    if (x_mid < width / 2 - 30)
      xpos += angle;
    if (y_mid < height / 2 + 30)
      ypos -= angle;
    if (y_mid > height / 2 - 30)
      ypos += angle;


    // if the servo angle is outside its range
    if (xpos >= 180)
      xpos = 180;
    else if (xpos <= 0)
      xpos = 0;
    if (ypos >= 180)
      ypos = 180;
    else if (ypos <= 0)
      ypos = 0;

    x.write(xpos);
    y.write(ypos);


  }
}
