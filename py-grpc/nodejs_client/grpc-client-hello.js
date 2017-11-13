var PROTO_PATH = __dirname + '/Hello.proto';

var grpc = require('grpc');
var hello_proto = grpc.load(PROTO_PATH).hello;

function main() {
  var client = new hello_proto.Greeter('localhost:50052',
                                       grpc.credentials.createInsecure());
  var user;
  if (process.argv.length >= 3) {
    user = process.argv[2];
  } else {
    user = 'world';
  }
  client.sayHello({name: user}, function(err, response) {
    console.log('Greeting:', response.message);  
  });
}

main();
