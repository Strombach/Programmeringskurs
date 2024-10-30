# Toolbox

All the modules/tools in the toolbox could be used stand-alone.

### Key Generator
A samll script to generate a key file to be used to encrypt/decrypt files with.

#### Example:
- To create a new key:
```bash
python key_generator.py
```

### Crypto Tool
Dependency: key_generator.py

#### Usage:
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

#### Example:
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

### DomEnus
A domain enumerator.

|Short Form|Long Form|Required|Description|
|---|---|---|---|
|-d|--domain|Yes|The domain to enumerate.|
|-p|--ports|No|Add comma separated list of ports that will be checked.|
|-s|--silent|No|Set for turning on silent mode.|
|-t|--threads|No|Number of threads to use. Default is 10|
|-v|--verbose|No|Set to turn on verbose mode.|
|-h|--help|No|List all arguments.|

#### Example:
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

### Assignment
Bygg en toolbox bestående av flera Python-script som kan användas för penetrationstester eller inom IT-säkerhet.

Använd dig av de tekniker och paket som vi gått igenom under kursen eller kunskap du har sedan tidigare.


#### Krav för varje verktyg:
Verktyget ska använda minst ett externt Python-bibliotek (t.ex. requests, shodan, cryptography, scapy, nmap osv).

Verktyget ska använda argparse och kunna köras med argument från terminalen (undantag om verktyget inte behöver ta någon input från användaren)

Verktyget ska innehålla en README-fil med instruktioner om hur verktyget används, exempelkörningar och kända begränsningar.

#### För Godkänt krävs:
Minst tre verktyg från olika kategorier (viktigt: Du får använda dina verktyg från laborationerna. Men se till att de följer kraven för uppgiften)

Verktygen ska innehålla tydliga instruktioner för användning

Koden ska innehålla grundläggande felhantering (t.ex. try-except), inmatningsvalidering och vara strukturerad i funktioner.


#### För Väl godkänt:
Inkludera ytterligare/mer avancerade funktioner såsom logging, rapportgenerering eller ett mainscript som importerar de andra skripten och interaktivt låter användaren köra dem

Implementera fler än tre verktyg för att visa din kunskap av fler Python-paket

Verktygen ska vara väl dokumenterade


Inlämning:
Lägg upp allting i ett Github repo. Skapa antingen en readme fil för varje verktyg (separera med folders) eller en readme med alla verktyg listade.

Se till att repot är public (eller bjud in mig om du vill hålla det privat) och lämna länken som inlämning.
