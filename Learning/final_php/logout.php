<?php
   session_start();
   
   if(session_destroy()) {
     // header("Location: Login.php");


echo "<script language='javascript' type='text/javascript'> location.href='Login1.php' </script>"; 
   }
?>
