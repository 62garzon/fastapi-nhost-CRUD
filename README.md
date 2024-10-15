# fastapi-nhost-CRUD


### Project Setup
1. Clone the project repository:
    ```bash
   git clone https://github.com/62garzon/fastapi-nhost-CRUD.git 
   ```
   
2. Navigate to the project directory:
    ```bash
    cd fastapi-nhost-CRUD/
    ```

3. Create and activate a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set up environment variables by copying the example configuration:
    ```bash
    cp .env.example .env
    ```

## Install the Nhost CLI
1. Start docker

2. Download the client
    ```bash
    sudo curl -L https://raw.githubusercontent.com/nhost/cli/main/get.sh | bash
    ```
3. Select the project
    ```bash
    nhost init --remote
    ```
   
4. Update JWT_SECRET secret so HASURA and FastAPI share the authentication
   a.
       ```bash
       vi  .env
       ```
   b. Navigate to https://local.dashboard.local.nhost.run/local/local/settings/secrets and update the key: HASURA_GRAPHQL_JWT_SECRET

5. Reload NHOST development environment
    ```bash
    nhost nhost up
    ```

## Running the Application
Start the application:

```bash
fastapi dev src/
```