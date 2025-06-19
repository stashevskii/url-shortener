function copyBtn() {
    const shortUrl = document.getElementById("short-url").textContent;
    navigator.clipboard.writeText(shortUrl).then(
        function() {
            const originalText = this.textContent;
            this.textContent = "Copied!";
            setTimeout(() => {this.textContent = originalText;}, 1500);
        }.bind(this)
    );
}

document.getElementById("copy-btn").addEventListener("click", copyBtn);