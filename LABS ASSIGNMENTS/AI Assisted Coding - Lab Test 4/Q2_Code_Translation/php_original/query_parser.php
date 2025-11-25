<?php
$conn = new mysqli("localhost", "root", "charansai1234@", "testdb");

$result = $conn->query("SELECT id, name FROM users");
$data = array();

while($row = $result->fetch_assoc()) {
    $data[] = $row;
}

print_r($data);
?>
