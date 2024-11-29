from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForCausalLM

app = Flask(__name__)

# Load model and tokenizer
model_name = "Jedalc/codeparrot-gp2-finetune"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

@app.route("/")
def index():
    return render_template("index.html")  # This serves the HTML file

@app.route("/generate_code", methods=["POST"])
def generate_code():
    data = request.json
    prompt = data.get("prompt", "")

    # Generate the code completion
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
    generated_code = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Clean up the response (optional)
    cleaned_code = "\n".join(
        line for line in generated_code.splitlines() if not line.startswith("#")
    )

    return jsonify({"generated_code": cleaned_code})

if __name__ == "__main__":
    app.run(debug=True)
