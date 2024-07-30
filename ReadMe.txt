1) Make sure you are in the same directory as the dockerfile.

2) Run the following commands while in the current directory in your terminal in sequence:
    1- docker build -t clickhouse-server .
    2- docker run -d --name clickhouse-server-container -p 8123:8123 clickhouse-server
