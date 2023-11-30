import serial
from sklearn.ensemble import RandomForestRegressor
from joblib import load
import time

# Load the trained Random Forest model
model = load('C:/Users/nikhi/Desktop/VS code Workspace/EV_Range_Prediction/random_forest_model.joblib')

# Open the serial connection to the Arduino
ser = serial.Serial('COM3', 9600)  # Adjust the COM port accordingly

# Read sensor values from Arduino
arduino_data = ser.readline().decode().strip()
sensor_values = [float(val) for val in arduino_data.split(',')]

# Predict remaining range using the ML model
remaining_range = model.predict([sensor_values])

ser.baudrate = 9600
ser.bytesize = 8
ser.parity = 'N'
time.sleep(2)

# Send the prediction back to the Arduino
ser.write(f'RANGE  : {remaining_range[0]:.2f}\n'.encode())

# Print the result
print(f'Received sensor values: {sensor_values}')
print(f'Predicted Remaining Range: {remaining_range[0]:.2f}')

ser.close()
