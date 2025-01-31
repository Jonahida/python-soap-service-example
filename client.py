import zeep

# Define the SOAP client
wsdl = 'http://localhost:8000/?wsdl'

client = zeep.Client(wsdl)

# Call the SOAP service
name = "Jonathan"
response = client.service.say_hello(name)

print(response)

