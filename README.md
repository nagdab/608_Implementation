# 608_Implementation
Implementation of the 608 Response Code, in collaboration with S²ERC at Georgetown University and the Federal Communications Commission.

The implementation consists of two parts: (1) The Python-based analytics engine, and (2) the Kamailio server.


                        +-----------+
                        |           |
                        | Analytics |
                        |  Engine   |
                        +-----------+
                           ^     | (HTTP)
                           |     v
                        +-----------+
     +-----+    608     |  Called   |           +-----+
     | UAC | <--------- |  Party    |           | UAS |
     +-----+            |  Proxy    |           +-----+
                        +-----------+

       

## The Analytics Engine ##
The analytics engine is modeled after a possible intermediary that assess the nature of the call to determine its validity. The engine communicates with the Kamailio proxy server via HTTP. 

To spin up the server, switch into the `analytics-engine` directory:  
`cd analytics-engine`

Point the `FLASK-APP` environment variable to `app.py`:  
`export FLASK_APP=app.py`

Run the flask app via:  
`flask run`

The server should indicate that it is running:  
`Running on http://127.0.0.1:5000/`

## The Kamailio Server ##
The Kamailio server is v5.2. To spin up the server, download and install Kamailio v5.2 here:  
http://kamailio.org/docs/tutorials/5.2.x/kamailio-install-guide-git/

The `http-client` module is not usually installed, so compile the `http-client` module and copy it over to the executibles bin for kamailio modules.

Change the `init` file to point to the `n_608.cfg` configuration file that specifies the correct configuration for our server.

Finally, update the `http_client_query` function on line 738 of the `n_608.cfg` configuration file to update the new domain for the analytics engine server (make it point to your domain instead, but keep the variables passed into the url):  
`http_client_query("https://$YOUR_DOMAIN_URL$/identity=var(identity)&info=var(info)&alg=var(alg)&date=var(date)&from=fu&to=tu&callid=$ci", "$var(result)");`

## Testing ##
Spin up your kamailio server via kamctl or kamailio commands, and run the flask app. Note also that there are a number of global variables in the flask application that allow you to specify whether the analytics-engine sees the call as secure (with or without STIR certification), and valid (analytics engine detecting fraudulent callers). If you have connected caller and callee agents, you will notice a 608 Response Code passed back, and depending on the flask app configuration, the response may contain the Call-Info Header.
