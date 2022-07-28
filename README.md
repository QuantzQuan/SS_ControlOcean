# SS_ControlOcean
Socket&amp;Serial to control BDS boat

## Main Code

* PC_CTRL: use keyboard to send different Socket command to Raspberry

* Zero_SS_Control: recieve command from PC and send to Arduino by Serial

## Test Code

* Keyboard_pynput_test: use pynput to listen keyboard(**Cautions!! It is slow and occupy many resource of PC**)
* Keyboard_test: listen keyboard faster
* Serial_test: use virtual COM to test(**Software: Configure Virtual Serial Port Driver**)
* socket_Tx: test socket tx
* stream: test video stream
