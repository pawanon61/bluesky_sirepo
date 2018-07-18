import happi

client = happi.Client(path = r"C:\Users\gaire01\Downloads\codes\happi_db.json")
x1 = client.find_device(name = 'xrt_m1h')
print(x1.z)