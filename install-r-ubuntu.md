### Add line to /etc/apt/sources.list
```
sudo echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | sudo tee -a /etc/apt/sources.list
```
### Get and export key
```
gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
gpg -a --export E084DAB9 | sudo apt-key add -
  ```
### Update and install r base
```
sudo apt-get update
sudo apt-get install r-base r-base-dev
```
### Install rstudio
Remember to change to current version
```
sudo apt-get install gdebi-core
wget https://download1.rstudio.org/rstudio-xenial-1.0.153-amd64.deb
sudo gdebi -n rstudio-xenial-1.0.153-amd64.deb
rm rstudio-xenial-1.0.153-amd64.deb
```
