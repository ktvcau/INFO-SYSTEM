## Installing Dependencies using `pip install -r requirements.txt`

To install all the necessary libraries for the provided code using a `requirements.txt` file, follow these steps:

1. **Create a `requirements.txt` file:** First, create a text file named `requirements.txt` in the same directory as your Python script.

2. **List Dependencies:** Inside `requirements.txt`, list all the libraries needed for your project, each on a separate line. In this case, the required libraries are:

    ```plaintext
    speedtest-cli
    psutil
    requests
    ```

3. **Install Dependencies:** Open a terminal or command prompt, navigate to the directory containing `requirements.txt`, and run the following command:

    ```bash
    pip install -r requirements.txt
    ```

   This command instructs pip to read the `requirements.txt` file and install all the listed dependencies.

## Usage

After installing the dependencies, you can use the provided Python script as follows:

1. **Run the Script:** Execute the Python script using the Python interpreter. You can run the script by typing the following command in the terminal or command prompt:

    ```bash
    python system_info.py
    ```

2. **View System Information:** Once the script is executed, it will display various system information such as device name, machine type, IP address, Wi-Fi speed, CPU information, CPU usage percentage, RAM usage, and disk usage.
