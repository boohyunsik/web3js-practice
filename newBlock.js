var Web3 = require('web3');

var web3 = new Web3(new Web3.providers.WebsocketProvider('wss://mainnet.infura.io/ws/v3/18ca20a916f94f058de8c26f8b04d09b'));

web3.eth.subscribe('newBlockHeaders', (error, result) => {
	if (!error) {
		console.log(result);
	} else {
		console.log('error', error);
	}
}).on('data', function (transaction) {
	console.log('tx', transaction);
})