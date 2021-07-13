# Webhook Shell Invoker

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/aa6de264cff84015905247f86ef3c232)](https://app.codacy.com/gh/kolayne/webhook_shell_script_invoker?utm_source=github.com&utm_medium=referral&utm_content=kolayne/webhook_shell_script_invoker&utm_campaign=Badge_Grade_Settings)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/204dc5924bdb413280ba7a566e4040c6)](https://www.codacy.com/gh/kolayne/webhook_shell_invoker/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=kolayne/webhook_shell_invoker&amp;utm_campaign=Badge_Grade)

Simple tool for running shell scripts on webhook events. A simple sample use case is Github Actions: send request from
a deploy action to a server with WSI (this project) running to easily run a deploy script

## Usage (server)

To set up a requests acceptor on a server, follow these steps:

1.  Create scripts inside `scripts/` directory and make them runnable (`chmod +x`)

2.  Create `config.py` with the following variables defined:

    -   `secret_token` A string token to verify that a trusted service is sending the request

    -   `projects_to_scripts` A dictionary from (strings) projects names to (strings) names of script files
         inside `scripts/` directory

    Example is in `example_config.py`

3.  Run `python3 main.py`

## Usage (client)

Default port is `2010`. Post HTTP requests to `/` with header `Authorization` set to the authorization secret key from
`config.py` and json body with key `project_name` set to name of a project (key of `projects_to_scripts`
from `config.py`) are accepted. You can send it in any way. Example with curl:
```bash
curl --fail http://localhost:2010 -H "Content-Type: application/json" \
        -H "Authorization: password12345" \
        --data '{"project_name": "project_name_1"}'
```
