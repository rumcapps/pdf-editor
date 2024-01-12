# app.py
from flask import Flask, request, jsonify
from pdf_text_extractor import extract_text_from_pdf

app = Flask(__name__)

@app.route('/api/convert', methods=['POST'])
def convert_pdf_to_pptx():
    try:
        pdf_file = request.files['pdf']
        pdf_path = 'uploaded_file.pdf'
        pdf_file.save(pdf_path)
        extracted_text = extract_text_from_pdf(pdf_path)

        # Placeholder response, modify as needed
        response_data = {
            'success': True,
            'pptxFile': 'path/to/your/generated.pptx',
        }

        return jsonify(response_data)

    except Exception as e:
        error_message = str(e)
        response_data = {
            'success': False,
            'error': error_message,
        }
        return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
