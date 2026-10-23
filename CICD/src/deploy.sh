#!/bin/bash

set -e

SERVER="student2@192.168.100.20"
REMOTE_TMP="/tmp/DO"

echo "Copying DO to production server..."
scp build/DO "$SERVER:$REMOTE_TMP" # Передал программу с VM1 → VM2:/tmp/DO

echo "Installing DO to /usr/local/bin..."
ssh "$SERVER" "sudo /usr/bin/install -m 755 /tmp/DO /usr/local/bin/DO" # Зашёл на VM2 и установил её в /usr/local/bin/DO

echo "Deployment completed successfully"