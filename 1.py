from flask import Flask, redirect, url_for, request
import pandas

# <---todo--->
# read data from table in data variable
data = pandas.read_csv("IN.csv")


def add_to_data(pincode,address,city,latitude,longitude):
	pass
	#  < --- TODO---- >
	# add entry in table

def add_data(pincode,address,city,latitude,longitude):
	global data
	around_diff = 0.005
	for key in data['key']:
		if pincode in key:
			# print('pincode already present')
			return False
		else :
			pass
	for data_latitude in data["latitude"]:
		diff = abs(float(latitude) - float(data_latitude))
		if diff <= around_diff:
			return False
		else :
			pass
	for data_longitude in data["longitude"]:
		diff = abs(float(longitude) - float(data_longitude))
		if diff < around_diff:
			return False
		else :
			pass
	add_to_data(pincode,address,city,latitude,longitude)
	return True

app = Flask(__name__)

@app.route('/post_location',methods = ['POST'])
def post_location():
	if request.method == 'POST':
		pincode = request.form['pincode']
		address = request.form['address']
		city = request.form['city']
		latitude = request.form['latitude']
		longitude = request.form['longitude']
		result = add_data(pincode,address,city,latitude,longitude)
		if result :
			return 'Data Added successfully'
		else:
			return "data already present"

if __name__ == '__main__':
	app.run(debug = True)