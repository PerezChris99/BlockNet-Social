from flask import Blueprint, render_template, request, jsonify
from .defi_contract import DeFiContract

main = Blueprint('main', __name__)

# Initialize the DeFiContract with appropriate canister ID and URL
defi = DeFiContract(canister_id="your_canister_id", url="https://ic0.app")

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/lend', methods=['POST'])
def lend():
    params = request.json
    result = defi.call_method("lend", params)
    return jsonify(result)

@main.route('/borrow', methods=['POST'])
def borrow():
    params = request.json
    result = defi.call_method("borrow", params)
    return jsonify(result)

@main.route('/stake', methods=['POST'])
def stake():
    params = request.json
    result = defi.call_method("stake", params)
    return jsonify(result)

@main.route('/dex', methods=['POST'])
def dex():
    params = request.json
    result = defi.call_method("dex", params)
    return jsonify(result)

@main.route('/analytics', methods=['GET'])
def analytics():
    data = defi.call_method("getAnalytics", {})
    return jsonify(data)
