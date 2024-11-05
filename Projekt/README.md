# Hacker Toolbox
This is a collection of some scripts that could be used for penetration testing purposes.
All the modules/tools in the toolbox could be used stand-alone and are described more in detail down below.

Hacker Tools are a terminal based application that presents a main menu from whitch a user could start the other modules.

### List of tools:
- **Crypto Tool:** A tool to encrypt and decrypt a file with a existing or newly created key.
- **Key Genereator:** Used by the Crypto Tool to generate new keys. Can be run stand-alone but isn't part of the Hacker Tool menu.
- **Domenus:** Subdomain enumerator using the Sublist3r-module.
- **WebGetter:** Download/copy webpages and all their assets to manipulate them or jsut run them locally.
- **Smuggler:** This tool takes a binary payload and hides it in a HTML file so that the payload could hopefully get past some defences.

## Installation
Hacker Tools are developed and tested in a python virtual environment (venv).

1. Clone the project.
2. cd into project directory.
3. Install dependencies.
```bash
pip install -r /path/to/requirements.txt
```
4. Start Hacker Tools
```bash
python hacker_tools.py
```
or run independent tools
```bash
python toolbox/[nameoftool].py [OPTIONS]
```
### All tools are dependent on "toolbox/args.py" to be able to run from Hacker_Tool menu.

## For futher development
To add a tool to Hacker Tools, you need to follow convention with classes in args for all options the module has when running independantly.

Then a function is declared with the same name as the module. This function is then called from the Hacker Tool main script.

First thing to improve for code quality, use args for when running scripts stand alone too. The solution in place was implemented after the first scripts was created with argparse in mind.

Args are used for some validation of the input from the user and should be in place when running stand alone as well.

# Key Generator
A small script to generate a key file to be used to encrypt/decrypt files with.

### Usage:
No arguments needed to run this script.

#### Example:
- To create a new key:
```bash
python key_generator.py
```

# Crypto Tool
Dependency: key_generator.py

Crypto Tool can encrypt any file for you. It will do so by generating a key for you that is then used to encrypt the choosen file. This key could also be used to decrypt files encrypted with it, so don't loose it.

### Usage:
When running the crypto tool as a stand alone some arguments is needed.
Default arguments are optional to add.

|Short Form|Long Form|Required|Description|
|---|---|---|---|
|-f|--file| Yes|The file to encrypt or decrypt.|
|-nk|--newkey|No (Default)|Generate a new key. Default mode if own key isn't provided.|
|-k|--key|No|A key file that could be used to encrypt another file with instead of creating aa new.|
|-e|--encrypt|No (Default)|To encrypt a file. Default mode if decryptkey isn't provided.|
|-dk|--decryptkey|No|The key file used to decrypt an encrypted file with.|
|-h|--help|No| List all arguments.|

#### Examples:
- To encrypt a file with a new key:
```bash
python crypto_tool.py -f test.txt
```
- To encrypt a file with a existing key:
```bash
python crypto_tool.py -f test.txt -k secret.key
```
- To decrypt a file:
```bash
python crypto_tool.py -f test.txt.enc -dk secret.key
```

# DomEnus
A domain enumerator using Sublist3r.
By using multiple search engines Domenus searches for subdomains connected to a specific domain. This is helpful when looking for admin portals, login sites, dev pages etc. when doing a security assessment of a domain.

**Known limitations:**
- Sublist3r bruteforcing isn't used in this module.
- All engines in Sublist3r are used and can't be disabled.

### Usage:
|Short Form|Long Form|Required|Description|
|---|---|---|---|
|-d|--domain|Yes|The domain to enumerate.|
|-fe|--filterExclude|No|Filter out subdomains that appears in comma separated wordlist|
|-fi|--filterInclude|No|Filter out subdomains that isn't present in comma separated wordlist|
|-p|--ports|No|Add comma separated list of ports that will be checked.|
|-s|--silent|No|Set for turning on silent mode.|
|-t|--threads|No|Number of threads to use. Default is 10|
|-v|--verbose|No|Set to turn on verbose mode.|
|-h|--help|No|List all arguments.|

#### Examples:
- Enumerate example.com with 20 threads:
```bash
python domenus.py -d example.com -t 20
```
- Enumerate -with minimal output, silent mode:
```bash
python domenus.py -d example.com -s
```
- Enumerating and serching for specific ports with verbose mode.
```bash
python domenus.py -d example.com -v -p 80,443
```
- Filter out www and blog from subdomains.
```bash
python domenus.py -d example.com -fe "www, blog"
```
- Filter out everything that isn't www or blog from subdomains.
```bash
python domenus.py -d example.com -fi "www, blog"
```
#### !OBS! Exlude has priority, so if both flags are present, the app will only exclude the subdomains !OBS!

# WebGetter
Using requests and BeutifulSoup WebGetter copies a webpage and rewrites all ```<img>,<link>,<script>``` so that src and href attributes points to a local downloaded folder. This is so that the page should copy look and some functionality when running offline.

### Usage:
|Short Form|Long Form|Required|Description|
|---|---|---|---|
|-u|--url|Yes|The URL pointing to the webpage to download|
|-n|--name|No|Name the page and asset folder|
|-h|--help|No|List all arguments.|

### Examples:
- To download/copy a webpage.
```bash
python webgetter.py -u https://webscraper.io/test-sites/e-commerce/allinone
```

# Smuggler
By using BeutifulSoup Smuggler adds javascript to a HTML file and makes it donwloadable.
We could make it so that the downlaod popsup after "the target" has entered the page or pressed a button.

When a modified HTML is create it can be tested by serving it via a webserver, like Live server plugin in vscode.

**!OBS!** Only been tested with the code in the payload folder both on Linux and Windows (Compiled with gcc for Linux or x86_64-w64-mingw32-gcc for Windows)**!OBS!**

**Known limitations:**
- Can't change the delay of the autmatic download.
- Both automatic and "active" download can't be used simultaneous
- Can only activate download with tags that has the id attribute. So an id in the html needs to exist and be found (if donwloaded with WebGetter) or an id needs to be set manually before running the smuggler.

### Usage:
|Short Form|Long Form|Required|Description|
|---|---|---|---|
|-p|--payload|Yes|The payload to get hidden in the HTML.|
|-hf|--htmlfile|Yes|The html to put the payload into.|
|-dn|--downloadname|No|What the downloaded file is named  when downloaded. Default: setup.exe
|-did|--downloadtagid|No|If the target should press any tag(s) to download the payload, enter the id of the tag(s). (Preferably a button or anchor tag)
|-h|--help|No|List all arguments.|


### Examples:
- Hide payload.exe in smuggler_index.html and make the download happen automatically.
```bash
python smuggler.py -p payload.exe -hf smuggler_index.html
```
- Name the payload FreeMoney.exe
```bash
python smuggler.py -p payload.exe -hf smuggler_index.html -dn FreeMoney.exe
```
- To dowwnload the payload, have "the target" press a tag that has the id attribute set to "downloadFile".
```bash
python smuggler.py -p payload.exe -hf smuggler_index.html -did downloadFile
```
