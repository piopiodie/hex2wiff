# Hex to Wif

## **Convert your Hexadecimal Bitcoin Private Key to Wallet Import Format (WIF)**


For security reasons, ensure to:

1. Perform this conversion on a computer that is offline, reducing the risk of exposing your private key.
2. Once converted, securely store the WIF key and avoid sharing it.

Remember, your private key is sensitive information. Handle with care! (By ChatGPT)

### **Running the hex2wif.py Script in Different Environments**


#### **1. MacBook (macOS):**

**Installing Python:**

Most macOS versions come pre-installed with Python 2.7. 

However, Python 3 is recommended.
To install Python 3, you can use the Homebrew package manager:


```
brew install python3
```

Install 
hashlib
binascii
base58 with pip command

```
pip install hashlib
```

```
pip install binascii
```

```
pip install base58
```

### **Executing the Script:**

Open the Terminal.

Navigate to the directory containing hex2wif.py using the cd command.

**Run the script with:**



```
python3 hex2wif.py
```


#### **2. Linux:**

   
**Installing Python:**

Many Linux distributions come with Python pre-installed. 

Check the version with python --version or python3 --version.

To install Python 3 on Debian-based distributions (like Ubuntu), use:

```
sudo apt-get update
sudo apt-get install python3
```


Executing the Script:

Open the Terminal.
Navigate to the directory containing hex2wif.py using the cd command.
Run the script with:


```
python3 hex2wif.py
```


#### **3. Windows:**


**Installing Python:**

Visit the official Python website and download the installer for Windows.

Run the installer and make sure to check the "Add Python to PATH" option during installation.
Executing the Script:

Open the Command Prompt.

Navigate to the directory containing hex2wif.py using the cd command.

Run the script with:


```
python hex2wif.py
```
