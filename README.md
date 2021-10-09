# Services Development Technologies

## gRPC Hello world service

About: https://en.wikipedia.org/wiki/GRPC
## Installation
- Install dependencies:
    - grpcio https://pypi.org/project/grpcio
    - grpcio-tools https://pypi.org/project/grpcio-tools
    ```sh
    pip install -r requirements.txt
    ```
- Generate proto:
    ```sh
    chmod u+x ./generate.sh
    ./generate.sh
    ```
- Run server:
    ```sh
    python server.py
    ```

- Run client:
    ```sh
    python client.py
    ```