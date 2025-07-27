# Import libraries
from flask import Flask, request, response, jsonify, url_for, render_template, redirect
# Instantiate Flask functionality
app = Flask(__name__)
# Sample data
transaction = [
    {'id' : 1, 'date': '2025-07-25', 'amount' : 100}
    {'id' : 2, 'date' : '2025-07-26', 'amount' : 200}
    {'id' : 3, 'date' : '2025-07-27', 'amount' : 300}
    {'id' : 4, 'date' : '2025-07-28', 'amount' : 400}
    {'id' : 5, 'date' : '2025-07-29', 'amount' : 500}
]


# Read operation
# This function containing the render_template function will list all transactions once the user hits the base URL
@app.route("/")
def get_transactions():
    return render_template('transactions.html', transactions=transactions)
    

# Create operation
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == "POST"
        # Create new transaction values using the field values
        transaction = {
                  'id': len(transactions)+1
                  'date': request.form['date']
                  'amount': float(request.form['amount'])
                 }
        # Append the created transaction to the list of existing ones
        transactions = append(transaction)

        # Redirect to the transaction list page after adding the new transaction
        return redirect(url_for("get_transactions"))
        # If the return method is GET, we render the form template to display the add transaction form page
    return render_template("form.html")




# Update operation

# Delete operation

# Run the Flask app