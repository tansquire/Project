<?php
include('Config.php');


$sql = "UPDATE command SET remote='1' WHERE valve=1";

$conn->query($sql);
  
        
?>
