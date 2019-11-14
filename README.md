# Benjamin
A python game with samurai for an arcade machine that runs from a Pi

![alt text](https://imgur.com/AvAnN7K.png "Smauri Idle")
![alt text](https://imgur.com/ltCpefb.png "Smauri Walk")
![alt text](https://imgur.com/JfrkUbl.png "Wall Grab")

## Hardware IO
![alt text](https://imgur.com/xb21sH7.png "Pi Diagram")

The Hardware IO was setup with 6 switches, four for each direction on the joystick, and two for each button.  When a button or joystick was pushed an interrupt is triggered, the interrupt then updates a relative boolean value inside the playerInput class.  The game then grabs these values during each frame and uses them as player input.  The circuit diagram can be seen in figure n, GPIO pins 4, 17, 27, 22, 5, and 6 were used for the inputs for up, left, right, down, button one, and button 2 respectively.  These pins were set up for input.  The GPIO pins 12 and 16 were setup for output for the lights on button one and two.  The two lights needed 5 volts to light up but the GPIO pins could only output 3 volts.  Because of this we used a transistor to be able to control a 5 volt source going into the lights.  

## Level Generation
![alt text](https://imgur.com/3RfnMe1.png "Example Level")
![alt text](https://imgur.com/7DJZ3X0.png "Brick Texture")
![alt text](https://imgur.com/QptDDPn.png "Example Level")

In order to have the ability to make custom levels quickly, a text parser was developed. By giving the program an array of 22-character strings, a level could be generated quickly. The program loops through each string and adds the appropriate block to the world depending on what letter is present in the string. A ‘W’ will result in a regular wall, and a ‘V’ will create a block which can be slid under. The ‘S’ indicates the starting point of the player, while the ‘O’ is the location of the skull. Any other characters are parsed as a blank area, however spaces make the most sense visually. 
