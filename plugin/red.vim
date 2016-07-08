" vi: ft=vim
" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
function! GetGitAlias()
python << endOfPython

from red import get_alias

for alias in get_alias():
    vim.command('nnoremap <Leader>g{alias} :Git {alias}<CR>'.format(
        alias=alias
    ))
endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
"command! -nargs=1 GetGitAlias call GetGitAlias(<f-args>)
command! GetGitAlias call GetGitAlias()
