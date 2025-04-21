from flask import Flask, request, jsonify
from gpt_notes import get_layering_recs, get_analysis_json

app = Flask(__name__)

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    perfumes = data.get('perfumes', [])
    # (You may need to save or pass these into get_layering_recs if it's not dynamic)
    result = get_layering_recs(perfumes)  # or however you're handling input
    return jsonify({ "recommendations": result })

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    perfumes = data.get('perfumes', [])
    result = get_analysis_json(perfumes)  # you'd implement this
    return jsonify({ "analysis": result })
