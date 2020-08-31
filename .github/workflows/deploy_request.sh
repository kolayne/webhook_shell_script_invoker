#!/bin/bash

curl --silent --show-error --fail -X POST "$deployment_server" \
          -H "Authorization: $deployment_token" -H 'Content-Type: application/json' \
          -d '{"project_name": "webhook_shell_invoker"}'
exit_code=$?

if [[ exit_code -eq 52 ]]; then
  exit 0  # Ignoring empty reply from server (self-restart)
else
  exit $exit_code
fi
