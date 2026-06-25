from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def calculator():
    try:
        
        a = request.args.get("a")
        b = request.args.get("b")
        op = request.args.get("op", "add")  
        if a is None or b is None:
            return jsonify({
                "error": "Please provide both a and b"
            }), 400

    
        a = float(a)
        b = float(b)

        
        if op == "add":
            result = a + b
        elif op == "sub":
            result = a - b
        elif op == "mul":
            result = a * b
        elif op == "div":
            if b == 0:
                return jsonify({
                    "error": "Division by zero is not allowed"
                }), 400
            result = a / b
        else:
            return jsonify({
                "error": "Invalid operation. Use add, sub, mul, div"
            }), 400

    
        return jsonify({
            "a": a,
            "b": b,
            "operation": op,
            "result": result
        })

    except ValueError:
        return jsonify({
            "error": "Invalid input. a and b must be numbers"
        }), 400


if __name__ == "__main__":
    app.run(debug=True)
