1) Make sure you are in the same directory as the dockerfile.

2) Run the following commands while in the current directory in your terminal in sequence:
    1- docker build -t clickhouse-server .
    2- docker run -d --name clickhouse-server-container -p 9000:8123 clickhouse-server

3) Uncomment create_table() and add_entries() when running the script for the first time.

4) comment them back to prevent getting errors due to create a table with the same name.
