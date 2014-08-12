<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>AI Agent</title>
<script type="text/javascript" src="static/jquery-1.6.2.min.js"></script>
</head>
<body>
<form id="send_domain" action="/sub" method="post" enctype="multipart/form-data">
<table width="100%" border="0">
  <tr>
    <td width="58%" height="492"><p>Domains:
      </p>
      <p>
        <textarea name="domains" id="domains" cols="80" rows="25" placeholder="put domains here..."></textarea>
    </p></td>
    <td width="42%"><p>
    <input type="checkbox" name="onClique" id="onClique" />
    onClique
    </p>
      <table width="99%" height="398" border="1">
      <tr>
        <td><p>
        WHOIS_AGE &lt; (days)
          <input type="text" name="WHOIS_AGE" id="WHOIS_AGE" />
        <br />
         WHOIS_REGISTER_PERIOD &lt; (years)
            
            <select name="Whois_Register_Period" id="Whois_Register_Period">
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
            </select>
        <br />
        RE 
        <input type="text" name="re" id="re" />
        </p></td>
      </tr>
      <tr>
        <td><p>Alexa:</p>
          <p><input type="checkbox" name="onAlexa" id="onAlexa" />
          onAlexa<br />
          ALEXA_GLOBAL  
          <input name="alexa_global" type="text" id="alexa_global" size="4" />
          <br />
          ALEXA_REGION  
          <input name="alexa_region" type="text" id="alexa_region" size="4" />
          <br />
          ALEXA_REP 
          <input name="alexa_rep" type="text" id="alexa_rep" size="4" />
      </p></td>
      </tr>
      <tr>
        <td><p>AutoSubmit:</p>
        <p>
          <input type="checkbox" name="onAutoSubmit" id="onAutoSubmit" />
        onAutoSubmit<br />
        NT_Account 
        <input name="NTuser_email" type="text" id="NTuser_email" size="40" />
        <br />
        NT_Password 
        <input  type="password" id="NTuser_password" name="NTuser_password" size="40" />
        <br />
        Reason<br />
          <textarea  id="reason" name="reason" cols="45" rows="5" placeholder="please fill in one line reson in English..."></textarea>
        </p></td>
      </tr>
  </table></td>
  </tr>
  <tr>
    <td><input type="submit" value="Submit" /></td>
    <td>&nbsp;</td>
  </tr>
</table>
<p>&nbsp;</p>
</form>

<script type="text/javascript">
    
    $('#send_domain').submit(function() {
        if(!$('#WHOIS_AGE').val()){
            alert("Please fill in WHOIS_AGE!");
            return false;
        }
        if(!$('#domains').val()){
            alert("Please fill in domains!");
            return false;
        }
        
        if($('input[id="onAlexa"]:checked').val() == 'on'){
            if(!$('#alexa_global').val()){
                alert("Please fill in ALEXA_GLOBAL!");
                return false;
                }
            if(!$('#alexa_region').val()){
                alert("Please fill in ALEXA_REGION!");
                return false;
                }
            if(!$('#alexa_rep').val()){
                alert("Please fill in ALEXA_REP!");
                return false;
                } 
        }
        
        if($('input[id="onAutoSubmit"]:checked').val() == 'on'){
            if(!$('#NTuser_email').val()){
                alert("Please fill in NT_Account!");
                return false;
                }
            if(!$('#NTuser_password').val()){
                alert("Please fill in NT_password!");
                return false;
                }
            if(!$('#reason').val()){
                alert("Please fill in a reson for auto submission!!");
                return false;
                } 
        }
    });
     
     </script>
</body>
</html>