<?php
// Sample authentication check
if ($_POST['email'] == 'atharvmittal2004@gmail.com' && $_POST['password'] == '12345') {
    header('Location: index.html');
    exit();
} else {
    echo "Invalid credentials!";
}
?>
