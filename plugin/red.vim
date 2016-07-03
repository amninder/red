" vi: ft=vim

command GitConfigExists :call GitConfigExists()

function! GitConfigExists()
    if exists('~/.gitconfig')
        echom "gitconfig exists"
    endif
endfunction
