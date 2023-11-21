                                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                ┃  Project 3: TLS Programming  ┃
                                ┃    Joshua Evans JO9038RL     ┃
                                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ TLS-Enabled TCP Echo Server & Client: ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Running the Server ┃                                                                     ┃
┣━━━━━━━━━━━━━━━━━━━━┛                                                                     ┃
┃ Open a Terminal or Command Prompt.                                                       ┃
┃                                                                                          ┃
┃ Navigate to the server directory:                                                        ┃
┃     cd path/to/TLSEchoServer                                                             ┃
┃                                                                                          ┃
┃ Run the Server Script:                                                                   ┃
┃     python SimpleTLSServer.py                                                            ┃
┃                                                                                          ┃
┃ Keep this terminal open. The server will now listen for incoming messages.               ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Running the Client ┃                                                                     ┃
┣━━━━━━━━━━━━━━━━━━━━┛                                                                     ┃
┃ Open a New Terminal or Command Prompt.                                                   ┃
┃                                                                                          ┃
┃ Run the Client Script to Send Message:                                                   ┃
┃     openssl s_client -connect localhost:12000                                            ┃
┃                                                                                          ┃
┃ Once connected, you can type messages and receive capitalized                            ┃
┃ responses from the server.                                                               ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Secure File Transfer Application: ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Running the Server ┃                                                                     ┃
┣━━━━━━━━━━━━━━━━━━━━┛                                                                     ┃
┃ Open a Terminal or Command Prompt.                                                       ┃
┃                                                                                          ┃
┃ Navigate to the server directory:                                                        ┃
┃     cd path/to/NetFileXfer/server                                                        ┃
┃                                                                                          ┃
┃ Run the Server Script:                                                                   ┃
┃     python NetFileXferServer.py <PORT>                                                   ┃
┃                                                                                          ┃
┃ Keep this terminal open. The server will now listen for incoming file transfers.         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Running the Client ┃                                                                     ┃
┣━━━━━━━━━━━━━━━━━━━━┛                                                                     ┃
┃ Open a New Terminal or Command Prompt.                                                   ┃
┃                                                                                          ┃
┃ Navigate to the NetFileXfer directory:                                                   ┃
┃     cd path/to/NetFileXfer                                                               ┃
┃                                                                                          ┃
┃ Run the Client Script to Transfer test.txt:                                              ┃
┃     python NetFileXferClient.py  <SERVER_IP> <SERVER_PORT> test.txt                      ┃
┃                                                                                          ┃
┃ This command will upload test.txt to the server.                                         ┃
┃                                                                                          ┃
┃ Similarly, to transfer mountain-lake.jpg:                                                ┃
┃     python NetFileXferClient.py  <SERVER_IP> <SERVER_PORT> mountain-lake.jpg             ┃
┃                                                                                          ┃
┃ This command will upload mountain-lake.jpg to the server.                                ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
