<?php
// Enable error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the input data
    $name = isset($_POST['name']) ? $_POST['name'] : '';
    $email = isset($_POST['email']) ? $_POST['email'] : '';
    $message = isset($_POST['message']) ? $_POST['message'] : '';

    // Prepare the content for the email
    $to = "atharvmittal2004@gmail.com"; // Your email address
    $subject = "New Contact Form Submission";
    $body = "Name: $name\nEmail: $email\nMessage: $message\n";
    $headers = "From: $email\r\n"; // Set the sender's email

    // Send the email
    if (mail($to, $subject, $body, $headers)) {
        // Email sent successfully
        // Return a success response (you can customize this if needed)
        echo json_encode(['success' => true]);
    } else {
        // Email sending failed
        echo json_encode(['success' => false]);
    }
} else {
    // If accessed directly, return an error
    http_response_code(405);
}
?>
