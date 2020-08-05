# Webhook Shell Invoker
Simple tool for running shell scripts on webhook events

## Usage
1. Create scripts inside `scripts/` directory and make them runnable (`chmod +x`)
2. Create `config.py` with the following variables defined:
    * `secret_token` A string tooken to verify that a trusted service is sending the request
    * `projects_to_scripts` A dictionary from (strings) projects names to (strings) names of script files inside `scripts/` directory

    Example is in `example_config.py`
3. Run `python3 main.py`
