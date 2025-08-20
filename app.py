from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# مسار الـ API
@app.route("/api/i3rab", methods=["POST"])
def i3rab():
    data = request.json  # استلام النص من الفرونت
    text = data.get("text", "")

    # هنا هنستخدم خدمة SinaTools المجانية كمثال
    response = requests.get(f"https://sina.tools/api/i3rab?text={text}")

    if response.status_code == 200:
        result = response.json()  # النتيجة JSON
        return jsonify(result)
    else:
        return jsonify({"error": "فشل في جلب الإعراب"}), 500


if __name__ == "__main__":
    app.run(debug=True)
