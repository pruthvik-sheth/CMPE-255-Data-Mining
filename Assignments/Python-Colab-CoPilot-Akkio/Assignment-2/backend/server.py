from flask import Flask, request, send_file
from flask_cors import CORS
import qrcode
from io import BytesIO

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json
    contact_info = f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(contact_info)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer, 'PNG')
    buffer.seek(0)
    
    return send_file(buffer, mimetype='image/png', as_attachment=True, download_name='contact_qr.png')

if __name__ == '__main__':
    app.run(debug=True)