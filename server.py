from spyne import Application, rpc, ServiceBase
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class HelloWorldService(ServiceBase):
    @rpc(str, _returns=str)
    def say_hello(ctx, name):
        return f"Hello, {name}!"

# Create the SOAP application
application = Application([HelloWorldService], 
                          tns='spyne.examples.helloworld',
                          in_protocol=Soap11(),
                          out_protocol=Soap11())

# Create the WSGI application
wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('127.0.0.1', 8000, wsgi_application)
    print("SOAP server running on http://localhost:8000")
    server.serve_forever()

