mkdir -p ~/.streamlit/
echo "[general]  
email = \"d.gunjan@iitg.ac.in\""  > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = true"  >> ~/.streamlit/config.toml