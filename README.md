# Testing a network connection

With this program you can determine if you have the right ethernet cable between two hosts.

## Getting started

1. If necessary: use a crossover cable adapter
2. Change the IP settings of the two hosts to IP addresses in the following subnet `10.0.0.0/24`
3. On one computer start the shell-script `listener.sh`
4. On the other computer start the Python script with the following command `./pSender.py "Put your message here"`

If there is no connection between the two hosts, the program will do a new attempt for sending the packet.

Use Control+C to quit.
