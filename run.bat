:: Create a virtual environment
py -m venv venv

:: Activate the virtual environment
call venv\Scripts\activate

:: Install dependencies
py -m pip install requests pyyaml

py ./src/fetch_pokemon.py
py ./src/fetch_evolution_chains.py
py ./src/generate_csv.py
py ./src/generate_yamls.py

pause