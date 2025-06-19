async function shortUrl() {
    let originalUrl = document.getElementById("input-url").value

    if (!originalUrl) {
        alert("Please enter a URL to shorten");
        return;
    }

    if (!originalUrl.startsWith("https://")) {
        originalUrl = `${"https://"}${originalUrl}`
    }

    try {
        const response = await fetch(
            `${config.serverUrl}${config.apiEndpoints.shorten}?url=${encodeURIComponent(originalUrl)}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            }
        });

        if (!response.ok) {
            alert("Error!");
            return;
        }

        const data = await response.json();
        document.getElementById("short-url").textContent = `${config.serverUrl}/${data.alias}`;
        document.getElementById("result-container").style.display = "block";
    } catch (error) {
        alert("Error: " + error.message);
        console.error("Fetch error:", error);
    }
}

document.getElementById("shorten-btn").addEventListener("click", shortUrl);