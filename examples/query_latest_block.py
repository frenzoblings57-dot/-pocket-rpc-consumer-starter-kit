#!/usr/bin/env python3
"""Minimal example: read the latest Ethereum block through Pocket."""

import argparse
import json

from pocket_consumer import PocketRpcClient

parser = argparse.ArgumentParser(description="Read the latest block through Pocket public RPC")
parser.add_argument("--chain", default="eth", help="Pocket chain slug, default: eth")
args = parser.parse_args()

client = PocketRpcClient(chain=args.chain)
block = client.latest_block_number()
print(json.dumps({"chain": args.chain, "latest_block": block, "endpoint": client.endpoint}))
