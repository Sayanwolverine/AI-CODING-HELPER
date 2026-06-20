async function sendCode() {
    const code = document.getElementById("code").value;
    const language = document.getElementById("language").value;

    const res = await fetch("http://127.0.0.1:5000/fix", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ code, language })
    });

    const data = await res.json();
    document.getElementById("output").innerText = data.result;
}