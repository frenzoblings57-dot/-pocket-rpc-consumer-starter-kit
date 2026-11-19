"""Reusable JSON-RPC client for Pocket public blockchain endpoints."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any


class PocketRpcError(RuntimeError):
    """Raised when Pocket or the upstream chain returns an error."""


class PocketRpcClient:
    """Call a Pocket public RPC endpoint using standard JSON-RPC.

    No API key, wallet, POKT, or application stake is required for the public
    endpoint example. Change only the chain slug to target another supported
    network.
    """

    def __init__(self, chain: str = "eth", timeout: float = 15.0) -> None:
        if not chain or any(ch not in "abcdefghijklmnopqrstuvwxyz0123456789-_" for ch in chain):
            raise ValueError("chain must contain only lowercase letters, numbers, '-' or '_'")
        self.chain = chain
        self.endpoint = f"https://{chain}.api.pocket.network"
        self.timeout = timeout

    def call(self, method: str, params: list[Any] | None = None) -> Any:
        """Call a JSON-RPC method and return its result."""
        if not method:
            raise ValueError("method is required")
        payload = {"jsonrpc": "2.0", "method": method, "params": params or [], "id": 1}
        request = urllib.request.Request(
            self.endpoint,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                body = json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise PocketRpcError(f"request to {self.endpoint} failed: {exc}") from exc

        if "error" in body:
            raise PocketRpcError(str(body["error"]))
        if "result" not in body:
            raise PocketRpcError("JSON-RPC response did not contain a result")
        return body["result"]

    def latest_block_number(self) -> int:
        """Return the latest block number as an integer."""
        result = self.call("eth_blockNumber")
        try:
            return int(result, 16)
        except (TypeError, ValueError) as exc:
            raise PocketRpcError(f"invalid block number returned: {result!r}") from exc
