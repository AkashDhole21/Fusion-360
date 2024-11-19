from flask import Flask, request, jsonify
import adsk.core, adsk.fusion, traceback
 
app = Flask(__name__)
 
@app.route('/Test', methods=['POST'])
def add_parameter():
    try:
        data = request.json
        param_name = data.get('name', 'length')
        param_unit = data.get('unit', 'cm')
        param_value = data.get('value', 20.0)
 
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
 
        param_value_real = adsk.core.ValueInput.createByReal(param_value)
        design.userParameters.add(param_name, param_value_real, param_unit, "")
 
       
        return jsonify({"message": f"Parameter '{param_name}' added successfully.", "unit": param_unit, "value": param_value}), 200
 
    except Exception as e:
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500
 
if __name__ == '__main__':
    app.run(debug=True, port=5000)