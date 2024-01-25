# Employee Management System (EMS)

## Set this project locally (Manual) :computer:

 - Clone this repository or download the zip file.<br>

 - Go inside the project root directory i.e webapp.

 - Create a python3 virtual environment:

    ```bash
    python3 -m venv .venv
    ```

    Or, use [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html):

    ```bash
    virtualenv .venv
    ```

 - Activate the virtual environment:

    - On Linux or Mac or any Unix based system-

        ```bash
        source .venv/bin/activate
        ```

    - On Windows based OS-
        ```
        .venv\Scripts\activate
        ```

 - Now Install the dependecies:

    ```bash
    pip install -r requirements.txt
    ```

  - Run these commands command before starting the development server:

    ```bash
    python manage.py migrate
    python manage.py collectstatic
    ```


 - Ready to go:

    #### Run the application

    ```bash
    python manage.py runserver
    ```

# Thanks

