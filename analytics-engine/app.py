import os
import sys
import random
from flask import Flask

date_valid = True
certificate_valid = True
certificate = 'CERTIFICATE'
identity_valid = True
call_valid = True


app = Flask(__name__)

@app.route('/identity=<identity>&info=<info>&alg=<alg>&date=<date>&from=<from_header>&to=<to_header>&callid=<call_id>')
def auth_engine(identity, info, alg, date, from_header, to_header, call_id):
  
    def check_date(date):
        return date_valid
        
    def get_certificate(cert_link):
        if certificate_valid:
            return certificate
        else:
            return None
        
    # we verify identity auth with certificate: stubbed out
    def check_identity(identity, certificate):
        return identity_valid
        
    def analytics_engine(from_header, to_header, call_id):
        return call_valid

    
    print('\n\n-------------\nNEW CALL:')
    print('FROM: '+ from_header)
    print('TO: ' + to_header)
    print('CALL ID: ' + call_id)

    cert_link = info
    
    if not check_date(date):
        print('RESULT: BAD_DATE')
        return 'BAD_DATE'
        
    cert = get_certificate(cert_link)
    if not cert:
        print('RESULT: BAD_CERT_LINK')
        return 'BAD_CERT_LINK'
    
    if not check_identity(identity, cert):
        print('RESULT: BAD_IDENTITY')
        return 'BAD_IDENTITY'
    
    if not analytics_engine(from_header, to_header, call_id):
        print('RESULT: BAD_ANALYTICS_VERIFIED_IDENTITY')
        return 'BAD_ANALYTICS_VERIFIED_IDENTITY'
        
    print('RESULT: GOOD')
    return 'GOOD'



app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))