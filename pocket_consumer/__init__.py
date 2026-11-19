"""Small, dependency-light client for Pocket public RPC endpoints."""

from .client import PocketRpcClient, PocketRpcError

__all__ = ["PocketRpcClient", "PocketRpcError"]
