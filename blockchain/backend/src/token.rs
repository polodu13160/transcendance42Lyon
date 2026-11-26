use crate::config::Config;
use anyhow::{Context, Result};
use alloy::primitives::{Address, B256, U256};
use alloy::signers::local::PrivateKeySigner;
use alloy::network::EthereumWallet;
use alloy::providers::{ProviderBuilder, Provider};
use alloy::sol;

sol! {
	#[sol(rpc)]
	contract MyTokenContract {
		function balanceOf(address account) external view returns (uint256);
		function mint(address to, uint256 amount) external;
		event Transfer(address indexed from, address indexed to, uint256 value);
	}
}

pub async fn check_burn_transaction(config: &Config, tx_hash: B256,player: Address, amount: U256) -> Result<bool> {
	let rpc_url = config.rpc_http_url.parse().context("Wrong http url format")?;
	let provider = ProviderBuilder::new().connect_http(rpc_url);
	match provider.get_transaction_receipt(tx_hash).await? {
		Some(receipt) => {
			if receipt.status() {
				for logs in receipt.inner.logs() {
					if logs.address() == config.token_contract_address {
						if let Ok(decoded) = logs.log_decode::<MyTokenContract::Transfer>() {
							let event = decoded.data();
							if event.from == player && event.to == Address::ZERO && event.value == amount {
								return Ok(true);
							}
						}
					}
				}
			}
			return Ok(false);
		}
		None => {
			return Ok(false);
		}
	}
}

pub async fn get_token_balance(config: &Config, player: Address) ->Result<U256> {
	let rpc_url = config.rpc_http_url.parse().context("Wrong http url format")?;
	let provider = ProviderBuilder::new().connect_http(rpc_url);
	let contract = MyTokenContract::new(config.token_contract_address, provider);
	let balance = contract.balanceOf(player).call().await.context("Failed to get player balance")?;
	Ok(balance)
}

pub async fn send_mint(config: &Config, player: Address, amount: U256) -> Result<B256> {
	let signer = config.backend_private_key.parse::<PrivateKeySigner>().context("Invalid backend private key")?;
	let wallet = EthereumWallet::new(signer);
	let rpc_url = config.rpc_http_url.parse().context("Wrong http url format")?;
	let provider = ProviderBuilder::new().wallet(wallet).connect_http(rpc_url);
	let contract = MyTokenContract::new(config.token_contract_address, provider);
	let pending_tx = contract.mint(player, amount).send().await.context("Failed to send mint transaction")?;
	let receipt = pending_tx.get_receipt().await.context("Failed to get mint transaction receipt")?;
	Ok(receipt.transaction_hash)
}
