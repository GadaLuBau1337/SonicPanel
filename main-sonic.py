
import base64,zlib,hashlib,sys,os

if hasattr(sys,'gettrace') and sys.gettrace():
    os._exit(1)

MfLxNfms = b'76WTUwOolKgwSHfyhtgI2ieLfIF5auoO8FqBkMCbC2meLT3vfXeKbapeelITxwwsNA5G+5CcNMdU/s74WDOiqWPLT7nXIlwao12i1JGGlVJwZ2gIf112aeLNjMptof3Ef5/zO/PndL+J5+1bRhK4Kz/q1nDqQ1S8R529Uj7p/eQxuZ0SGxJIpHcHofj2mrjcn4RY93WJWdl6arjtPuMP9cqYrTqC1OPFKqOIYBpmT8sgSd5slbtXwRP6nlbBYidO0p61ne2/D9sdgmT1mfdjTFdmeiNBDavvGIk8C3Z38leOab1sA/Dj1SDw4YusyYWsGNF2F9V0y1da5keBFhxydLpT+5qEmxze1RIX3Hv7I3gc47GYKHSe/EixJO/iR6SegrSoO0jdUiGtR6lduJf1wmN5yQ4+scrKyy4YpirXeMo32PefsHL5nXMJKykUBvi1R/+iaxK77J8xSkfaBvzewDLZ9JWci63hp3QMLM/CAc5DWqj6rZurDvIM+Qt7s2DX2in75VCC7tN84PBWg3bbMfR2JgeW5pUmNU669oZ5p8RdH9h15sZxeiBWnCSsTSc1N7AMO3DbQ81mz3A/CF0Vww80iRXdfqdmFO/GFu8clHrrIa5U+bf99YlriDyWuNmGVpzP5nh9CCEIbVnUmhWcdAZWIrPtaE0e621hvAQtQyb2wibJzPZHsDSYUvAuyAlD3edkEDy6ysJ276GOkPWKlr/5rcwUqGDXn9u+cOe4dZ+12C6/L0O4PaZRJkU3OA9IHdyy5dOPNOOYDAgH8S5aVvPmlGGY0ghMH1jQcXId8IXKFZkoUFeB9M5GGT/oqOXMFJtYkJyzCo9sck4V1/09dBz8DD5NEdFJaufQbQouaYKVkIIWKQnC2sxkxqNsUKV9q/eHA+FVrtELAMhx7Jwr1zogsy1KgWHdRS/5yLfXVs4J3k8A2zVN57wcUNQmWAdcMFfoMN7AQGpBgzdYKfa34z+SduOPRbWGuGu7y0eErOSxKUS10EjnnLUkhXMLaSfeurf8PTHC27CEcyzT5LBLE/+faAkOyL/PCBBd5r0ctIzzhV4swWDdMgwnI48EVWsms74l8TUJY0cGP+7O5+awceEkqM5BsLJaBJX6qRxXSByPO3verLVdfA=='
kbkJcLLs = b'^$l!Wk$E5pW=g*}zFsD~L9so`Q>-Bj{?*b;@hm9v3fwi{18pY!KCM;ZL)pvXFbz7vIb*gpt|!X<_ofru<<Q%dqa9{r*ZHACcZK)X0)93k42qJf*Y8{N3T*I*z|7hujD`&T!d5CIW}Uz@W6hl%a5J_~@1AAQA0<Uh{6a#_F$H9QP9JoWHP>s3ZC-od%5seLY%o7<eLFOA{=0t4w|egd@enm`9F8fRlVbgcDkF$3QMKM{MV4Mq1PEhJm6MbK$$wlMVp=%^9&e2u4vs*22y-Tj7RUA`I(eqI0#}4Q_52TFZUz(yL_(veaNrl4LGxdOuxmFt1VofQ|9OLq%+{bBth?8IZC3Wtpvl!|j#Tg-Be%AkTlf4v)mMli7ft161YMG8fIy=j{XT`f0=!I%d@t1UDrKY(?4!wwOs~G<FQUr8VJn^@(ELI9!FrG>CaCEW229Is-J60qYI=a|U-L33Ei1035OP_nlD8e2A0PQHLho<iX&!B5p{g>QU0aH9+}<`p3KLHtAP|VGom-w9^|TYb=R2xpdXz7>d(mpORR9t{Ltfzh=o9n!zK!MkHD>Bk$G2+9#rjs5!)qCB!ZLl|bsx9?F4I~At%xT$bDa?)9Kv@E*gXgYh?`XM#?&0PZOPtqs{de+?2~6JJlnGYq4<@Fe<y23CYKfel}v!K$8I^rpUA^{D|y24qd+i-uBr>v<lfZ~CPn9eiBNDl;^ks4%MND`rxNw+Y<*eJBx*u0@_Bc%kwZ`vla?|n<y*%3dM~e2P+f2^tYPV{;7>h)j1I0`f+g-QkR+Xti}hkyc-}E(VTb~LnhKBm)LQ^We|*F#b;a3;TX|R?K){50SM3veF<#q)+(%;TC!hujHVmak!hrizx~p>4u)kpi#U2ES|2f0^*-DSN*Og2cenV6l1C7$EGoVw8nTZI)*Q<_4O^wNR`j$IR0w<(JEX?bHv}^jkdB8FV7#vN=+#r_91ri`#gz<I(j6`f3VK0P)bL<d{6xNNzQ9jvn|24mKEW!H9QVLG{;Qn<l{R;^{cKnHJ1LRs3^Sa_D)YzF2W{qYCD3}<JA)ErQ9u%4%v&^j)ZszfZmau#Gq5'
PhAnlbeq = b'PKNiDaWpXGk8pWcnBSRz7zBE+TGdJrNSuTYwfIb3T5C+oMtT8EaeE/Skaf+WQcT9e4LNcFUYP1qpUsoBKElop3XsT0PCfInuU0enQUir2G85P456lCY8UfXMfmSh/Z6vhScr6v3WgRUIIukBD24CC/Tlh1+E7H1dU0NnUR6Yj48LbqZCxuFVDYnZOWw2n0cAxkdyJiy7mD3h47yA+rMXty+9NPIGKvOI86w88zlp2DZ7C/tc3NpHhzIXwNwJYlKmfEf8KJzNLJh3XHncfWmYksgf5F6CLtMYvaCBKvjmUpjp978Q8rZel+MNhU33uv+P7uugZhd0DgWasJKjlKMnt/VvvL/rduD9Eh9bUWo79/o2sVbjUV/ujaOvOo6jjC3dDHLxXLFQWm5o/ueFHKQOdvJCQsJBpbheyRCsbAEcQZY4LVVnnpQMaY6ACvz2pVScTWG6foCbo0RInSqIjTSnamKymwg1Xrip0uVE4LQ/GO17d0euTU/QWpEMP0fMgq1BnGbdkKscW//ZS7ylmImyNJ/bU8eyB4+qxRs0mgLkdDl67zOg5IYk82QGzFW7gbCkyqv4d3mwlx7CF39vKxNfs++3NYsICI0J0vjWK9bA3mnsg7GDcaDvK+wnzJ/msYWEzbdeU9sk5tJoVx44EMd+Kr8ECFbNN9EGVkd0JMa33kt7pKpILVkgbJ3r0bHF5712+se4F8h2pw7ZCOsipkMCclIwmJuSYwUxTxuf8MrAhfbRRCtwtOSULDzW3/IorVKoFhI8rM8hh7S3DQDyQp8vJy0E1ZmRDQ/jtw0NQBJoc2ufnInk002dDESQc4ocYNx5a/0K4Zhi6hYmMRK03CYBdCRr72TcH+ye0GC5a/f1RqyD9i04NlT4xw55/RS1TtQEODQLwCXgpnKd/finj1S/JfR22Ue5gSC0S4fWWG6aqM90GgDunW45zoG81wSj15P6u11gZTTQ1fw+a8vFsuC05CUDj/JgW6JCrtyuMq6I3fcVr+0X9cPjALVbE77xJYBYjNK58uwb/doJkjeke2v8dw6dZYojwDwBSLuL0WasTR1aEkN9Czmt5g2JHrbiLxL/mdXlfMvQCt1P8VjCZCWeMifQvlbvEiQa9NroMN248zG372kmwQvF0+8='
hZwxXXyw = "4cbb6c42c02eaf46a4de10274c660b08e97f9642e3b5769de6f33409419a5a75"

if hashlib.sha256(MfLxNfms+kbkJcLLs+PhAnlbeq).hexdigest() != hZwxXXyw:
    os._exit(1)

_seed = "".join(["UL","TRA","DY","NAM","IC","KEY"])
_k = hashlib.sha256(_seed.encode()).digest()

_part1 = base64.b64decode(MfLxNfms)
_part2 = base64.b85decode(kbkJcLLs)
_part3 = base64.b64decode(PhAnlbeq)

_payload = _part1 + _part2 + _part3

_dec = bytes([b ^ _k[i % len(_k)] for i,b in enumerate(_payload)])

exec(zlib.decompress(_dec))
