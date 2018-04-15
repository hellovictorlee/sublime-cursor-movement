Sublime-cursor-movement
----------

Sublime-cursor-movement is a lightweight package for Sublime Text to quickly move cursor cross through multiple lines with one key binding. The default multiple lines is 5 lines. It's also support select multiple lines with one key binding.

## Installation

In macOS, ```Tools``` > ```Command Palette``` > ```Package Control: Add Repository```, or shortcut ```Shift + command + p```.

In Windows, ```Tools``` > ```Command Palette``` > ```Package Control: Add Repository```, or shortcut ```Shift + command + p```.

Go to ```Package Control: Add Repository```.

<p align='center'>
<img src='/Users/victory2152/GitHub/sublime-cursor-movement/img/img1.png' style='max-width:400px'></img>
</p>

Add repository ```https://github.com/ShuaiHsunLee/sublime-cursor-movement```
<p align='center'>
<img src='/Users/victory2152/GitHub/sublime-cursor-movement/img/img2.png' style='max-width:750px'></img>
</p>

Go to ```Package Control: Install Package```.
<p align='center'>
<img src='/Users/victory2152/GitHub/sublime-cursor-movement/img/img3.png' style='max-width:400px'></img>
</p>

Add package called ```sublime-cursor-movement```.
<p align='center'>
<img src='/Users/victory2152/GitHub/sublime-cursor-movement/img/img4.png' style='max-width:350px'></img>
</p>


## Usage
```alt + up``` : make your cursor move up 5 lines at once

```alt + down``` : make your cursor move down 5 lines at once

```shift + alt + up``` : select 5 lines upward at once

```shift + alt + down``` : select 5 lines downward at once

## Customization

Go to ```Preference``` > ```Key Bindings```.

Add codes below into it.

```
{ "keys": ["alt+up"], "command": "multi_up", "args": {"nlines": 5} },

{ "keys": ["alt+down"], "command": "multi_down", "args": {"nlines": 5} },

{ "keys": ["shift+alt+up"], "command": "multi_up_select", "args": {"nlines": 5} },

{ "keys": ["shift+alt+down"], "command": "multi_down_select", "args": {"nlines": 5} }
```

The default is 5, you can go with any number.