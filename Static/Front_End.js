async function sendMessage() {
    // Get the user input from the textarea
    const input = document.getElementById("input").value;
    const responseDiv = document.getElementById("response");

    // Clear the response area while waiting for a new response
    responseDiv.innerHTML = "<p>Loading...</p>";

    try {
        // Send the POST request to the Flask backend
        const response = await fetch("/generate_code", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt: input }),
        });

        // Parse the JSON response
        const data = await response.json();

        // Display the generated response
        responseDiv.innerHTML = `<p style="white-space: pre-wrap;">${data.generated_code}</p>`;
    } catch (error) {
        // Handle any errors and display a message
        responseDiv.innerHTML = `<p style="color: red;">Error: Unable to fetch response. Please try again.</p>`;
        console.error("Error:", error);
    }
}

