<!DOCTYPE html>
<html>
<body>
<meta http-equiv="refresh" content = "2" />
<?php
$myfile = fopen("/home/dadu/file.txt", "r") or die("Unable to open file!");
echo fread($myfile,filesize("/home/dadu/file.txt"));
fclose($myfile);
?>

</body>
</html>
