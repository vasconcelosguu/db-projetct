document.getElementById('generate-report-button').addEventListener('click', generateReport);

function generateReport() {
    const carteira = document.getElementById('carteira').value;
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;

    const url = `/generate_report?carteira=${carteira}&start_date=${startDate}&end_date=${endDate}`;
    
    fetch(url)
        .then(response => {
            if (response.ok) {
                const filename = response.headers.get('Content-Disposition').split('filename=')[1];
                return response.blob().then(blob => ({ blob, filename }));
            } else {
                throw new Error('Erro ao gerar o relatório');
            }
        })
        .then(({ blob, filename }) => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = filename || 'report.csv';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            const log = document.getElementById('log');
            log.textContent = 'Relatório gerado com sucesso!';
        })
        .catch(error => {
            const log = document.getElementById('log');
            log.textContent = `Erro: ${error.message}`;
        });
}