# BESTIoTTradfri
Python code to controll the IKEA Tradfri light exhibited at the Computer Corner of HTL Kaindorf at the BEST 2022.

## Installation
Install this reposotory to get the running code. Depending on your network you may have to reset the IP of the Tradfri gateway. The security code should work for our device.

## Start the server
To start the server navigate into the *server* directory and execute the following:
```
sudo uvicorn main:app --host 0.0.0.0 --port 80
```

## API
To controll the light send a request to the following URL:
```
http://IP:80/switch/<on/off>
```

## GUI
To acces the GUI navigate to:
```
http://IP:80/items/<random_number_of_your_liking>
```