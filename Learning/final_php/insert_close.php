<?php
include('Config.php');


$sql = "UPDATE command SET close='1' WHERE valve=1";

$conn->query($sql);
  
        
?>
