document.getElementById("detect-button").addEventListener("click", async () => {
    const description = document.getElementById("description").value;
    const resultElement = document.getElementById("result");
    resultElement.textContent = "Detecting...";

    try {
        const response = await fetch("/detect", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ description }),
        });

        const data = await response.json();
        resultElement.textContent = `Detected Fruit: ${data.fruit}`;
    } catch (error) {
        console.error("Error detecting fruit:", error);
        resultElement.textContent = "An error occurred. Please try again.";
    }
});
