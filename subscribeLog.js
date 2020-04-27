var Web3 = require('web3');

var web3 = new Web3(new Web3.providers.WebsocketProvider('wss://ropsten.infura.io/ws/v3/595b7af287a44ac4876e614e31f797ef'));

web3.eth.subscribe('logs', {
	address: '0xa93f97e8a30447b27682fee9b10d6dcbe3711da2',
	topics : [null]
}, function(error, result) {
	if (error) {
		console.log("error", error);
	}
}).on("connected", function(subscriptionId) {
	console.log("subscrpitionId : ", subscriptionId);
}).on("data", function(log) {
	console.log("log", log);
});
