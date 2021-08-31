let g:mapleader=" "
syntax enable			"syntax on
set hlsearch 			"highlight searched patterns
set incsearch			"highlight patterns while typing
set ruler			"show cursor position
set autoindent			"Indentation
set smartindent			"makes indenting smart
set foldmethod=indent "folding method
set number			"line number
set relativenumber  "relative number
set mouse=a			"enable mouse
set cursorline			"Enable higlith of the current line
set clipboard^=unnamed,unnamedplus	"copy from nvim to anywhere
set formatoptions-=cro		"avoid next line comment after comment
set splitright			"vertical split will be to the right
set tabstop=2			"insert 2 space for tab
set softtabstop=2 "for correct tab detection
set shiftwidth=2		"Change number of space characters inserted for indentation
set smarttab			"makes tabbing smarter
set expandtab			"convert tabs to spaces
set laststatus=0		"always show status line
set background=dark		"set the background tonality
set showtabline=2		"always show tabs
set ignorecase      "ignore case in patterns
set smartcase       "Detects by casing
set t_Co=256        "accept 256 colors
set nobackup                            " This is recommended by coc
set nowritebackup                       " This is recommended by coc
set updatetime=300                      " Faster completion
set timeoutlen=500                      " By default timeoutlen is 1000 ms
set termguicolors

let g:indent_guides_enable_on_vim_startup = 1 "indent guides on

" Center screen when inserting
autocmd InsertEnter * norm zz

"Ruby formatter
let g:rufo_auto_formatting = 1

au! BufWritePost $MYVIMRC source % "autosource nvim
