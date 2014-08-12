#!/usr/bin/env python
# -*- coding: utf-8 -*-

#project: AI agent
#file name: index.py
#description: Submitting disease vector domain automatically
#             bottle framework here, warp the AI agent to a web service
#author: Teebone Ding (RD-TW-INTRN)
#location and created date: 2011/07 @ Trend Micro, Taipei

import bottle
from bottle import route,run,template,request,response,static_file
import os
import sys
bottle.debug(True)
import subprocess
import json

@route('/')
def default():
    return template('AutoSub')

@route('/rest',method='POST')
def put_rest():
    bottle.response.headers['Content-Type'] = 'text/plain'
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'
    bottle.response.headers['Access-Control-Allow-Methods'] = 'GET'
    
    data = request.body.read()
    if not data:
        bottle.abort(400, 'No data received')
    
    entity = json.loads(data)
    
    try:
        domains = entity['domains']
        onClique = str(entity['onClique'])
        WHOIS_AGE = str(entity['whois_age'])
        Whois_Register_Period = str(entity['whois_reg_period'])
        re = entity['re']
        onAlexa = str(entity['onAlexa'])
        alexa_global = str(entity['alexa_global'])
        alexa_region = str(entity['alexa_region'])
        alexa_rep = str(entity['alexa_rep'])
        onAutoSubmit = str(entity['onAutoSubmit'])
        NTuser_email = entity['user']
        NTuser_password = entity['pwd']
        reason = entity['reason']
    except:
        bottle.abort(400, 'Some key might missing!')
        
    dothis = 'main.py onClique='+onClique+' onAlexa='+onAlexa+' onAutoSubmit='+onAutoSubmit+' whois_age='+WHOIS_AGE+ \
    ' whois_reg='+Whois_Register_Period+' alexa_glo='+alexa_global+' alexa_reg='+alexa_region+' alexa_rep='+alexa_rep
    
    long_str = 'user='+NTuser_email+'\tpwd='+NTuser_password+'\treason='+reason+'\twhois_key='+re+'\n'
    print str(domains)+'\n'
    print dothis
    print long_str
    
    stdin, stdout = os.popen2(dothis)
    stdin.write(long_str)
    for do in domains:
        yield do
        stdin.write(do)
        if do[-1:] != '\n':
            yield '\n'
            stdin.write('\n')
    stdin.close()
    while 1:
        stdout.flush()
        line = stdout.readline()
        if line == "": break
        print line,
        yield line
    
@route('/sub', method='POST')
def open_main():
    bottle.response.headers['Content-Type'] = 'text/plain'
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'
    bottle.response.headers['Access-Control-Allow-Methods'] = 'GET'
    
    domains = request.forms.get('domains')
    onClique = request.forms.get('onClique')
    WHOIS_AGE = request.forms.get('WHOIS_AGE')
    Whois_Register_Period = request.forms.get('Whois_Register_Period')
    re = request.forms.get('re')
    onAlexa = request.forms.get('onAlexa')
    alexa_global = request.forms.get('alexa_global')
    alexa_region = request.forms.get('alexa_region')
    alexa_rep = request.forms.get('alexa_rep')
    onAutoSubmit = request.forms.get('onAutoSubmit')
    NTuser_email = request.forms.get('NTuser_email')
    NTuser_password = request.forms.get('NTuser_password')
    reason = request.forms.get('reason')
    if onClique == "on":
        onClique = str(1)
    else:
        onClique = str(0)
    if onAlexa == "on":
        onAlexa = str(1)
    else:
        onAlexa = str(0)
    if onAutoSubmit == "on":
        onAutoSubmit = str(1)
    else:
        onAutoSubmit = str(0)
    
    dothis = 'main.py onClique='+onClique+' onAlexa='+onAlexa+' onAutoSubmit='+onAutoSubmit+' whois_age='+WHOIS_AGE+ \
    ' whois_reg='+Whois_Register_Period+' alexa_glo='+alexa_global+' alexa_reg='+alexa_region+' alexa_rep='+alexa_rep
    
    long_str = 'user='+NTuser_email+'\tpwd='+NTuser_password+'\treason='+reason+'\twhois_key='+re+'\n'
    print domains
    yield domains
    print dothis
    print long_str
    stdin, stdout = os.popen2(dothis)
    stdin.write(long_str)
    stdin.write(domains)
    stdin.close()
    while 1:
        stdout.flush()
        line = stdout.readline()
        if line == "": break
        print line,
        yield line

@route('/static/:filename')
def get_file(filename):
    return static_file(filename, root='./static/')

if __name__ == "__main__":
    run(host='10.1.112.146',port=8080) 