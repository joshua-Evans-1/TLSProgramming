# Project 3: TLS Programming 
Joshua Evans 

[Overview & Implementation](/report/report.md)

## TLS-Enabled TCP Echo Server & Client:

### Running the Server
Open a Terminal or Command Prompt.

Navigate to the server directory:

```bash
cd path/to/TLSEchoServer
```
Run the Server Script:
```bash
python SimpleTLSServer.py 
```
Keep this terminal open. The server will now listen for incoming messages.


### Running the Client
Open a New Terminal or Command Prompt.

Run the Client Script to Send Message:
```bash
openssl s_client -connect localhost:12000
```
Once connected, you can type messages and receive capitalized responses from the server.

---

## Secure File Transfer Application:

### Running the Server
Open a Terminal or Command Prompt.

Navigate to the server directory:

```bash
cd path/to/NetFileXfer/server
```
Run the Server Script:
```bash
python NetFileXferServer.py <PORT>
```
Keep this terminal open. The server will now listen for incoming file transfers.


### Running the Client
Open a New Terminal or Command Prompt.

Navigate to the NetFileXfer directory:
```bash
cd path/to/NetFileXfer
```
Run the Client Script to Transfer test.txt:
```bash
python NetFileXferClient.py  <SERVER_IP> <SERVER_PORT> test.txt
```
This command will upload test.txt to the server.

Similarly, to transfer mountain-lake.jpg:
```bash
python NetFileXferClient.py  <SERVER_IP> <SERVER_PORT> mountain-lake.jpg
```
This command will upload mountain-lake.jpg to the server.

---


