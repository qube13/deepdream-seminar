const http = require('http');
var fs = require('fs');
const port=process.env.PORT || 3000
const server = http.createServer((req, res) => {
res.statusCode = 200;
res.setHeader('Content-Type', 'text/html');
fs.readFile('./index.html', null, function(error, data) {
    if (error) {
        response.writeHead(404);
        response.write('File not found!');
    } else {
        response.write(data);
    }
    res.end();
});
});
server.listen(port,() => {
console.log(`Server running at port `+port);
});
