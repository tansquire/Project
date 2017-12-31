 
<?php
 if($_GET['button1']){fun1();}
 if($_GET['button2']){fun2();}
 
 function fun1()
 {
   //This function will update some column in database to 1
echo"openning";

//as per user information give different alert message

echo '<script language="javascript">';
echo 'alert("message successfully sent")';
echo '</script>';

 }
 function fun2()
 {
   //This function will update some column in database to 2

echo"closing";
 }
?>
 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title></title>
  </head>
  <body>
    <button id="btnfun1" name="btnfun1" onClick='location.href="?button1=1"'>OPEN</button>

    <button id="btnfun2" name="btnfun2" onClick='location.href="?button2=1"'>CLOSE</button>



  </body>
</html>
