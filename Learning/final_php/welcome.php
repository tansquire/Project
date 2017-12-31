<?php
   include('session.php');
   if(!isset($_SESSION['login_user']))
$x=1;
else
$x=0;

?>
<html">
   
   <head>
      <title>Welcome </title>
   </head>
   
   <body>

      <h1>Welcome <?php echo $login_session; ?></h1> 
      <h2><a href = "Logout.php">Sign Out</a></h2>
      <h3>Welcome <?php echo $x; ?></h3> 
   </body>
   
</html>
