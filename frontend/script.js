function runAgent() {
    const appId = document.getElementById("appId").value;
    const log = document.getElementById("log");

    if (!appId) {
        alert("Please enter App ID");
        return;
    }

    log.innerHTML = "";
    addLog("🤖 Agent initialized");
    addLog("📡 Sending request to backend...");

    fetch("http://127.0.0.1:5000/run-agent", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ app_id: appId })
    })
    .then(res => res.json())
    .then(data => {
        addLog("🔵 Reviews fetched");
        addLog("🟢 Issues extracted");
        addLog("🟣 Topics consolidated");
        addLog("🟠 Trend report generated");
        addLog("✅ DONE! Check output/trend.csv");

        addLog("");
        addLog("📊 Reviews: " + data.reviews_fetched);
        addLog("📌 Issues: " + data.issues_found);
    })
    .catch(err => {
        addLog("❌ Error running agent");
        console.error(err);
    });
}

function addLog(message) {
    const log = document.getElementById("log");
    log.innerHTML += message + "<br>";
}

