from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    mean_value = None

    if request.method == "POST":
        numbers_str = request.form.get("numbers", "")
        
        try:
            # Convert comma-separated input into a list of floats
            nums = [float(n.strip()) for n in numbers_str.split(",") if n.strip()]
            
            if nums:
                mean_value = sum(nums) / len(nums)
        except:
            mean_value = "Invalid input. Please enter numbers separated by commas."

    return render_template("index.html", mean_value=mean_value)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
