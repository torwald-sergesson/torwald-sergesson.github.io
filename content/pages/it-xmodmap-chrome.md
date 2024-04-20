---
title: Make Chromebook Super_L key Control 
slug: xmodmap-chromebook
categories:
- IT
tags:
- shell
- linux
- xmodmap
- chromebook
---

```shell
➜  ~ xmodmap
xmodmap:  up to 3 keys per modifier, (keycodes in parentheses):

shift       Shift_L (0x32),  Shift_R (0x3e)
lock        Caps_Lock (0x42)
control     Control_L (0x25),  Control_R (0x69)
mod1        Alt_L (0x40),  Alt_R (0x6c),  Meta_L (0xcd)
mod2        Num_Lock (0x4d)
mod3
mod4        Super_L (0x85),  Super_L (0xce),  Hyper_L (0xcf)
mod5        ISO_Level3_Shift (0x5c),  Mode_switch (0xcb)
```

Copy current xmodmap config:

```shell
xmodmap -pke > ~/.xmodmap
```

Do its backup just in case

```shell
cp ~/.xmodmap ~/.xmodmap.bak
```

Drop `Super_L` from `mod4`:

```shell
xmodmap -e "remove mod4 = Super_L"
```

And add it to Control:

```shell
xmodmap -e "add Control = Super_L"
```

As a result:

```shell
➜  ~ xmodmap
xmodmap:  up to 4 keys per modifier, (keycodes in parentheses):

shift       Shift_L (0x32),  Shift_R (0x3e)
lock        Caps_Lock (0x42)
control     Control_L (0x25),  Control_R (0x69),  Super_L (0x85),  Super_L (0xce)
mod1        Alt_L (0x40),  Alt_R (0x6c),  Meta_L (0xcd)
mod2        Num_Lock (0x4d)
mod3
mod4        Hyper_L (0xcf)
mod5        ISO_Level3_Shift (0x5c),  Mode_switch (0xcb)
```

After this your `Super_L` button will work as Control.

Don't forget to update .xmodmap config in your $HOME folder:

```shell
xmodmap -pke > ~/.xmodmap
```

