<?php
$curl=curl_init();

curl_setopt_array($curl, array(
	CURLOPT_RETURNTRANSFER => 1,
	CURLOPT_URL => 'http://localhost:8080'
));

$result=curl_exec($curl);
echo $result;

echo "<h1>hello Zsolt</h1>";?>
