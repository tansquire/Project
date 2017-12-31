<?php
 
 if($_GET['button2']){fun2();}
 
 function fun1()
 {
   //This function will update some column in database to 1
echo"openning";



 }
 function fun2()
 {
   //This function will update some column in database to 2



include("insert.php");
include("alert.php");


 }
?>
 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title></title>
  </head>
  <body>
    

<button id="btnfun2" name="btnfun2" onClick='location.href="?button2=1"'>CLOSE</button>






<button onclick="myFunction()">Try it</button>

<script>
function myFunction() {
alert("Hello! I am an alert box!");

}
</script>












  </body>
</html>
