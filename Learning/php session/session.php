<?php
 include('Config.php');

   session_start();
   
   $user_check = $_SESSION['login_user'];
   
   




  // $ses_sql = mysqli_query($db,"select username from Login where username = '$user_check' ");
   
  // $row = mysqli_fetch_array($ses_sql,MYSQLI_ASSOC);
   
   //$login_session = $row['username'];


        $sql1 = "SELECT * FROM Login WHERE username='$user_check'";

	$result = $conn->query($sql1);
	$row = mysqli_fetch_assoc($result);
        $login_session = $row['username'];





   
   if(!isset($_SESSION['login_user'])){
     // header("location:Login.php");
      echo "<script language='javascript' type='text/javascript'> location.href='welcome.php' </script>";  


   }
?>
