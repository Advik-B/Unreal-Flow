# Dev Environment

Here is how to quickly get started with the development environment.

## Prerequisites
- Python 3.9+
- pip (That is linked to Python 3.9+)
- Protobuf compiler (protoc) (Get it from [here](https://github.com/protocolbuffers/protobuf/releases/latest))

## Setup
1. Clone the repository
2. Install Invoke: 
    ```
    pip install invoke
    ```
3. Install the dependencies:
    ```
    invoke requirements
    ```
4. Build the protobuf files:
    ```
    invoke proto
    ```

## Run
```
cd src
python -m unrealflow
```

## Build
```
invoke build
```
