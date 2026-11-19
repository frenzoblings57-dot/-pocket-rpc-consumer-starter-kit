# Pocket RPC Consumer Starter Kit

A beginner-friendly, reusable example for builders who want to call existing Pocket Network public blockchain RPC services from their own application.

This kit **consumes an existing Pocket service**. It does not register a new service, run a supplier, operate a RelayMiner, create a wallet, stake POKT, or submit a Mainnet transaction.

## What it demonstrates

- Standard JSON-RPC over HTTPS
- A small reusable Python client
- Chain-slug based endpoint selection
- A working latest-block example
- Automated tests with mocked responses
- Clean-environment validation
- Docker support

## Quick start

Requirements: Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate
python -m examples.query_latest_block
```

Expected output is a JSON object similar to:

```json
{"chain": "eth", "latest_block": 26439787, "endpoint": "https://eth.api.pocket.network"}
```

Block numbers change continuously, so your number will be different.

## Use another supported chain

```bash
python -m examples.query_latest_block --chain base
python -m examples.query_latest_block --chain arb-one
```

The client uses the documented Pocket pattern:

```text
https://{chain-slug}.api.pocket.network
```

See Pocket’s [Supported Chains](https://docs.pocket.network/developers/supported-chains) page for current slugs.

## Use the client in your own code

```python
from pocket_consumer import PocketRpcClient

client = PocketRpcClient(chain="eth")
latest_block = client.latest_block_number()
chain_id = client.call("eth_chainId")
print(latest_block, chain_id)
```

The client uses only Python’s standard library, so the runtime example has no third-party dependency and no API key.

## Run tests and clean validation

```bash
python -m pip install -r requirements-dev.txt
pytest -q
./scripts/validate_clean.sh
```

The tests mock network responses and do not spend funds. The clean validation script installs the pinned development dependency, runs the test suite, and compiles the code.

## Run with Docker

```bash
docker compose run --rm pocket-rpc-example
```

The image runs the same read-only latest-block example.

## Pocket resources

- [Pocket Developer Documentation](https://docs.pocket.network/developers)
- [Supported Chains](https://docs.pocket.network/developers/supported-chains)
- [Integration Examples](https://docs.pocket.network/developers/integration-examples)
- [Pocket Agentic Portal](https://agent.pocket.network/)

## Scope and safety

This is a consumer-side starter kit. It is intentionally limited to public, read-only RPC calls. It does not handle private keys, signing, staking, paid relays, supplier operations, or deployment of a new Pocket service.
