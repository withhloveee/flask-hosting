from flask import Flask, render_template, request
import os
from statistics import mean, median, multimode

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        numbers_str = request.form.get("numbers", "")

        try:
            # Split input into floats
            nums = [float(n.strip()) for n in numbers_str.split(",") if n.strip()]

            if not nums:
                error = "Please enter at least one number."
            else:
                result = {
                    "mean": mean(nums),
                    "median": median(nums),
                    "mode": multimode(nums)  # handles multiple modes
                }
        except:
            error = "Invalid input. Please enter comma-separated numbers."

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
