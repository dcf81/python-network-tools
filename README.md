# Python Network Tools

A collection of lightweight Python utilities for network administration and security testing.

## Python Port Scanner (v2)

`scanner_v2.py` is a TCP port scanner that checks for open ports across user-defined IP targets and port ranges.

### Features
* Custom target entry (IP addresses or domain names)
* Dynamic port range selection
* Clean output filtering for active open ports
* Error handling for interrupted scans and invalid hosts

### Usage

Run the scanner directly from the terminal:

```bash
python3 scanner_v2.py


## Banner Grabber

`banner_grabber.py` connects to an open port on a target IP and extracts the service's identification banner (software type and version).

### Usage

```bash
python3 banner_grabber.py

Enter target IP address: 127.0.0.1
Enter port number: 22

[+] Banner from 127.0.0.1:22 -> SSH-2.0-OpenSSH_10.2p1 Ubuntu-2ubuntu3.5


## Astrophysics Distance Converter

`astro_calc.py` converts astronomical light-travel distances (light-minutes, light-hours, light-days, light-weeks, light-months, and light-years) into formatted distances in miles.

### Usage

```bash
python3 astro_calc.py

--- Astrophysics Distance Converter ---
1. Light-Minutes (e.g., Sun, Inner Planets)
2. Light-Hours   (e.g., Saturn, Pluto, Voyager 1)
3. Light-Days    (e.g., Oort Cloud edge)
4. Light-Weeks   (e.g., Inner Oort Cloud boundary)
5. Light-Months  (e.g., Outer Oort Cloud boundary)
6. Light-Years   (e.g., Stars and Galaxies)

Select conversion type (1-6): 3
Enter distance in Light-Days: 1

[+] 1.0 Light-Days = 16,094,764,800.00 Miles


