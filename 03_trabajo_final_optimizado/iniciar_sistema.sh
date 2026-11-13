#!/usr/bin/env bash
# Script de inicio operativo del Sistema Clínico "Sonrisa Sana"
echo "=========================================================="
echo "   Iniciando Servidor Web - Clínica Sonrisa Sana (FastAPI) "
echo "=========================================================="
cd "$(dirname "$0")"
python3 run_server.py
