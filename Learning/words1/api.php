<?php 

	class Api extends Rest {
		
		public function __construct() {
			parent::__construct();
		}

		public function generateToken() {
			$email = $this->validateParameter('email', $this->param['email'], STRING);
			$pass = $this->validateParameter('pass', $this->param['pass'], STRING);
			try {
				$stmt = $this->dbConn->prepare("SELECT * FROM users WHERE email = :email AND password = :pass");
				$stmt->bindParam(":email", $email);
				$stmt->bindParam(":pass", $pass);
				$stmt->execute();
				$user = $stmt->fetch(PDO::FETCH_ASSOC);
				if(!is_array($user)) {
					$this->returnResponse(INVALID_USER_PASS, "Email or Password is incorrect.");
				}

				if( $user['active'] == 0 ) {
					$this->returnResponse(USER_NOT_ACTIVE, "User is not activated. Please contact to admin.");
				}

				$paylod = [
					'iat' => time(),
					'iss' => 'localhost',
					'exp' => time() + (15*60),
					'userId' => $user['id']
				];

				$token = JWT::encode($paylod, SECRETE_KEY);
				
				$data = ['token' => $token];
				$this->returnResponse(SUCCESS_RESPONSE, $data);
			} catch (Exception $e) {
				$this->throwError(JWT_PROCESSING_ERROR, $e->getMessage());
			}
		}

		public function addWord() {
			$pos1 = $this->validateParameter('pos1', $this->param['pos1'], STRING, false);
			$word = $this->validateParameter('word', $this->param['word'], STRING, false);
			$sentence = $this->validateParameter('sentence', $this->param['sentence'], STRING, false);
			$meaning = $this->validateParameter('meaning', $this->param['meaning'], STRING, false);

			$word_obj = new Word;
			$word_obj->setPos($pos1);
			$word_obj->setWord($word);
			$word_obj->setSentence($sentence);
			$word_obj->setMeaning($meaning);
			$word_obj->setCreatedBy($this->userId);
			$word_obj->setCreatedOn(date('Y-m-d'));

			if(!$word_obj->insert()) {
				$message = 'Failed to insert.';
			} else {
				$message = "Inserted successfully.";
			}

			$this->returnResponse(SUCCESS_RESPONSE, $message);
		}

		public function getWordDetails() {
			$wordId = $this->validateParameter('wordId', $this->param['wordId'], INTEGER);

			$word_obj = new Word;
			$word_obj->setId($wordId);
			$word = $word_obj->getWordDetailsById();
			if(!is_array($word)) {
				$this->returnResponse(SUCCESS_RESPONSE, ['message' => 'Word details not found.']);
			}

			$response['wordId'] 		= $word['id'];
			$response['wordName'] 		= $word['pos1'];
			$response['word'] 			= $word['word'];
			$response['meaning'] 		= $word['meaning'];
			$response['sentence'] 		= $word['sentence'];
			$response['createdBy'] 		= $word['created_user'];
			$response['lastUpdatedBy'] 	= $word['updated_user'];
			$this->returnResponse(SUCCESS_RESPONSE, $response);
		}
		
		public function getWordDetails1() {
			$wordName = $this->validateParameter('wordName', $this->param['wordName'], STRING);

			$word_obj = new Word;
			$word_obj->setWord($wordName);
			$word = $word_obj->getWordDetailsByWord();
			if(!is_array($word)) {
				$this->returnResponse(SUCCESS_RESPONSE, ['message' => 'Word details not found.']);
			}

			$response['wordId'] 		= $word['id'];
			$response['wordName'] 		= $word['pos1'];
			$response['word'] 			= $word['word'];
			$response['meaning'] 		= $word['meaning'];
			$response['sentence'] 		= $word['sentence'];
			$response['createdBy'] 		= $word['created_user'];
			$response['lastUpdatedBy'] 	= $word['updated_user'];
			$this->returnResponse(SUCCESS_RESPONSE, $response);
		}
		
		
		public function getAllWordDetails() {
			$wordId = $this->validateParameter('wordName', $this->param['wordName'], STRING);

			$word_obj = new Word;
			$word = $word_obj->getAllWords();
			if(!is_array($word)) {
				$this->returnResponse(SUCCESS_RESPONSE, ['message' => 'Word details not found.']);
			}

			$this->returnResponse(SUCCESS_RESPONSE, $word);
		}
		
		
		
		

		public function updateWord() {
			$wordId = $this->validateParameter('wordId', $this->param['wordId'], INTEGER);
			$pos1 = $this->validateParameter('pos1', $this->param['pos1'], STRING, false);
			$sentence = $this->validateParameter('sentence', $this->param['sentence'], STRING, false);
			$meaning = $this->validateParameter('meaning', $this->param['meaning'], STRING, false);

			$word_obj = new Word;
			$word_obj->setId($wordId);
			$word_obj->setPos($pos1);
			$word_obj->setSentence($sentence);
			$word_obj->setMeaning($meaning);
			$word_obj->setUpdatedBy($this->userId);
			$word_obj->setUpdatedOn(date('Y-m-d'));

			if(!$word_obj->update()) {
				$message = 'Failed to update.';
			} else {
				$message = "Updated successfully.";
			}

			$this->returnResponse(SUCCESS_RESPONSE, $message);
		}

		public function deleteWord() {
			$wordId = $this->validateParameter('wordId', $this->param['wordId'], INTEGER);

			$word_obj = new Word;
			$word_obj->setId($wordId);

			if(!$word_obj->delete()) {
				$message = 'Failed to delete.';
			} else {
				$message = "deleted successfully.";
			}

			$this->returnResponse(SUCCESS_RESPONSE, $message);
		}
	}
	
 ?>