# 608_Implementation
Implementation of the 608 Response Code, in collaboration with S²ERC at Georgetown University and the Federal Communications Commission.

The implementation consists of two parts: (1) The Python-based analytics engine, and (2) the Kamailio server.

<![CDATA[
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

       ]]>

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

