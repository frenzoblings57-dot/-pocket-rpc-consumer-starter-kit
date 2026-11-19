import json
from unittest.mock import patch

from pocket_consumer import PocketRpcClient, PocketRpcError


def test_endpoint_is_derived_from_chain_slug():
    client = PocketRpcClient("base")
    assert client.endpoint == "https://base.api.pocket.network"


def test_latest_block_decodes_hex_result():
    client = PocketRpcClient("eth")
    with patch.object(client, "call", return_value="0x10"):
        assert client.latest_block_number() == 16


def test_rpc_errors_are_exposed_as_pocket_rpc_error():
    client = PocketRpcClient("eth")
    with patch.object(client, "call", side_effect=PocketRpcError("upstream error")):
        try:
            client.latest_block_number()
        except PocketRpcError as exc:
            assert "upstream error" in str(exc)
        else:
            raise AssertionError("PocketRpcError was not raised")


def test_invalid_chain_is_rejected():
    try:
        PocketRpcClient("ETH")
    except ValueError as exc:
        assert "chain" in str(exc)
    else:
        raise AssertionError("invalid chain was accepted")
