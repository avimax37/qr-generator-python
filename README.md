<!-- TITLE -->
# QR Code Generator using Python

QR Code Generator is a simple tool where a URL is provided as an input and the application generates the QR code and saves it as a **`.png`** file. It makes use of the pyqrcode module in Python.

<!-- BUILT WITH -->

## Built With

![Python][python-shield]

<!-- EXAMPLE -->

## Example

Input:
```
Please enter a URL:
github.com/avimax37
Please enter a filename:
my-github
```

Output:
```
Your QR is generated
```

Here we will get the QR code in a **`.png`** file named **`my-github`**.

<!-- INSTALLATION -->

## Installation

Use the link to download Python.

[![Python][python-shield]][python-url]

Use the link to download PyCharm.

[![PyCharm][pycharm-shield]][pycharm-url]

Use the link to download Visual Studio Code.

[![Visual Studio Code][visual studio code-shield]][visual studio code-url]

<!-- USAGE -->

## Usage

Open Command Prompt or Windows PowerShell to start.

```python
# get into python mode
python

# create a python script
hello.py
print("Hello World")

# go to the file path
cd <file path>

# run the script
python hello.py

# install pyqrcode module
pip install pyqrcode

# install pypng module
pip install pypng
```

VS Code or PyCharm can also be used.

<!-- CODE -->

## Code

So first we are going to import **`pyqrcode`** and **`png`** module.
```python
from pyqrcode import QRCode
```

This function will return a **`QRCode`** object.

Then we ask the user to enter a URL.

```python
print("Please enter a URL:")
user_url = input()
```
Here, as usual, we are making use of the **`input()`** function to get the input from the user in form of a string  and store it's value into the **`user_url`** variable.

```python
if user_url.find(".") != -1:
```

Here we are checking if the input string contains **`.`** or not. If it contains **`.`**, then it is considered as a valid url and we move to the next step.

Then we ask the user to enter a filename for the QR Code png file.

```python
print("Please enter a filename:")
file_name = input()
```

Now we create the QR Code.

```python
url = pyqrcode.create(user_url)
url.png(f"{file_name}.png", scale = 8)
```

This **`.create()`** function will create a QR Code of the url which was given by the user as input. Then the **`.png()`** function will create a **`.png`** file with a filename also given by the user and save it.

Now a confirmation message is generated.

```python
print("Your QR is generated.")
```

If the input string does not contain **`.`**, then it is considered as an invalid url and we get out of the loop with a warning message.

```python
else:
     print("Please enter a valid URL.")
```

<!-- LOGIC -->

## Logic

Let's consider the input is **`github.com/avimax37`**, so when we write **`url = pyqrcode.create(user_url)`**, our **`.create()`** function will create the QR for the url given by the user. Then **`.png()`** function will generate the **`.png`** file and save it with the filename given by the user.

<!-- LICENSE -->

## License

Distributed under the MIT License. See **`LICENSE.md`** for more information.

<!-- CONTACT -->

## Contact

Avinaba Bera

[![Twitter][twitter-shield]][twitter-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LINKS -->

## Project Links

[![Github][github-shield]][github-url]

<!-- MARKDOWNS -->

[python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/downloads

[pycharm-shield]: https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green
[pycharm-url]: https://www.jetbrains.com/pycharm/download/#section=windows

[visual studio code-shield]: https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white
[visual studio code-url]: https://code.visualstudio.com/download

[twitter-shield]: https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white
[twitter-url]: https://twitter.com/IainSchneider

[linkedin-shield]: https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://www.linkedin.com/in/avinaba-bera

[github-shield]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-url]: https://github.com/avimax37/qr-generator-python
