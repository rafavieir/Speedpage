#!/bin/bash

streamlit run index.py > /tmp/monitoring_log_py.log 2>&1 &

echo "Script Python iniciado em segundo plano. Logs em /tmp/monitoring_log_py.log"
