---
title: Vim config files
slug: vim-configs 
categories:
- Dev
tags:
- shell
- linux
- vim
- config
---

```
set number

set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'


" ----------============ Code/project navigation =============-----------
" plugin on GitHub repo
Plugin 'scrooloose/nerdtree' 		" Project and file navigation
Plugin 'majutsushi/tagbar'   		" Class/module browser

" ----------============ Other  =============-----------
Plugin 'bling/vim-airline'         	" Lean & mean status/tabline for vim
Plugin 'fisadev/FixedTaskList.vim' 	" Pending tasks list
Plugin 'rosenfeld/conque-term'  	" Consoles as buffers
Plugin 'tpope/vim-surround'        	" Parentheses, brackets, quotes, XML tags, and more
Plugin 'flazz/vim-colorschemes'		" Colorschemes

" ----------============ Snippets support =============-----------
Plugin 'garbas/vim-snipmate'		" Snippets manager
Plugin 'MarcWeber/vim-addon-mw-utils'	" dependentcies #1
Plugin 'tomtom/tlib_vim'		" dependentcies #2
Plugin 'honza/vim-snippets'		" snippets repo

" ----------============ Languages support =============-----------
Plugin 'klen/python-mode'		" Python mode (docs, refactor, lints, highlighting, run and ipdb and more
Plugin 'davidhalter/jedi-vim'		" Jedi-vim autocomplete plugin
Plugin 'mitsuhiko/vim-jinja'		" Jinja support for vim 
Plugin 'mitsuhiko/vim-python-combined'	" Combined Python 2/3 for Vim
Plugin 'fatih/vim-go'
" Plugin 'Shougo/neocomplete.vim'

Plugin 'tpope/vim-fugitive'
call vundle#end()
" filetype plugin indent on " required 
" filetype on
" filetype plugin on
filetype plugin indent on

set backspace=indent,eol,start
aunmenu Help.
aunmenu Window.
let no_buffers_menu=1
set mousemodel=popup

set ruler
set completeopt-=preview
set gcr=a:blinkon0
if has("gui_running")
	set cursorline
endif
set ttyfast

" highligh
syntax on
if has("gui_running")
	" GUI? set theme and size of window
	set lines=50 columns=125
	coloscheme molokai
	"" NERDTree
	autocmd vimenter * TagbarToggle
	autocmd vimenter * NERDTree
	autocmd vimenter * if !argc() | NERDTree | endif

	" vim MacOS X
	if has("mac")
		set guifont=Consolas:h13
		set guoptions=maxvert,maxhorz
	else
		" default GUI
		set guifont=Ubuntu\ Mono\ derivative\ Powerline\ 10
	endif
else
	" terms?
	" coloscheme myterm
	" colorscheme 3dglasses
	" colorscheme campfire
    " colorscheme zenburn
    " colorscheme railscasts
	" colorscheme ChocolateLiquor
    colorscheme 256_noir
    " colorscheme MountainDew
    " colorscheme vividchalk
    " colorscheme 0x7A69_dark
    " colorscheme CodeFactoryv3 
     colorscheme 256-jungle
    " colorscheme adam
    " colorscheme Monokai
    " colorscheme gentooish
    colorscheme 1989
    " colorscheme monoacc
    " colorscheme material
endif

tab sball
set switchbuf=useopen

" disable beeper
set visualbell t_vb=
set novisualbell

set enc=utf-8
set ls=2
set incsearch
set hlsearch
set nu
set scrolloff=5

set nobackup
set nowritebackup
set noswapfile

" hide panels
set guioptions-=m " menu
set guioptions-=T " toolbar
set guioptions-=r " scrollbar

" tab settings
set smarttab
set tabstop=4
set shiftwidth=4
set expandtab
set softtabstop=4

augroup vimrc_autocmds
	autocmd!
	autocmd FileType ruby,python,javascript,c,cpp highlight Excess ctermbg=DarkGrey guibg=Black
	autocmd FileType ruby,python,javascript,c,cpp match Excess /\%80v.*/
	autocmd FileType ruby,python,javascript,c,cpp set nowrap
augroup END

" set directory with SnipMate settings
let g:snippets_dir="~/.vim/vim-snippets/snippets"

" set Airline
set laststatus=2
" let g:airline_theme='bubblegum'
" let g:airline_theme='badwolf'
let g:airline_powerline_fonts=1
let g:airline#extensions#tabline#enabled=1
let g:airline#extensions#tabline#formatter = 'unique_tail'

" TagBar settings
map <F4> :TagbarToggle<CR>
let g:tagbar_autofocus = 0 " autofocus on Tagbar when open

" NerdTree settings
" show NERDTree on F3
map <F3> :NERDTreeToggle<CR>
" ignoring file with extention
let NERDTreeIgnore=['\~$', '\.pyc$', '\.pyo$', '\.class$', 'pip-log\.txt$', '\.o$']

" TaskList settings
map <F2> :TaskList<CR> " show list tasks on F2

" Work with buffers
map <C-q> :bd<CR> 

"================================
" Python-mode settings
"=============================
" disable autocomplete on code (between it jedi-vim)
let g:pymode_rope = 0
let g:pymode_rope_completion = 0
let g:pymode_rope_comple_on_dot = 0

" Documents
let g:pymode_doc = 0
let g:pymode_doc_key = 'K'
" check code
let g:pymode_lint = 1
let g:pymode_lint_checker = "pyflakes,pep8"
let g:pymode_lint_ignore = "E501,W601,C0110"
" checking code after saving
let g:pymode_lint_write = 1

" support virtualenv
let g:pymode_virtualenv = 1

" set breakpoints
let g:pymode_breakpoint = 1
let g:pymode_breakpoint_key = '<leader>b'

" highlight synax
let g:pymode_syntax = 1
let g:pymode_syntax_all = 1
let g:pymode_syntax_indent_errors = g:pymode_syntax_all
let g:pymode_syntax_space_errors = g:pymode_syntax_all

" disable autofold on code
let g:pymode_folding = 0

" возможность запускать код
let g:pymode_run = 0

" Disable choose first function/method at autocomplete
let g:jedi#popup_select_first = 0

let &path.="/usr/include,/usr/include/x86_64-linux-gnu"

```
