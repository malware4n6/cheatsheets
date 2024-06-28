# WSL

```sh
sudo apt install linux-image-extra-virtual
```

Edit `/etc/default/grub`

```sh
# add at the end of the line starting with
GRUB_CMDLINE_LINUX_DEFAULT="quiet..."
# this option:
video=hyperv_fb:3840x2160 
```

```sh
sudo update-grub
```

```powershell
set-vmvideo $vmname -horizontalres:3840 -verticalres:2160 -resolutiontype:single
# optional
set-vm $vmname -EnhancedSessionTranportType HVSocket
```

Read [Kali blog](https://www.kali.org/docs/virtualization/install-hyper-v-guest-enhanced-session-mode/) for new options.

# Setup

- Git bash
- retoolkit
- wireshark
- Visual Studio Community
- Firefox
- Python3 + pip install *
- windbg
- notepad++

- binja
- ida free
- hiew
