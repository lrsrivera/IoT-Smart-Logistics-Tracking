from web3 import Web3
import time

# 1. Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Verify connection
if web3.is_connected():
    print("✅ Connected to Ganache")
else:
    print("❌ Connection failed")

# 2. Load the contract
contract_address = "0x75Ace60854a5C05BF576DF1912433B4fD48936bf"  # From Remix
abi = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "packageId",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "location",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "status",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "additionalInfo",
				"type": "string"
			}
		],
		"name": "PackageUpdated",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_packageId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_location",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_status",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_additionalInfo",
				"type": "string"
			}
		],
		"name": "updatePackage",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_packageId",
				"type": "string"
			}
		],
		"name": "getLatestPackageStatus",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_packageId",
				"type": "string"
			}
		],
		"name": "getPackageHistory",
		"outputs": [
			{
				"internalType": "uint256[]",
				"name": "",
				"type": "uint256[]"
			},
			{
				"internalType": "string[]",
				"name": "",
				"type": "string[]"
			},
			{
				"internalType": "string[]",
				"name": "",
				"type": "string[]"
			},
			{
				"internalType": "string[]",
				"name": "",
				"type": "string[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "index",
				"type": "uint256"
			}
		],
		"name": "getRecord",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getTotalRecords",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "MAX_ENTRIES",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "packageHistory",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "packageId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "location",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "status",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "additionalInfo",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "packageRecords",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "packageId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "location",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "status",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "additionalInfo",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]  

# Load contract
try:
    contract = web3.eth.contract(address=contract_address, abi=abi)
    web3.eth.default_account = web3.eth.accounts[0]
    print(f"✅ Connected to Smart Contract at {contract_address}")
except Exception as e:
    print(f"❌ Contract loading failed: {e}")
    exit()

# Check total records
try:
    total_records = contract.functions.getTotalRecords().call()
    print(f"🔹 Total Records Before Storing Data: {total_records}")
except Exception as e:
    print(f"❌ getTotalRecords failed: {e}")

# Store dummy data 
try:
    package_id = f"PKG{int(time.time())}"
    txn_hash = contract.functions.updatePackage(
        package_id,          # _packageId
        "Warehouse A",       # _location
        "In Transit",        # _status
        "Temperature: 22°C"  # _additionalInfo
    ).transact({
        'from': web3.eth.default_account,
        'gas': 500000  # Increased from 300000 to 500000
    })
    
    receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
    print(f"✅ Package updated! TX Hash: {receipt.transactionHash.hex()}")
    print(f"🛢 Gas used: {receipt.gasUsed}")
    
    # Verify the update
    (timestamp, location, status, info) = contract.functions.getLatestPackageStatus(package_id).call()
    print(f"\n📦 Latest status for {package_id}:")
    print(f"🕒 Timestamp: {timestamp}")
    print(f"📍 Location: {location}")
    print(f"🟢 Status: {status}")
    print(f"ℹ️ Additional Info: {info}")
    
except Exception as e:
    print(f"❌ updatePackage failed: {e}")

# Check updated records
try:
    updated_total = contract.functions.getTotalRecords().call()
    print(f"\n🔹 Total Records After Storing Data: {updated_total}")
except Exception as e:
    print(f"❌ Failed to get updated records: {e}")