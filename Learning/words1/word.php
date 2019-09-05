<?php 
	class Word {
		private $id;
		private $pos1;
		private $word;
		private $sentence;
		private $meaning;
		private $updatedBy;
		private $updatedOn;
		private $createdBy;
		private $createdOn;
		private $tableName = 'wordlist';
		private $dbConn;

		function setId($id) { $this->id = $id; }
		function getId() { return $this->id; }
		function setPos($pos1) { $this->pos1 = $pos1; }
		function getPos() { return $this->pos1; }
		function setWord($word) { $this->word = $word; }
		function getWord() { return $this->word; }
		function setSentence($sentence) { $this->sentence = $sentence; }
		function getSentence() { return $this->sentence; }
		function setMeaning($meaning) { $this->meaning = $meaning; }
		function getMeaning() { return $this->meaning; }
		function setUpdatedBy($updatedBy) { $this->updatedBy = $updatedBy; }
		function getUpdatedBy() { return $this->updatedBy; }
		function setUpdatedOn($updatedOn) { $this->updatedOn = $updatedOn; }
		function getUpdatedOn() { return $this->updatedOn; }
		function setCreatedBy($createdBy) { $this->createdBy = $createdBy; }
		function getCreatedBy() { return $this->createdBy; }
		function setCreatedOn($createdOn) { $this->createdOn = $createdOn; }
		function getCreatedOn() { return $this->createdOn; }

		public function __construct() {
			$db = new DbConnect();
			$this->dbConn = $db->connect();
		}

		public function getAllWords() {
			$stmt = $this->dbConn->prepare("SELECT * FROM " . $this->tableName);
			$stmt->execute();
			$words = $stmt->fetchAll(PDO::FETCH_ASSOC);
			return $words;
		}

		public function getWordDetailsById() {

			$sql = "SELECT 
						w.*, 
						u.name as created_user,
						u1.name as updated_user
					FROM wordlist w 
						JOIN users u ON (w.created_by = u.id) 
						LEFT JOIN users u1 ON (w.updated_by = u1.id) 
					WHERE 
						w.id = :wordId";

			$stmt = $this->dbConn->prepare($sql);
			$stmt->bindParam(':wordId', $this->id);
			$stmt->execute();
			$word = $stmt->fetch(PDO::FETCH_ASSOC);
			return $word;
		}
		
		
		public function getWordDetailsByWord() {

			$sql = "SELECT 
						w.*, 
						u.name as created_user,
						u1.name as updated_user
					FROM wordlist w 
						JOIN users u ON (w.created_by = u.id) 
						LEFT JOIN users u1 ON (w.updated_by = u1.id) 
					WHERE 
						w.word = :wordName";

			$stmt = $this->dbConn->prepare($sql);
			$stmt->bindParam(':wordName', $this->word);
			$stmt->execute();
			$word = $stmt->fetch(PDO::FETCH_ASSOC);
			return $word;
		}
		
		
		

		public function insert() {
			
			$sql = 'INSERT INTO ' . $this->tableName . '(id, pos1, word, sentence, meaning, created_by, created_on) VALUES(null, :pos1, :word, :sentence, :meaning, :createdBy, :createdOn)';

			$stmt = $this->dbConn->prepare($sql);
			$stmt->bindParam(':pos1', $this->pos1);
			$stmt->bindParam(':word', $this->word);
			$stmt->bindParam(':sentence', $this->sentence);
			$stmt->bindParam(':meaning', $this->meaning);
			$stmt->bindParam(':createdBy', $this->createdBy);
			$stmt->bindParam(':createdOn', $this->createdOn);
			
			if($stmt->execute()) {
				return true;
			} else {
				return false;
			}
		}

		public function update() {
			
			$sql = "UPDATE $this->tableName SET";
			if( null != $this->getPos()) {
				$sql .=	" pos1 = '" . $this->getPos() . "',";
			}

			if( null != $this->getSentence()) {
				$sql .=	" sentence = '" . $this->getSentence() . "',";
			}

			if( null != $this->getMeaning()) {
				$sql .=	" meaning = '" . $this->getMeaning() . "',";
			}

			$sql .=	" updated_by = :updatedBy, 
					  updated_on = :updatedOn
					WHERE 
						id = :userId";

			$stmt = $this->dbConn->prepare($sql);
			$stmt->bindParam(':userId', $this->id);
			$stmt->bindParam(':updatedBy', $this->updatedBy);
			$stmt->bindParam(':updatedOn', $this->updatedOn);
			if($stmt->execute()) {
				return true;
			} else {
				return false;
			}
		}

		public function delete() {
			$stmt = $this->dbConn->prepare('DELETE FROM ' . $this->tableName . ' WHERE id = :userId');
			$stmt->bindParam(':userId', $this->id);
			
			if($stmt->execute()) {
				return true;
			} else {
				return false;
			}
		}
	}
 ?>