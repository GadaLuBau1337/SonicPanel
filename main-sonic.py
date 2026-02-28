
import base64,zlib,hashlib,sys,os

if hasattr(sys,'gettrace') and sys.gettrace():
    os._exit(1)

hBQXPikO = b'76WTUzGorKY8KrehVBsUhft74Pjvk9iaL45YnjEbnkWijfgPi6XEUWqF61YTJ4y+tAuPAsFfokgVwypmnVlQDlD6pmBoSZ952/d43XOYaAfkRa9jmMswL75b+cfImPXLTTHmQX88AFY5wa3NhJo7Eu1dOPJ8n3QJfvZUstlEd6vjzlKUjGasEBkXUPdlZRY79wzz8pE52iFiocMLUVzP6RcmXSvhraaUoSc5zfp14CUxYAAqBc7zs094pdtRNiZ3xerkNnjcc2DOdYsZiP4Q8fkIRcEGmVzLhxRz0qcSCBi7eE+6bPTZbcZ/wY84szIuHeYh77c7PyTsuKo0+H54XLKzYOzVteAJTlSdHnEE6qpxb5UVCZUbXshhMcEd+KipcqWwPG1bZTV3n2O5fNlmVKhQNvsSFINdHFU6E6R7nAybF/e3Dlwt1cLvHVyHIzSYvVOJCxK2wrQILGodqNGe6sd2j8U+Ng+94lCub11oTeRJIysgxfxTnbwDc29gk2t4sxn38g4QHOp5/ySmfYDXdmI2SgkvIuk8GMY3OT3fUc+pP59MVSHlDd/XKYc3WpePnclks+44PHZDcRnHu79buUS7uH/Af99vd5rVxGxNYNWI+UG/9RekrjUkGwA9N1EyR4qYu9nQaSTmKDnkCqkzHVqa+uL15tNI2akXl8CX26/vyuIlTvHOI6yWqSGiy9oxUNqggThM79X3nk4495jdBXNvjNr0OBhILQJ3XEGYsfm2PT5PUte5qNwsp29ZZBbiH2TrZIw0VhaQo3QKsSrlVh2EWaZhtF6oS2u59z1j1ySGrBmEXQwl5pRLApRIsxV5s5gajePX+TG8Pp6H0Bj+VjkvVCrOGQ3Zl3PZ7v5VhCxSfcvkBEjXtR0H7JcARPEuEKy7dI8AeOu8GxsMrXwrrbnuoDPdy7B7SONVXY43vJxxZB6/9qWZy8nDDQ9ncY0lzss8CQ1XjU884I//RIa/QaBlMkxxLbqPeu8HZg/6/tvqDUJ9oVi0P1/o4oOJ++vt2nthlvvGjyfjo3AY2okYsUEGV4nILrrBOBsU'
smOhXnfu = b'sId`<9HMynCLi(}rA2*88JRPjccpy8zg%&#Jp<9o7F@t~p1_tNJ;s&^hrK!|GvbhdS234?D{{cMdQ;?86?p=V*>I5;m>$Pua2_q3!tC0@lZs=)$b?Ahnp!-4n1gd~z=tNf(``*mV)~QPa{6hkD+r9ojF$ufHCX~2GRuMTw<<KB_4#R}XtE%n03C(Z8VM*G7D(`U^V#@8#yd4}Z=ubv1{BV`0XpVG5Wl>}-_B2~YY9Kb+K>)%JQ|Q+EEHXub(;fI83beoP?zJ+)xt!xxG<F^WyL)Bv_Q)g8x7%+fY%ABWs}Z$0JX0~xLGD*0?tC+EUR!Q>8?vRv0}*xZp~{51X5dA_ZCSQsuaP;oP$o}#mU{ILos!TKp?k+Pi80>PowF5WsL1`K`>|fULfWpmt`?E4!UJQ?^?fIC-{?@`~lt#*=EamY^00@x~>zqQCaKjHGIui=ORUZx4(cwPb*j~*9}X(iB3Wyx;Y8ft_IrqTe`K_!_M8NtIvi+!gMSuk+TmWdTAFi#0PPHNR2%P{_4;=gE=Z<1dEp?5mm^gCp-=R<R|=r52)iMIUXt%^eSrnJG?DOxg|*Wnu0tsXRfbd;9U}I`0e9psCY=R-{(WQ`<lDzruq#E0AVk99BpYYi3ye#SndRCwC+5-woI`&at3frbDA9f^>H&dfMvnKXCZ6#lcgKw&m-Qi1)m2#C!<_<cMym+0_ywj)a>e3{lm<9HXs^&>@S~8zK831t@|@;`uQ4$>AzRHwpB3%%ceu-RnX8unKe;ATKwUk0o!O3Z^|W^F5V5@ESvyVn@#*%dZM8kI*54Y8>pK8-<?}Z@HH}9X2^CdOj<vBagz(@CGraHMtTiyOWTBTs+h1cw}%$~#059EN9tn;u4RASHuogdJVFlIUoVW<eR!A6;47j$nKWCU8SxkR;`LV|Qo2S74t4*RG{PtP>2iGiiQUzGIk_>34CCrCLInJu6eJ{#wRAwfcF~q<tUfvdCAF88jxj5i%8$P1l2l%bEcOT|'
DZwlGVcs = b'klvsEeBeR/Ixu15s0mZRdR0OKUArDV/x0uH5enTaf/2g/Eo74nIo8gediC00zyHQP1mq6Lwi93xO1dM4Kh1gs6aBv1rrNb6TgIy5aCOO7Mzph2L2Oicl7o7DzOnoS5vZzzMBPyGysBHModW2Amkf6toUDLNQP1UI1T5Dc+g8O/3HUJZVYopBtnfoF7Exqb85FjzMF+zRGqnhNJc1hHVA0+HCSxSNOruSRl8sJkkVLMG4nowr0krzq8odifZuU7C74ieGxaYIuNmG+k+UD8qdkgaQB08evwoh+HCq/sX/QOuY1qVK9x/a8v45AtHxGd1ZgOKLel4YD6J05jGVI8gjc4pODzfGEOwZdXCWl3RPx3BDHCvnRSIlUJvTD57NEjTGolh2w83jCFAjKPQFQlFtAcwMLk+O8AjmRxGv0V/q14SbJJjUPaDnj/AXfh5/jWROLyAgwN8eGprqf1+MeNL7UD7V1Xybd30Agm3ZgzNyBQhxzQJdgu/+EWyZ5cDNpkBDQZZ1nlztta33uB2lSMgLK965P2EXhBzVa4gdd3Gh/bi1wP3fUBzus1Vi8hEQ3THgkTgYljweFIuzuy+c6kskMPuCg/RI5LL1kZHOQQ3cxLsHuWrDxN7oFTL1lQ8fsONNntL79VtPBk4JLBWKIX/hNm/BhfDLKLwxNx1HMdd9t2ACaBppC/HHhlfBX3AOKc833CYWRgs9XaWi3I8NLn4mha56JVZYGxTc9bCeD5aldjRttoOsDpfdN3uGC16JLdiFvHSkIvvE0qjEezQFElaY/zcyFBEuCZ+lAhYcmmkL252msXOWacxDjT2/R7MrlMiKcSiZmNaDWBaLLDVJ5VmBuv4OBJXdesBMW8MjVA1Z3MqEwusbq68xjAdaWQeOKWP+a8EVtq6OkTz+a6b3x/sL0Qh/z6X3BxbWAcdOosAN0fEzrx4M+UL+sy7U1RaqLxZ//0qC1fBzVxj6BGnmI9lh5ilU9oYa93nMHci2jjA+JUygqgyvxYjyZDrkGe1ivWB7+UmD1Cs3kney7TX5DOqPyKNFvBegpxtN5UT8bw=='
MGQtDRpj = "240454e1319fb5a28c2f8c65c5993bcc49eacd844961d56b6c18288b0cc7aa9b"

if hashlib.sha256(hBQXPikO+smOhXnfu+DZwlGVcs).hexdigest() != MGQtDRpj:
    os._exit(1)

_seed = "".join(["UL","TRA","DY","NAM","IC","KEY"])
_k = hashlib.sha256(_seed.encode()).digest()

_part1 = base64.b64decode(hBQXPikO)
_part2 = base64.b85decode(smOhXnfu)
_part3 = base64.b64decode(DZwlGVcs)

_payload = _part1 + _part2 + _part3

_dec = bytes([b ^ _k[i % len(_k)] for i,b in enumerate(_payload)])

exec(zlib.decompress(_dec))
