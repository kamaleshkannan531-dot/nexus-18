from http.server import HTTPServer, BaseHTTPRequestHandler

content = """<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocol Suite</title>
</head>
<body bgcolor="lightblue">
    <h1 align="center">TCP/IP PROTOCOL SUITE</h1>
    <h3 align="center">NAME: V KAMALESH KANNAN &nbsp;|&nbsp; REGISTER NO: 26011247</h3>
    <table border="2" align="center" width="75%" cellpadding="10" bgcolor="white">
        <tr bgcolor="lightgrey">
            <th>Layer</th>
            <th>Protocols</th>
        </tr>
        <tr>
            <td><b>Application Layer</b></td>
            <td>HTTP, HTTPS, FTP, SMTP, DNS, TELNET</td>
        </tr>
        <tr>
            <td><b>Transport Layer</b></td>
            <td>TCP, UDP</td>
        </tr>
        <tr>
            <td><b>Internet Layer</b></td>
            <td>IP, ICMP, ARP, IGMP</td>
        </tr>
        <tr>
            <td><b>Network Access Layer</b></td>
            <td>Ethernet, Wi-Fi, PPP, Token Ring</td>
        </tr>
    </table>
</body>
</html>"""

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET request received...")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyServer)
    print("Serving on http://127.0.0.1:8000 ...")
    httpd.serve_forever()
