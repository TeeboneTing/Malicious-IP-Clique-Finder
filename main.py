#!/usr/bin/env python
# -*- coding: utf-8 -*-

#project: AI agent
#file name: main.py
#description: Submitting disease vector domain automatically
#             This is the main routine that execute the AI agent
#author: Teebone Ding (RD-TW-INTRN)
#location and created date: 2011/07 @ Trend Micro, Taipei

import sys
import json
#import simplejson as json
import cStringIO
import time
import random
import string
from datetime import date
from datetime import timedelta
from ai_utils import GsRating
from ai_utils import GetMethods
from ai_utils import GsMethods
from ai_utils import GsAlexa
from ai_utils import AutoSub

def reqPara(args, key, type):
    for arg in args:
        kv = arg.split("=")
        if kv[0] == key:
            if not kv[1]:
                return None
            if type == "float":
                return string.atof(kv[1])
            elif type == "int":
                return string.atoi(kv[1])
            else:
                return kv[1]               
    return ""



class MainRoutine:
    def __init__(self):
        self.onClique = reqPara(sys.argv,"onClique","int")
        self.onAlexa = reqPara(sys.argv,"onAlexa","int")
        self.onAutoSubmit = reqPara(sys.argv,"onAutoSubmit","int")
        self.whois_age = reqPara(sys.argv,"whois_age","int")
        self.whois_register_period = reqPara(sys.argv,"whois_reg","int")
        self.alexa_global = reqPara(sys.argv,"alexa_glo","int")
        self.alexa_region = reqPara(sys.argv,"alexa_reg","int")
        self.alexa_rep = reqPara(sys.argv,"alexa_rep","int")

        line = sys.stdin.readline().split('\t')
        self.whois_keyword = reqPara(line,"whois_key","str")
        self.nt_usermail = reqPara(line,"user","str")
        self.nt_password = reqPara(line,"pwd","str")
        self.reason = reqPara(line,"reason","str")
        if self.whois_keyword.endswith("\n"):
            self.whois_keyword = self.whois_keyword[:-1]
    def main(self):
        domains = []
        out = cStringIO.StringIO()
        excp = cStringIO.StringIO()
        nosbmt = cStringIO.StringIO()
        for line in sys.stdin:
            sys.stdout.flush()
            if line == '\n' or not line:
                break
            else:
                if line.startswith('http://'):
                    line = line[7:]
                if line.endswith("/*"):
                    line = line[:-2]
                    
                time.sleep(random.random())
                if not self.onClique:
                    domains = [ line.split()[0] ] #one element list
                else:
                    domains = GetMethods().getIPCliques(line.split()[0])
                    
                for domain in domains:
                    if not domain:
                        break
                    else:
                        print 'processing... '+ domain
                        time.sleep(random.random())
                        rating = GsRating(domain).gs_rating()
                        if rating not in [90,91,89,37]:
                            nosbmt.write(domain + ',')
                            continue
                        else:
                            get = GsMethods(domain)
                            c_date_list = get.gs_createdate().split('-')
                            e_date_list = get.gs_expiredate().split('-')
                            if not (c_date_list[0] and e_date_list[0]):
                                #print out exception
                                print domain + ' sent to exception list' 
                                excp.write(domain + ',')
                                continue
                            createdate = date(int(c_date_list[0]),int(c_date_list[1]),int(c_date_list[2]))
                            expiredate = date(int(e_date_list[0]),int(e_date_list[1]),int(e_date_list[2]))
                            #nss = get.gs_nss() #No use now. Might use this in the future.
                            today = date.today()
                            if not((today-createdate) < timedelta(days=(self.whois_age)) and \
                                (expiredate-createdate) < timedelta(days=(self.whois_register_period*365))):
                                nosbmt.write(domain + ',')
                                continue
                            else:
                                if self.whois_keyword: #if regular expression not empty,check it!
                                    ret = get.gs_re(self.whois_keyword)
                                    if ret:
                                        print domain + ' sent to submission list'
                                        out.write(domain + ',')
                                        continue
                                
                                if self.onAlexa:
                                    alexa = GsAlexa().gs_alexa(domain) # this is a dictionary
                                    if not alexa:
                                        #NO DATA
                                        continue
                                    elif alexa['global'] == -1 or alexa['region'] == -1 or alexa['reputation'] == -1:
                                        print 'Lack of Alexa data, domain ' + domain + ' send to exception list.'
                                        excp.write(domain + ',')
                                        continue
                                    elif alexa['global'] > self.alexa_global or \
                                        alexa['region'] > self.alexa_region or alexa['reputation'] < self.alexa_rep: 
                                        print domain + ' sent to submission list'
                                        out.write(domain + ',')
                                    else:
                                        nosbmt.write(domain + ',')
                                        continue
                                else:
                                    print domain + ' sent to submission list'
                                    out.write(domain + ',')

        print 'Process Over.'
        if self.onAutoSubmit:
            AutoSub().AutoSubmit(out.getvalue()[:-1],self.nt_usermail,self.nt_password,self.reason)
            print 'Submitted list:'
        else:
            print 'To be submit list:'
        print out.getvalue().split(',')[:-1]
        print 'exception (no whowas data) list:'
        print excp.getvalue().split(',')[:-1]
        print 'Non-submitted list:' 
        print nosbmt.getvalue().split(',')[:-1]
        return None

        
M = MainRoutine()
M.main()