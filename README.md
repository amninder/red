# Red (Under development)#
------
Red is Git utility tool for using all custom aliases in Vim. It requires [tpope/vim-fugitive](https://github.com/tpope/vim-fugitive).
* Maps all the aliases in `.gitconfig` to Leader.
* Runs on top of Fugitive.

## Installation ##

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/amninder/red ~/.vim/bundle/red`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Bundle 'https://github.com/amninder/red'` to .vimrc
  - Run `:BundleInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/amninder/red'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/amninder/red'` to .vimrc
  - Run `:PlugInstall`

## Usage ##
```vim
<Leader>g{alias} :Git {alias} <CR>
```
