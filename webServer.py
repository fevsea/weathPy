from http.server import BaseHTTPRequestHandler, HTTPServer
import makeGraph


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        print(self.path)

        if self.path == "/foo.png":
           self.send_header("Content-type", "image/png")
           self.end_headers()
           self.wfile.write(load_binary('foo.png'))
           return


        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        makeGraph.render()

        html = """<!DOCTYPE html><html><head>
<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 15px;
}
</style>
<title>Temperaturas</title>
</head><body><img src="foo.png" alt="Full history"><table style="width:100%">"""


        makeGraph.initDB()
        data = makeGraph.readDB()
        for item in data:
            html += "<tr>"
            for col in item:
                html += "<td>" + str(col) + "</td>"
            html += "</tr>"

        html += """</table></body></html>"""

        # Write content as utf-8 data
        self.wfile.write(bytes(html, "utf8"))
        return


def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


def load_binary(file):
    with open(file, 'rb') as file:
        return file.read()


run()
