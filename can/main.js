var http = require('http');
var fs = require('fs');
var url = require('url');
var path = require('path');

var mime = {
    html: 'text/html',
    txt: 'text/plain',
    css: 'text/css',
    gif: 'image/gif',
    jpg: 'image/jpeg',
    png: 'image/png',
    svg: 'image/svg+xml',
    js: 'application/javascript'
};

http.createServer(function (request, response) {
   // Parse the request containing file name
   var file = url.parse(request.url).pathname.substr(1);
   
   // Print the name of the file for which request is made.
   console.log("Request for " + file + " received.");
   
   var type = mime[path.extname(file).slice(1)] || 'text/plain';
   console.log("Looking for file "+file+" with type "+type);
   var s = fs.createReadStream(file);
    s.on('open', function () {
        response.setHeader('Content-Type', type);
        s.pipe(response);
    });
    s.on('error', function () {
        response.setHeader('Content-Type', 'text/plain');
        response.statusCode = 404;
        response.end('Not found');
    });
}).listen(8081, function() {
    // Console will print the message
    console.log('Server running at http://127.0.0.1:8081/');
});
