# app.py
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from pptx import Presentation
from io import BytesIO

app = Flask(__name__)
CORS(app)

@app.route('/api/convert', methods=['POST'])
def convert_pdf_to_pptx():
    try:
        pdf_file = request.files['pdf']
        pdf_path = 'uploaded_file.pdf'
        pdf_file.save(pdf_path)

        # Simplified logic to test PowerPoint conversion
        presentation = Presentation()
        slide = presentation.slides.add_slide(presentation.slide_layouts[0])
        title = slide.shapes.title
        title.text = "Hello, this is a test slide!"

        pptx_output = BytesIO()
        presentation.save(pptx_output)
        pptx_output.seek(0)

        return send_file(pptx_output, as_attachment=True, download_name='output.pptx')

    except Exception as e:
        error_message = str(e)
        app.logger.error(f"Error during conversion: {error_message}")
        response_data = {
            'success': False,
            'error': error_message,
        }
        return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
