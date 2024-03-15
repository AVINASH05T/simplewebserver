from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
		<title>TOP COMPANIES IN REVENUE</title>
	</head>
	<body bgcolor="pink">
        <h1 align="center"> TOP COMPANIES IN THE WORLD BY REVENUE </h1>
	<table align="center" border="4" cellspacing="5" cellpadding="5" width="555" height="300" bgcolor="black" >
        <tr>
			<th bgcolor="grey">RANK</th>
			<th bgcolor="skyblue">COMPANIES</th>
			<th bgcolor="green">REVENUE</th>
            <th bgcolor="red">COUNTRY</th>
		</tr>
		<tr>
			<td bgcolor="white">1</td>
			<td bgcolor="white">APPLE</td>
			<td bgcolor="white">$385.70 B</td>
            <td bgcolor="white">USA</td>
		</tr>
		<tr>
			<td bgcolor="lightblue">2</td>
			<td bgcolor="lightblue">GOOGLE</td>
			<td bgcolor="lightblue">$307.39 B</td>
            <td bgcolor="lightblue">USA</td>
		</tr>
		<tr>
			<td bgcolor="lightgreen">3</td>
			<td bgcolor="lightgreen">MICROSOFT</td>
			<td bgcolor="lightgreen">$227.58 B</td>
            <td bgcolor="lightgreen">USA</td>
		</tr>
                <tr>
			<td bgcolor="gold">4</td>
			<td bgcolor="gold">IBM</td>
			<td bgcolor="yellow">$61.85 B</td>
            <td bgcolor="gold">USA</td>
		</tr>
                <tr>
			<td bgcolor="violet">5</td>
			<td bgcolor="violet">ORCALE</td>
			<td bgcolor="violet">$51.62 B</td>
            <td bgcolor="violet">USA</td>
		</tr>
                <tr>
			<td bgcolor="pink">6</td>
			<td bgcolor="pink">SCHNEIDER ELECTRIC</td>
			<td bgcolor="pink">$36.60 B</td>
            <td bgcolor="pink">FRANCE</td>
		</tr>
                 
	</table>
	</body>

</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()