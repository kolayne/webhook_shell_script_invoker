# Webhook Shell Invoker

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0c6e62c7d7264d7f8a5723e636699dde)](https://app.codacy.com/manual/kolayne/webhook_shell_invoker?utm_source=github.com&utm_medium=referral&utm_content=kolayne/webhook_shell_invoker&utm_campaign=Badge_Grade_Dashboard)

Simple tool for running shell scripts on webhook events

## Usage

1.  Create scripts inside `scripts/` directory and make them runnable (`chmod +x`)

2.  Create `config.py` with the following variables defined:

    -   `secret_token` A string tooken to verify that a trusted service is sending the request
    -   `projects_to_scripts` A dictionary from (strings) projects names to (strings) names of script files inside `scripts/` directory

    Example is in `example_config.py`

3.  Run `python3 main.py`
