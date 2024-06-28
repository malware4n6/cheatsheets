# Linux Q&A

- Problem: vs code is set as the default explorer
- Solution: create the file ~/.config/mimeapps.list if necessary:

```text
[Default Applications]
inode/directory = org.gnome.Nautilus.desktop
```

- Crash i3 / Ubuntu
```sh
# try to detect problems
journalctl -b -1 -e

# try to disable some of them caused by flatpack
systemctl --user stop xdg-desktop-portal{,-gtk}
systemctl --user disable xdg-desktop-portal{,-gtk}
```


----

# IP

```bash
sudo ip addr add 192.168.10.1/24 dev eth0
sudo ip link set eth0 up
sudo ip route add default via 192.168.10.254
sudo ip route add 192.168.20.0/24 via 192.168.10.254 dev eth0
```

[https://www.cyberciti.biz/faq/ip-route-add-network-command-for-linux-explained/](https://www.cyberciti.biz/faq/ip-route-add-network-command-for-linux-explained/)

----

# xrandr

```bash
xrandr --listmonitors
xrandr --listactivemonitors
xrandr --output HDMI-1 --auto (--above | --below | --right-of) eDP1
xrandr --output eDP1 --mode 800x600
xrandr --output HDMI-1 --same-as eDP1
```

----

# Quick setup

```bash
sudo apt install git tmux vim htop tree zsh fonts-powerline terminator python3-pip python3-venv wget curl less rlwrap
sudo apt install gcc binutils clang g++ gdb gdb-multiarch gdbserver python3-dev
sudo apt install wireshark socat netcat-traditional openssh-server inetsim
sudo apt install qemu-user qemu-system-common qemu-system-arm
sudo apt install qemu-system-mips
```

```bash
python3 -m pip install -U pip
pip install wheel
pip install ipython jupyter mkdocs
pip install pylint black
pip install pyscaffold
pip install prettyprint rich
pip install numpy pandas
pip install construct
pip install scapy
pip install flask
pip install networkx pyvis
pip install pefile lief capstone unicorn qiling angr pyew miasm
pip install libtmux yara-python
pip install frida frida-tools
pip install jq
```

## Malware analysis

- capa + rules:
    ```sh
sudo mkdir /tools
sudo chown -R $USER:$USER /tools
cd /tools
git clone https://github.com/mandiant/capa.git
git clone https://github.com/mandiant/capa-rules.git
```
- binary ninja
- IDA Free
- malcat
- [docker](https://docs.docker.com/engine/install/ubuntu/)
- [floss](https://github.com/mandiant/flare-floss)
- [gdb-gef](https://github.com/hugsy/gef)
- yara + yarac
- rizin/r2
- [openjdk / jre](https://adoptopenjdk.net/releases.html)

## Development

- [delta: A syntax-highlighting pager for git, diff, and grep output](https://github.com/dandavison/delta)
- [batcat](https://github.com/sharkdp/bat)
