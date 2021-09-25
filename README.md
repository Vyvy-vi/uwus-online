# uwus-online
A random message board that uwu-ifies anything you post :P


## Requirements

- `Python` v3.8+
- `pip` (required to install `poetry`)
- `poetry` (Package Manager)
- `taskipy` (for setting up scripts, commands)
- `python-dotenv` (for loading env variables)
- `Starlette` (ASGI Framework)
- `uvicorn` (ASGI Server)
- `Jinja2` (for rendering templates)

## Setting up the dev environment

1. Install Poetry
   ```
   pip install poetry
   ```

2. Set up the project dependencies and the pre-commit hooks
   ```
   poetry install
   poetry run task precommit
   ```

3. Run the project
   ```
   poetry run task start
   ```

4. Linting your code
   ```
   poetry run task lint
   ```

5. Test your code
   ```
   poetry run task test
   ```
