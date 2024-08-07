from flask import Flask, request, send_file, render_template, Response
import pandas as pd
from io import BytesIO
from datetime import datetime
from scripts.data_generator import generate_mailing

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_report')
def generate_report():
    carteira = request.args.get('carteira')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    data = generate_mailing(carteira, start_date, end_date)
    df = pd.DataFrame(data)
    
    output = BytesIO()
    df.to_csv(output, index=False, encoding='utf-8-sig')
    output.seek(0)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'report_{carteira}_{timestamp}.csv'
    
    return Response(
        output.getvalue(),
        mimetype='text/csv',
        headers={"Content-Disposition": f"attachment;filename={filename}"}
    )

if __name__ == '__main__':
    app.run(debug=True)
