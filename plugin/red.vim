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

print get_alias()

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! GetGitAlias call GetGitAlias()
