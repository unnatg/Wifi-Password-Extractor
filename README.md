# Wifi-Password-Extractor
A simple python script to extract the password and other relevant information of the wireless networks stored on your PC/laptop
If you enter 'netsh int tcp show profiles' in cmd, you will get all the wireless user profiles.
From the wireless profiles, you can find the password of a profile by typing 'netsh int tcp show profile <profile name> key=clear' in cmd.
You will get the details of the network as well as the password.
This only works on the networks which you have connected to.
