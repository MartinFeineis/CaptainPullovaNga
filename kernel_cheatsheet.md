# Linux Kernel Cheatsheet
## Chapter 1 Surveying the Linux Kernel
### System calls
  About 300 System Calls invoked by standard C library, architecture dependent. On an error system call return _errno_ value (negative), otherwise a posistive number
  Application --> Library --> System Call. Man page section 2 e.g. ```man 2 intro```

### Read messages from the Kernel
  Display messages with ```dmesg```
  Otherwise ```tail -f /var/log/messages ; /var/log/syslog```

### /proc and /sys Filesysytem
  Virtual Filesystems that create their content dynamically when it gets accessed.



## Chapter 2 Booting
  BIOS --> GRUB --> Kernel
  GRUB loads the initial root filesystem and then transfers control over to the kernel. Kernel starts up, with parameters passed over from GRUB.
  ```man -k grub``` Kernel Commandline parameters are in ```/proc/cmdline``` around 500 see and manipulate with ```sysctl -a```


## Chapter 3 Working with loadable Kernel Modules
* ```lsmod``` lists loadable linux kernel modules from ```/lib/modules/`uname -r` ``` 
* ```modinfo``` with a modulename gives information about that modules