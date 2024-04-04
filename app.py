from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3307
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sensors_db'

mysql = MySQL(app)

# Cargar datos de los sensores
@app.route('/api/v1/load', methods=['POST'])
def load_data():
    data = request.json
    try:
        sensor_values = {}
        
        for sensor_data in data:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO measurement_detail (sensor, value, unit, timestamp) VALUES (%s, %s, %s, %s)", (sensor_data['sensor'], sensor_data['value'], sensor_data['unit'], sensor_data['timestamp']))
            mysql.connection.commit()
            cursor.close()
            
            sensor = sensor_data['sensor']
            value = sensor_data['value']
            if sensor in sensor_values:
                sensor_values[sensor].append(value)
            else:
                sensor_values[sensor] = [value]
        
        for sensor, values in sensor_values.items():
            avg_value = mean(values)
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO summary (sensor, average_value) VALUES (%s, %s)", (sensor, avg_value))
            mysql.connection.commit()
            cursor.close()
        
        return jsonify({'message': 'Datos cargados correctamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Obtener la lista de resumen de valores promedios
@app.route('/api/v1/list', methods=['GET'])
def list_summary():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM summary")
        data = cursor.fetchall()
        cursor.close()
        summary_list = [{'sensor': row[0], 'valor_promedio': row[1], 'unidad': row[2], 'marca_tiempo': row[3]} for row in data]
        return jsonify(summary_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
