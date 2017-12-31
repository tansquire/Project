<!DOCTYPE html>
<html>
<body>
<meta http-equiv="refresh" content = "2" />
<?php
$myfile = fopen("http:/10.22.52.214/hi.txt", "r") or die("Unable to open file");
echo fread($myfile,filesize("/home/dadu/pyserial-2.7/php.txt"));
fclose($myfile);
?>

</body>
</html>







