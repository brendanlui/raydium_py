from solana.rpc.api import Client
from solders.keypair import Keypair  # type: ignore

PRIV_KEY = ""    # TODO
RPC = "https://api.mainnet-beta.solana.com"
UNIT_BUDGET = 100_000
UNIT_PRICE = 1_000_000
client = Client(RPC)
payer_keypair = Keypair.from_base58_string(PRIV_KEY)
