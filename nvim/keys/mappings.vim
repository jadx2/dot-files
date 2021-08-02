"Moving Command
nnoremap <leader>j :m .+2<CR>==
nnoremap <leader>k :m .-2<CR>==
vnoremap <leader>j :m '>+1<CR>gv=gv
vnoremap <leader>k :m '<-2<CR>gv=gv

" Save and Quit
map <C-s> :w<CR>
map <C-Q> :q!<CR>

" Move by block of code
map <S-k> {
map <S-J> }

" Folding
augroup OpenAllFoldsOnFileOpen
 autocmd!
 autocmd BufRead * normal zR
augroup END
map <C-z> za

" Window switching
map <C-h> <C-w>h
map <C-j> <C-w>j
map <C-k> <C-w>k
map <C-l> <C-w>l

" NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
map <C-t> :NERDTreeToggle<CR>

""FzF
map <C-p> :Files<CR>

" Autocomment
map <C-c> gcc
map <leader>c gc

" Remove last searched pattern
nnoremap <CR> :noh<CR><CR>

