This is the readme file for:
AI agent for Submitting disease vector domain automatically
Author: Teebone Ding (RD-TW-INTRN)
Date: 2011 Jul/Aug

Description:
There are three python programs,
          one web server framework,
          a web page template and
          jQuery library
          in this project.

PROGRAMS:
ai_utils.py  : all the utilitiy functions are put here
main.py      : the main program is here
warp.py      : web service framework

WEB SERVER FRAMEWORK:
bottle.py    : bottle web framework. for more information please see http://bottlepy.org/docs/dev/

WEB PAGE TEMPLATE:
AutoSub.tpl  : render the web service for us to browse results by a web browser

jQuery library:
I put this in /static folder.

User Instructions:

This instruction tells you how to go on a web server for AI agent.
1. Open "warp.py" and go to the last line in this file, you'll see the run() funtion.
2. Change the host to your own computer ip and change port number as you want.
3. Open command line and execute warp.py, the web server will go on.
4. Open a web browser and put http://YOUR_IP:port/ on the URL line, you get AI agent now!

RESTful interface: We also provide a RESTful interface for user to communicate with our project by json format.
1. Follow the above web server instructions
2. Use POST method to put data to http://YOUR_IP:port/rest
3. the json string data format example is shown below:
{
"onClique":0,
"onAlexa":1,
"onAutoSubmit":0,
"whois_age":365,
"whois_reg_period":1,
"re":"key1 | key2",
"alexa_global":5000,
"alexa_region":500,
"alexa_rep":1000,
"user":"user_account",
"pwd":"GodBlessTrendMicro",
"reason":"These sites are malicious sites.",
"domains":["www.google.com","www.yahoo.com"]
}
4. Be careful that if you won't use alexa, re, or auto submission,
   leave those key("alexa_global","alexa_region","alexa_rep","re",
   "user","pwd","reason") to be empty string, don't miss them.
   
If you can see Core-Tech Backend Wiki, please go to 
http://coretech-backend-dev.tw.trendnet.org/mediawiki/index.php/Restful_Interface#AI_Agent_for_Auto_Submission


Thanks. :)
Teebone Ding 2011.08.16
