document.getElementById('generate-report-button').addEventListener('click', async () => {
    const carteira = document.getElementById('carteira').value;
    const response = await fetch(`/generate_report?carteira=${carteira}`);
    const data = await response.json();
    
    const logElement = document.getElementById('log');
    if (data.html_data) {
        logElement.innerHTML = data.html_data;
    } else {
        logElement.textContent = data.error;
    }
});