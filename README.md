# one-time-pad - otp
Python implementation of One-time pad cipher which a type of Vignere cipher which is an unbreakable cipher .

use otp from command line in \*nix systems

#### Help Menu :

command ran : ***$ otp -h***

![Help Menu](https://github.com/snehilk1312/one-time-pad/blob/main/output-screenshots/01_help_menu.png?raw=true)


#### Encrypt a String

command ran : ***$  otp -e "encrypt this string"***


![Encrypting a string](https://github.com/snehilk1312/one-time-pad/blob/main/output-screenshots/02_encrypt%20string.png?raw=true)

The output ciphertext will be ***cipher.txt*** and key will be ***key.txt*** in working directory  .




#### Encrypt a File

command ran : ***$  otp -f "filename.ext"***


![Encrypting a File](https://github.com/snehilk1312/one-time-pad/blob/main/output-screenshots/03_encrypt_file.png?raw=true)

The output ciphertext will be ***cipher.txt*** and key will be ***key.txt*** in working directory  .




#### Decrypt a String or File

command ran : ***$  otp -d cipher.txt -k key.txt***

![Decrypting a file or string](https://github.com/snehilk1312/one-time-pad/blob/main/output-screenshots/04_decode.png?raw=true)

The output plaintext will be ***plaintext.txt*** in working directory  .




## For \*nix systems: 

### To run this code from anywhere in terminal, do as follows:



#### 1. git clone https://github.com/snehilk1312/one-time-pad.git

#### 2. cd one-time-pad/one-time-pad/

#### 3. To run from anywhere in terminal , In home directory : mkdir myPythonScripts

#### 4. In .bashrc(if you are in bash) file, add : export PATH="$PATH:/home/user/myPythonScripts"

#### 6. source ~/.bashrc

#### 7. cd myPythonScripts

#### 8. move "otp" to myPythonScripts: mv ~/one-time-pad/one-time-pad/otp ~/myPythonScripts/otp

#### 9. chmod +x urdi



Upon doing above steps we can run "otp" as any similar Linux command line commands(as "cd" , "pwd" , "ls"), with various arguments . 


