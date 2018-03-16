# Convert file encoding
Tutorial from https://www.tecmint.com/convert-files-to-utf-8-encoding-in-linux/


### Check file encoding 
```
$ file -i file.txt
file.txt: text/plain; charset=iso-8859-1

```
### Check all known encodings
```
$ iconv -l
```
### Syntax to use iconv
```
$ iconv options -f from-encoding -t to-encoding inputfile(s) -o outputfile
```
### Example

```
$ file -i input.file
$ cat input.file 
$ iconv -f ISO-8859-1 -t UTF-8//TRANSLIT input.file -o out.file
$ cat out.file 
$ file -i out.file
```
