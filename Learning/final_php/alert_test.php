<?php
   include('session.php');
   if(!isset($_SESSION['login_user']))
$x=1;
else
$x=0;
$a="hello";
$b="hi hello";
FUNCTION hello(){
 GLOBAL $a;
 GLOBAL $b;
 GLOBAL $check;
 if($check==1)
 echo $a;
 else
 echo $b;
 
}
FUNCTION func(){
 GLOBAL $check;
 echo $check;

}
 
?>
<html>
   
   <head>
      <title>Welcome </title>
<script>
function echoHello(){
 alert("<?PHP hello(); ?>");
 }
</script>
   </head>
   
   <body>
      
<h1>value of check is <?php func(); ?></h1>
<h2><a href = "Logout.php">Sign Out</a></h2>
<button onclick="echoHello()">Say Hello</button>
   </body>
   
</html>


 


