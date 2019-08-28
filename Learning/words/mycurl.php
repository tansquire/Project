<?php 
	$curl = curl_init();
	$request = '{
					"name":"generateToken",
					"param":{
						"email":"user1@gmail.com",
						"pass":"pass123"
					}
				}';
	curl_setopt($curl, CURLOPT_URL, 'http://localhost/words/');
	curl_setopt($curl, CURLOPT_POST, true);
	curl_setopt($curl, CURLOPT_HTTPHEADER, ['content-type: application/json']);
	curl_setopt($curl, CURLOPT_POSTFIELDS, $request);
	curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);

	$result = curl_exec($curl);
	$err = curl_error($curl);
	if($err) {
		echo 'Curl Error: ' . $err;
	} else {
		// header('content-type: application/json');
		$response = json_decode($result, true);
		$token = $response['resonse']['result']['token'];
		curl_close($curl);

		/*call another API*/
		$curl = curl_init();
		$request = '{
						"name":"getWordDetails",
						"param":{
							"wordId":6
						}
					}';
			curl_setopt_array($curl, array(
			  CURLOPT_URL => "http://localhost/words/",
			  CURLOPT_RETURNTRANSFER => true,
			  CURLOPT_ENCODING => "",
			  CURLOPT_MAXREDIRS => 10,
			  CURLOPT_TIMEOUT => 30,
			  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
			  CURLOPT_CUSTOMREQUEST => "POST",
			  CURLOPT_POSTFIELDS => $request,
			  CURLOPT_HTTPHEADER => array(
				    "authorization: Bearer $token",
				    "content-type: application/json",
				  ),
			));

			$response = curl_exec($curl);
			$err = curl_error($curl);

			if ($err) {
			  echo "cURL Error #:" . $err;
			} else {
			  echo $response;
			}
			curl_close($curl);
		}
 ?>