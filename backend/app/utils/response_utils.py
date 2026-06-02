"""Response utility helpers."""

from flask import jsonify

def success_response(message, data=None, success_code=200):
    return jsonify({
        "success": True,
        "message": message,
        "data": data
    }), success_code

def error_response(message,error_code=400):
    return jsonify({
        "success": False,
        "message": message
    }), error_code
