# Write-ups

## Bin

|    Challenge     | Write-ups                    |
| :--------------: | :--------------------------- |
|    block-game    | [writeups](/bin/block-game)       |
|  context-clues   | [writeups](/bin/context-clues)    |
|    going_over    | [writeups](/bin/going_over)       |
|     kangaroo     | [writeups](/bin/kangaroo)         |
|   misdirection   | [writeups](/bin/misdirection)     |
|     patches      | [writeups](/bin/patches)          |
|    symbolism     | [writeups](/bin/symbolism)        |
| win-bin-analysis | [writeups](/bin/win-bin-analysis) |

### Crypto 

|       Challenge       | Write-ups                         |
| :-------------------: | :-------------------------------- |
|  audio-transmission   | [writeups](/crypto/audio-transmission)    |
|   file-zip-cracker    | [writeups](/crypto/file-zip-cracker)      |
| hidden-in-plain-sight | [writeups](/crypto/hidden-in-plain-sight) |
|    inDEStructible     | [writeups](/crypto/inDEStructible)        |
|     new-algorithm     | [writeups](/crypto/new-algorithm)         |
|         salad         | [writeups](/crypto/salad)                 |
|    secret-message     | [writeups](/crypto/secret-message)        |
|   would-you-wordle    | [writeups](/crypto/would-you-wordle)      |
|        xoracle        | [writeups](/crypto/xoracle)               |


### Forensics

|   Challenge    | Write-up                   |
| :------------: | :------------------------- |
| corrupted-file | [writeups](/forensic/corrupted-file) |
|  data-backup   | [writeups](/forensic/data-backup)    |
|    infected    | [writeups](/forensic/infected)       |
| recent-memory  | [writeups](/forensic/recent-memory)  |
| scavenger-hunt | [writeups](/forensic/scavenger-hunt) |
| speedy-at-midi | [writeups](/forensic/speedy-at-midi) |
|  stolen-data   | [writeups](/forensic/stolen-data)    |

## Misc

|     Challenge      | Write-ups                      |
| :----------------: | :----------------------------- |
|    bank-clients    | [writeups](/misc/bank-clients)       |
| check-the-shadows  | [writeups](/misc/check-the-shadows)  |
| dnsmasq-ip-extract | [writeups](/misc/dnsmasq-ip-extract) |
|  filtered-feeders  | [writeups](/misc/filtered-feeders)   |
|   firewall-rules   | [writeups](/misc/firewall-rules)     |
|      root-me       | [writeups](/misc/root-me)            |
|     snort-log      | [writeups](/misc/snort-log)          |
|      we-will       | [writeups](/misc/we-will)            |


## OSINT

|     Challenge      | Write-ups                      |
| :----------------: | :----------------------------- |
|    contributor     | [writeups](/osint/contributor)        |
|      dns-joke      | [writeups](/osint/dns-joke)           |
|      mystery       | [writeups](/osint/mystery)            |
|   photo-op-spot    | [writeups](/osint/photo-op-spot)      |
|       rarity       | [writeups](/osint/rarity)             |
| sho-me-whats-wrong | [writeups](/osint/sho-me-whats-wrong) |


## Web

|     Challenge     | Write-ups                     |
| :---------------: | :---------------------------- |
|    apache-logs    | [writeups](apache-logs)       |
|      buster       | [writeups](buster)            |
|  cookie-factory   | [writeups](cookie-factory)    |
|    flag-vault     | [writeups](flag-vault)        |
| heres-my-password | [writeups](heres-my-password) |
|  road-not-taken   | [writeups](road-not-taken)    |
| seigwards-secrets | [writeups](seigwards-secrets) |


<!-- 
Works in Bash

# Get Challenge Names in Directories and outputs them to file
ls ../{CATEGORY} -l | grep '^d' | awk '{print $9}' | sed 's/.$//' > {CATEGORY}

ex. 
ls ../forensics/ -l | awk '{print $9}' | sed 's/.$//' > forensics

-----

# Get writeup format by category
category={CATEGORY}; while read -r chal; do printf "| [$chal](../$category/$chal) | [writeups]($chal)\n"; done < $category

ex.
category=bin; while read -r chal; do printf "| [$chal](../$category/$chal) | [writeups]($chal)\n"; done < $category

---

# make directory for all challenges
mkdir `cat bin crypto forensics misc osint web`

# add .keep file to all challenges
for dir in `ls -l | grep '^d' | awk '{print $9}'`; do cd $dir; touch .keep; cd ..; done

--> 
