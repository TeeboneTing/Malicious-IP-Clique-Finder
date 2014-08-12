#!/usr/bin/env python
# -*- coding: utf-8 -*-

#project: AI agent
#file name: ai_utils.py
#description: Submitting disease vector domain automatically
#             This is an utility tool module file
#author: Teebone Ding (RD-TW-INTRN)
#location and created date: 2011/07 @ Trend Micro, Taipei

import socket
import urllib2
import json
#import simplejson as json
import time
import random
import httplib
import re

class GetMethods:
    def getIPCliques(self,domain):
        try:
            ip =  socket.gethostbyname(domain)  #convert domain name to ip addr
        except:
            print 'convert domain to IP error, return original domain.'
            return [domain]
        clique_url = 'http://10.48.36.10:8016/thor/ipclique/' + ip
        while True:
            try:
                page = json.loads(urllib2.urlopen(clique_url).read())
                break
            except:
                print 'GsMethod init error, try again!'
                time.sleep(random.random())
        list = []
        for obj in page['domains']:
            list.append(str(obj))
        print domain + ' IP cliques: ' + str(list)
        return list

        
class GsMethods:
    def __init__(self,domain):
        self.url = 'http://ec2-50-18-91-111.us-west-1.compute.amazonaws.com/whowas/' + domain
        while True:
            try:
                self.page = json.loads(urllib2.urlopen(self.url).read())
                break
            except:
                print 'GsMethod init error, try again!'
                time.sleep(random.random())

    def gs_createdate(self):
        try:
            print 'created on: ' + self.page["created_on"]
            return self.page["created_on"].split()[0]
        except:
            print 'no creation date!'
            return ''
        
    def gs_expiredate(self):
        try:
            print 'expires on: ' + self.page["expires_on"]
            return self.page["expires_on"].split()[0]
        except:
            print 'no expire date!'
            return ''
        
    def gs_nss(self):
        list = []
        try:
            for obj in self.page["nameservers"]:
                list.append(str(obj))
        except:
            print 'no nameserver data... return empty list'
            return []
        print 'name servers: ' + str(list)
        return list
        
    def gs_re(self,re_str):
        ret = 0
        try:
            raw = self.page["raw"]
        except:
            print 'no raw data... return zero.'
            return ret
        result = re.search(re_str, raw)
        print 'search result:'+ str(result)
        if not result:
            print 'regular expression not found... return 0'
        else:
            print 'regular expression found!!! return 1'
            ret = 1
        return ret
class GsRating:
    def __init__(self,domain):
        self.url = 'http://10.48.36.10:8016/thor/rating/' + domain
        while True:
            try:
                self.page = json.loads(urllib2.urlopen(self.url).read())
                break
            except:
                print 'GsRating init error, try again!'
                time.sleep(random.random())
                
    def gs_rating(self):
        print 'rating value: ' + str(self.page[0]["ratingValue"][0]) +'('+ self.page[0]["ratingString"][0] +')'
        return self.page[0]["ratingValue"][0]
        
        
class GsAlexa:
    def gs_alexa(self,domain):
        url = 'http://teebirdland.appspot.com/alexa/' + domain
        print 'Getting alexa.com data...'
        while True:
            try:
                get = urllib2.urlopen(url).read()
                break
            except:
                print 'GsAlexa init error, try again!'
                time.sleep(random.random())
        
        try:
            page = json.loads(get)[0]
            print page
            return page
        except:
            print 'json load error!!! Return empty dictionary.'
            print get
            return {}
        

class AutoSub:
    def AutoSubmit(self,domains,user_mail,pwd,reason):
        list = domains.split(',')
        data_to_be_sent = { \
            "sender":str(user_mail), \
            "receiver":"spntw@urlsgalore.atr.trendmicro.com", \
            "source_id":1112, \
            "password":str(pwd), \
            "reason":str(reason), \
            "patterns": list \
        }
        
        print 'data to be sent:' + json.dumps(data_to_be_sent)
        while True:
            try:
                h = httplib.HTTPConnection('10.48.36.73:8016')
                headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
                h.request('POST', '/thor/submitter/', json.dumps(data_to_be_sent), headers)
                r = h.getresponse()
                break
            except:
                print 'Auto Submit connection fail, try again now...'
                time.sleep(random.random())
        res = r.read()
        print 'response result:' + res
        if res == '{}':
            print 'Auto Submit Success!'
        else:
            print 'Auto Submit Fail, the response: ' + res