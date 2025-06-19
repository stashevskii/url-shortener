async function trackUrl() {
    const alias = document.getElementById("input-url").value;

    if (!alias) {
        alert("Please enter a URL to shorten");
        return;
    }

    try {
        const response = await fetch(`${config.serverUrl}${config.apiEndpoints.track}/${alias}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        });

        if (response.status == 404) {
            alert("This alias does not exists!");
            return;
        } else if (!response.ok) {
            alert("Error!");
            return;
        }

        const data = await response.json();
        console.log("Server data:", data);

        document.getElementById("total-clicks").textContent = data.clicks;
        document.getElementById("original-url").textContent = data.url;
        document.getElementById("result-container").style.display = "block";
    } catch (error) {
        alert("Error: " + error.message);
        console.error("Fetch error:", error);
    }
}

document.getElementById("track-btn").addEventListener("click", trackUrl);