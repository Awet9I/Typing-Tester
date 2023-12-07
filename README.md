# Typing-Tester Application Setup Instructions

To run the application, follow these steps:

## For GitHub:
- Clone the repository 

## Setting Up the Virtual Environment:
- It is recommended to create a virtual environment.
  - **For Mac or Linux OS**:
    ```
    python3 -m venv <dirname>
    ```
  - **For Windows**:
    ```
    python -m venv <dirname>
    ```

## Activating the Virtual Environment:
- After creating the Python virtual environment, activate it:
  - **For Mac or Linux OS**:
    ```
    source <dirname>/bin/activate
    ```
  - **For Windows**:
    ```
    cd <dirname>/Scripts
    ./activate
    ```

## Installing Dependencies:
- When you are inside your virtual environment, run the following to install all external libraries used in the project:
```

pip install -r requirements.txt
```


## Running the Application:
- The application can be started by running from the root directory:

```
python ./play.py
```
