// script.js
document.addEventListener('DOMContentLoaded', () => {
    const pdfInput = document.getElementById('pdfInput');
    const convertButton = document.getElementById('convertButton');
    const downloadLink = document.getElementById('downloadLink');

    convertButton.addEventListener('click', async () => {
        const file = pdfInput.files[0];
        if (file) {
            const formData = new FormData();
            formData.append('pdf', file);

            try {
                const response = await fetch('http://127.0.0.1:5000/api/convert', {
                    method: 'POST',
                    body: formData,
                });

                if (response.ok) {
                    const data = await response.json();
                    if (data.success) {
                        downloadLink.href = data.pptxFile;
                        downloadLink.style.display = 'block';
                    } else {
                        console.error('PPT conversion failed:', data.error);
                    }
                } else {
                    console.error('Server returned an error:', response.status);
                }
            } catch (error) {
                console.error('Error:', error);
            }
        }
    });
});
