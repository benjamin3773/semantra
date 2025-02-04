function submitQuery() {
    const query = document.getElementById("query").value;
    const saveLocation = document.getElementById("save_location").value;
    const port = document.getElementById("port").value || "8080"; // Default to 8080
    const resultMessage = document.getElementById("resultMessage");

    fetch("/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: new URLSearchParams({
            query: query,
            save_location: saveLocation,
            port: port
        })
    })
    .then(response => response.json())
    .then(data => {
        resultMessage.innerText = data.message;
        resultMessage.style.color = data.status === "success" ? "green" : "red";
    })
    .catch(error => {
        resultMessage.innerText = "❌ Failed to send request.";
        resultMessage.style.color = "red";
    });
}

