from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        initial_amount = float(request.form['initial_amount'])
        cagr = float(request.form['cagr'])
        period = float(request.form['period'])
        period_type = request.form['period_type']

        # Convert the period to years if it's in months
        if period_type == 'months':
            period = period / 12

        # Calculate the final value
        final_value = initial_amount * ((1 + cagr/100) ** period)
        result = f"The final value of the investment is: {final_value:.2f}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
