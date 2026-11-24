use alloy::sol;

sol! {
	#[sol(rpc)]
	contract MyTokenContract {
		function balanceOf(address account) external view returns (uint256);
		function mint(address to, uint256 amount) external;
	}
}

pub async fn get_token_balance(config: &Config, player: Address, amount: U256) ->Result<U256> {
	let rpc_url = config.rpc_http_url.parse().context("Wrong http url format")?;
	let provider = ProviderBuilder::new().connect_http(rpc_url);
	let contract = MyTokenContract::new(config.token_contract_address, provider);
	let balance = contract.balanceOf(player, amount).call().await.context("Failed to get player balance")?;
	Ok(balance._0)
}

