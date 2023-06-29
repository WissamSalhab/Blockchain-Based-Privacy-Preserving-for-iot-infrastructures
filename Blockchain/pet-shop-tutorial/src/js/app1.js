App = {
  web3Provider: null,
  contracts: {},

  init: async function() {

    return await App.initWeb3();
  },

  initWeb3: async function() {
	if (window.ethereum) {
		  App.web3Provider = window.ethereum;
	  try {
	    // Request account access
	    await window.ethereum.enable();
  	} catch (error) {
	    // User denied account access...
	    console.error("User denied account access")
 	 }
	}
	web3 = new Web3(App.web3Provider);
    return App.initContract();
  },

  initContract: function() {
	$.getJSON('GiveConsent.json', function(data) {
	  // Get the necessary contract artifact file and instantiate it with @truffle/contract
	  var GiveConsentArtifact = data;
	  App.contracts.GiveConsent = TruffleContract(GiveConsentArtifact);
	  // Set the provider for our contract
	  App.contracts.GiveConsent.setProvider(App.web3Provider);
	  // Use our contract to retrieve and mark the adopted pets
	  App.markAccepted();
	});

    //return App.bindEventss();
  },
/*
  bindEventss: function() {
    $(document).on('click', '.btn-success', App.handleAccept);
  },
*/
markAccepted: function() {
var GiveConsentInstance;

App.contracts.GiveConsent.deployed().then(function(instance) {
  GiveConsentInstance = instance;

web3.eth.getAccounts(function(error, accounts) {
  if (error) {
    console.log(error);
  }

  var account = accounts[0];


  return GiveConsentInstance.RequestConsent(50, {from: account});
}).then(function(bool) {
  GiveConsentInstance.VerifyRequest(50)
}).then(function(bool) {
  $('.abcdefg').eq(0).find('button').text('Adopt').attr('disabled', true);
}).catch(function(err) {
  console.log(err.message);
});
  },
/*
  handleAccept: function(event) {
    event.preventDefault();    var petId = parseInt($(event.target).data('id'));    var adoptionInstance;
    web3.eth.getAccounts(function(error, accounts) {
      if (error) {
        console.log(error);
      }
    var account = accounts[0];
    App.contracts.Adoption.deployed().then(function(instance) {
      adoptionInstance = instance;
      return adoptionInstance.adopt(petId, {from: account});
    }).then(function(result) {
    return App.markAdopted();
  }).catch(function(err) {
    console.log(err.message);
  });
});
}
*/
};
};

$(function() {
  $(window).load(function() {
    App.init();
  });
});
