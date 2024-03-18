# Keylogger in python (using pyhook)
<br>

## Idea and Objective :thought_balloon: 

The idea behind this project was to delve into the realm of keyloggers while striving for dynamic functionality. Key strokes sent by the client via sockets are analyzed on the server to extract sensitive data such as email addresses, passwords, IBAN numbers, and more. This exploration aims to understand the mechanisms of keylogging and how they can potentially compromise security, while also providing insights into defensive measures against such threats.
<br><br>

## Overview  :writing_hand:

This project is divided into a client and a server component. Naturally, the keylogger resides on the client side to capture keystrokes, which are then sent to the server for analysis. Let's delve into the functionalities of each component:

- **Client**: The client side consists of the main file responsible for capturing data and sending it to the remote server via sockets. Additionally, it includes text files to enhance the code's understanding of user inputted words, along with the pyhook package for hooking into the system's keyboard events.
  
- **Server**: On the server side, there are text files to translate all key combinations into understandable phrases. The server script is responsible for receiving data from the client, while the analysis script is tasked with parsing and extracting sensitive information from the captured keystrokes by the keylogger.
<br>

## How to Use :hammer:

To effectively use the keylogger, follow these steps:

:gear: Begin by cloning the repository onto your device using Git or by downloading it directly from the repository's page.

:gear: Navigate to the directory where you cloned the repository and execute the main.py file on the client side. This file is responsible for initializing the keylogger and sending captured keystrokes to the designated server.

:gear: Similarly, navigate to the directory where you want to run the server component. Then, execute the server.py file. This script sets up the server to receive keystroke data from the client and perform analysis on it.
<br><br>

## Disclaimer :no_entry: 

This keylogger project has been developed solely for **educational purposes and ethical learning**. The intention is to understand how keyloggers work and to explore methods for defending against such threats.

**:x: I do not condone or support the use of this software for any malicious or illegal activities :x:**

Any usage of this keylogger for unauthorized monitoring of computer systems or data interception is strictly prohibited and may be illegal in many jurisdictions. The creator of this project takes no responsibility for any misuse of the software.

Additionally, it's worth noting that the pyhook package, used for hooking into keyboard events, may be flagged as a threat by certain antivirus software or operating systems, especially if not compiled into an executable form. Users are advised to exercise caution and use this software responsibly and within legal boundaries.
