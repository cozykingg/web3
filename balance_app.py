from web3 import Web3

GOERLI_URL = ""
ACCOUNT = ""

web3 = Web3(Web3.HTTPProvider(GOERLI_URL))

try:
    LINK = web3.isConnected()
except:
    print ("Link Failed!")
    pass


def get_balance(account=ACCOUNT):
    
    balance = web3.eth.getBalance(account)
    eth_balance = float(web3.fromWei(balance,"ether"))
    return eth_balance

def get_account(account=ACCOUNT):
    
    acc = web3.eth.accounts
    print (acc)
    return account
