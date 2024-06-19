# Copy ClickHouse Yandex image.
FROM yandex/clickhouse-server:latest

# Set ClickHouse environment vars.
ENV CLICKHOUSE_DB default
ENV CLICKHOUSE_USER default
ENV CLICKHOUSE_PASSWORD ''

# Update package manager and instal gosu to run commands as admin.
RUN apt-get update && apt-get install -y gosu && rm -rf /var/lib/apt/lists/*

# Create a directory for ClickHouse data.
RUN mkdir -p /var/lib/clickhouse && chown -R clickhouse:clickhouse /var/lib/clickhouse

# Expose all protocol ports.
EXPOSE 8123 9000 9009

# Start ClickHouse server.
CMD ["gosu", "clickhouse", "clickhouse-server", "--config-file=/etc/clickhouse-server/config.xml"]
