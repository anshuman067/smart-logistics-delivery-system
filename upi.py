from flask import Flask, render_template, request, jsonify
import razorpay
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
db = SQLAlchemy(app)

# Razorpay credentials
RAZORPAY_KEY_ID = "rzp_test_WXRNMLHZxsiQwu"
RAZORPAY_KEY_SECRET = "YZQYJnA9KdWObC0zz4ImSYYy"
razorpay_client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_id = db.Column(db.String(100), unique=True, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/create_order', methods=['POST'])
def create_order():
    data = request.json
    amount = int(data['amount']) * 100  # Convert to paise

    order = razorpay_client.order.create({
        'amount': amount,
        'currency': 'INR',
        'payment_capture': '1'  # Auto capture payment
    })

    new_payment = Payment(payment_id=order['id'], amount=data['amount'], status='Pending')
    db.session.add(new_payment)
    db.session.commit()

    return jsonify(order)


@app.route('/payment_success', methods=['POST'])
def payment_success():
    data = request.json
    payment_id = data['razorpay_payment_id']
    order_id = data['razorpay_order_id']

    payment = Payment.query.filter_by(payment_id=order_id).first()
    if payment:
        payment.status = 'Success'
        db.session.commit()

    return jsonify({'status': 'success'})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
