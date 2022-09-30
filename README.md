# L293DMotorDriver
12V power was given to Shild with DC Power Supply.
The AFMotors library was used to control the motors.
Since 2 engines were used, a new variable named engine2 was created and the 2nd engine was sent there.
FORWARD/BACKWARD gives information about which direction the motor will turn.
In order for the 2 engines to work sequentially with each other, their times were adjusted with the delay() function.
In our project, the first engine started working for 3 seconds and after a 2 second break, the second engine started to start again.
Then we want the 1st engine to run again.
That's why the delay() function is adjusted for this loop
