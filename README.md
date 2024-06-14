# e-paper_python
 **Department of Computer Science University of York**


  <h6>  Integrating manual to upload images to Wavshare e-paper module.</h6>

<h5>
    By Nirdesh Sagathia, MSc Cyber Security October 19, 2022</h5>



 <h2>   Hardware Requirements</h2>



* Raspberry pi 4 Model B(used), you can choose a newer version after Rpi 3.
* E-paper module: here we used Waveshare 5.65inch e-paper 7-colour ACep Display module(600x448 pixels)
* [Universal e-Paper Raw Panel Driver HAT](https://thepihut.com/products/universal-e-paper-raw-panel-driver-hat?variant=32051318652990&currency=GBP&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gclid=CjwKCAjw-rOaBhA9EiwAUkLV4rikGcrenrVlZKNkQqx6GRbDe0JkMeXggmUC-ms1FglD5GNLHTtFQhoCCM8QAvD_BwE)
* [https://uk.pi-supply.com/products/pijuice-standard](https://uk.pi-supply.com/products/pijuice-standard) ( If you want to run RPi over a portable power supply - Access the remote connection via WiFi over a laptop for input and output)

<h2>Software Requirement</h2>




* [https://www.waveshare.com/wiki/5.65inch_e-Paper_Module_(F)](https://www.waveshare.com/wiki/5.65inch_e-Paper_Module_(F)) (manual available for waveshare e-paper module)
* [https://cloudconvert.com/bmp-converter](https://cloudconvert.com/bmp-converter) (To convert the images into BMP format with 600x448 pixels)
* VNC viewer on laptop and on RPi.
* [https://github.com/waveshare/e-Pape](https://github.com/waveshare/e-Paper)<span style="text-decoration:underline;">r </span>(Python code used from an example in a given repository)

<h2>Details</h2>




* Enable SSH, VNC and SPI connection from <code><em>raspi-config </em></code>command.</strong>
* Install BCM2835 libraries:

    ```
    wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.71.tar.gz tar zxvf bcm2835-1.71.tar.gz
    cd bcm2835-1.71/
    sudo ./configure && sudo make && sudo make check && sudo make install
    ```


* Install WiringPi libraries:

    ```
    git clone
    cd WiringPi
    ./build
    gpio -v
    ```



* Install Python3 libraries:


    ```
    sudo apt-get update
    sudo apt-get install python3-pip sudo apt-get install python3-pil sudo pip3 install RPi.GPIO
    sudo pip3 install spidev

    ```








 * Convert any image format to BMP



```
Go to https://cloudconvert.com/bmp-converter
Upload your image and set the options for Width and Height( i.e. 600x448 pixels).
Download it and save and send it to RPi storage via any medium (USB or VNC file transfer or any other method)
```



* Download the executable GUI application from [https://github.com/mark-nirdesh/e-paper_python](https://github.com/mark-nirdesh/e-paper_python)


```
Extract the folder. Go to the dist folder. Open run_me.
Select your desired image(Converted in the above step). Wait till the process is complete.
Hurray!! image is on the colour e-paper module.
```

<h3>Overview of intergration</h3>

<ol>
<li>GUI to upload image on e-paper module of waveshare 5.65inch e-paper module</li>
<li> Go to dist to open the GUI on linux(Rpi).</li>
<li>Select your desire image and upload it on the e-paper module</li>
<li>You can make your custom code for different waveshare e-paper modules.</li>
<li>All codes used are from https://github.com/waveshare/e-Paper</li> 
</ol>
