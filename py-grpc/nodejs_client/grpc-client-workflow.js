var PROTO_PATH = __dirname + '/../proto/workflow.proto';
var fs = require("fs");
var grpc = require('grpc');
var workflow_proto = grpc.load(PROTO_PATH).workflow;

function main() {
  var client = new workflow_proto.Workflow('localhost:50051',
                                       grpc.credentials.createInsecure());
  var jsonMess;
  if (process.argv.length >= 3) {
    jsonMess = require(process.argv[2]);
  } else {
    jsonMess = {
      "Header": "RunningRequest",
      "Body": [
        [0],
        [0, 1],
        [0, 1, 0, 1]
      ]
    }
  }
  client.running({message: JSON.stringify(jsonMess)}, function(err, response) {
    console.log('Response: \n', response.message);  
  });
}

main();
