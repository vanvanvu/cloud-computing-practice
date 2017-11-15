var PROTO_PATH = __dirname + '/../proto/workflow.proto';

var grpc = require('grpc');
var workflow_proto = grpc.load(PROTO_PATH).workflow;

function main() {
  var client = new workflow_proto.Workflow('localhost:50051',
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
