<?php

include('session.php');
if(!isset($_SESSION['login_user']))
$x=1;
else
$x=0;


 if($_GET['button1']){fun1();}
 if($_GET['button2']){fun2();}
 
 
 function fun1()
 {
 GLOBAL $check;
GLOBAL $remote_status;
GLOBAL $opened_status;
if($check==1)
{
if($remote_status==0)
include("local_alert.php");
elseif($opened_status==1)
include("already_open.php");
else





{
include("insert_open.php");
include("open_alert.php");
}
}
else
include("bad_alert.php");

}

 function fun2()
 {
GLOBAL $check;
GLOBAL $remote_status;
GLOBAL $closed_status;
if($check==1)
{
if($remote_status==0)
include("local_alert.php");
elseif($closed_status==1)
include("already_close.php");
else


{
include("insert_close.php");
include("close_alert.php");
}
}
else
include("bad_alert.php");

}



function remote()
{
GLOBAL $remote_status;
if($remote_status==1)
echo "REMOTE";
else
echo "LOCAL";
}


function open()
{
GLOBAL $opened_status;
if($opened_status==1)
echo "OPENED";
else
echo "CLOSED";
}


?>


<!DOCTYPE html>

<html>

<head>


<script type="text/javascript" src="http://ajax.googleapis.com/ajax/
libs/jquery/1.3.0/jquery.min.js"></script>


<script type="text/javascript">
var auto_refresh = setInterval(
function ()
{
$('#area1').load('ready3.php').fadeIn("slow");
}, 100); // refresh every 100 milliseconds
</script>


<script type="text/javascript">
var auto_refresh = setInterval(
function ()
{
$('#time').load('currenttime.php').fadeIn("slow");
}, 100); // refresh every 100 milliseconds
</script>

<script type="text/javascript">
var auto_refresh = setInterval(
function ()
{
$('#open1').load('open2.php').fadeIn("slow");
}, 100); // refresh every 100 milliseconds
</script>

<script type="text/javascript">
var auto_refresh = setInterval(
function ()
{
$('#remote1').load('remote1.php').fadeIn("slow");
}, 100); // refresh every 100 milliseconds
</script>

<script type="text/javascript">
var auto_refresh = setInterval(
function ()
{
$('#picture').load('valve.php').fadeIn("slow");
}, 100); // refresh every 100 milliseconds
</script>








</head>
<body>


<table border=1 width=100%>
  <tr>
    <td colspan="1" width=10% height=100px style="background-color:#3B170B"><img src="iitm.png" style=width:100%;height:120%;"></td>
    <td colspan="4"><table border=1 width=100%> <tr><td colspan="4" height=60px align="middle" style="background-color:#F6CEE3;font-size: 250%">IIT Madras water network control system</td></tr> <tr><td colspan="3" height=50px width=40% align="middle" style="background-color:#F5D0A9;font-size: 150%"> <div id="time">  </td>
    <td colspan="1" align="middle" width=10% style="background-color:#F2F5A9;font-size: 150%"> <a href = "Logout.php">Sign Out</a></td> </tr> </table></td>
  </tr>
  <tr>
        <td height=300px align="middle" style="background-color:#848484;font-size: 150%">Level sensor reading</td> 
	<td><table width=100% border=1> <tr><td height=270px align="middle" style="background-color:#848484"> <div id="area1"> </div> </div></td></tr> <tr><td align="middle" style="background-color:#848484">RR sump</td></tr> </table></td>  
	<td><table width=100% border=1> <tr><td height=270px align="middle" style="background-color:#848484;font-size: 150%">sensor2</td></tr> <tr><td align="middle" style="background-color:#848484">Children Park(L&T)</td></tr> </table></td>
	<td><table width=100% border=1> <tr><td height=270px align="middle" style="background-color:#848484;font-size: 150%">sensor3</td></tr> <tr><td align="middle" style="background-color:#848484">Stuff club</td></tr> </table></td>
	<td><table width=100% border=1> <tr><td height=270px align="middle" style="background-color:#848484;font-size: 150%"> sensor4 </td></tr> <tr><td align="middle" style="background-color:#848484">Lake well</td></tr> </table></td>
	
  </tr>
  

<tr>
	<td height=250x align="middle" style="background-color:#848484;font-size: 150%">Actuator control</td> 
	
	<td colspan="2"><table border=1 width=100%><tr><td colspan="2" height=200px align="middle"><div id="picture"></td></tr>  <tr><td align="middle" style="background-color:#848484"> <div id="open1"></td> <td align="middle" style="background-color:#848484"><div id="remote1"></td></tr> <tr><td colspan="1" align="middle" height=50px style="background-color:#848484" > <button id="btnfun1" name="btnfun1" style="background-color:#868A08;color:black; height: 35px; width: 90px;font-size: 150%;" onClick='location.href="?button1=1"'>OPEN</button> </td> <td colspan="1" align="middle" style="background-color:#848484"><button id="btnfun2" name="btnfun2" style="background-color:#868A08;color:black; height: 35px; width: 90px;font-size: 150%;"onClick='location.href="?button2=1"'>CLOSE</button> </td></tr></table></td>
	<td colspan="2" align="middle" style="background-color:#848484;font-size: 150%">Actuator2 control</td>
</tr>


<tr>
	<td colspan="5" align="middle" style="background-color:#81F7D8;font-size: 150%">Copyright@process control LAB, IIT Madras</td>
</tr>
</table>
</body>
</html>
