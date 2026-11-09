mod config;
use config::Config;

fn main() -> anyhow::Result<()> {
	let config = Config::load()?;
	println!("ws url : {}", config.rpc_ws_url);
	println!("http url : {}", config.rpc_http_url);
	println!("contract addr : {}", config.contract_address);
	println!("server port : {}", config.server_port);
	println!("private key : {}", config.backend_private_key);
	Ok(())
}
