OP-TEE GDB plugin
=================
Plugin to be used with OP-TEE setups (*) as described at:
https://github.com/OP-TEE/build

1. Source / Download
   $ wget https://raw.githubusercontent.com/Jyx/configs/master/gdb-optee.py


2. Pre-reqs
   $ export OPTEE_PROJ_PATH="<where I've stored my build.git repo forest>"

   Example for my QEMU v7 forest
   $ export OPTEE_PROJ_PATH="/home/jbech/devel/optee_projects/qemu"

   Ensure that you know what the load address is (you'll find that address by
   running the TA once and read the secure side UART. Note that you need to add
   0x20 to that address to point to the .text segment).
   $ export TA_LOAD_ADDR="0x10d020"


3. Run / Debug
   There is a slight difference between host application and firmware.


3.1 Firmware (TEE core, TA, Linux, TF-A, U-Boot)
    In this example we load a TA, it's the same procedure for TEE core, linux, TF-A ...

    Shell 1 - QEMU:
      a) In build.git: ln -s ../toolchains/aarch32/bin/arm-linux-gnueabihf-gdb gdb
      b) make run
      c) At the prompt "(qemu) " do nothing!

    Shell 2 - gdb:
      a) Still in build.git
      b) ./gdb -q
      c) (gdb) source gdb-optee.py
      d) (gdb) connect
      e) (gdb) load_ta <name_of_ta> # tab completion works
      f) (gdb) c


3.2 Host application (xtest, hello_world, hotp etc ...)
    In this example we load xtest

    Shell 1 - QEMU:
      a) In build.git: ln -s ../toolchains/aarch32/bin/arm-linux-gnueabihf-gdb gdb
      b) make GDBSERVER=y run
      c) (qemu) c

    Shell 2 - Normal world UART:
      a) Wait until you see "buildroot login: "
      b) buildroot login: root
      c) # gdbserver :12345 xtest

    Shell 3 - gdb:
      a) In build.git
      b) ./gdb -q
      c) (gdb) source gdb-optee.py
      e) (gdb) load_host <name_of_host> # tab completion works, use xtest
      d) (gdb) connect gdbserver
      f) (gdb) c



(*) Hardcoded path to sysroot, so in "host" application it will only work with AArch32 compiler. Fix for this will come later.
