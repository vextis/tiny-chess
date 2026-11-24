import json,os,urllib.request as U
V=[0,100,320,330,500,900,0]
def TB(s):return[(int(c,36)-18)*3for c in s]
P=[0,TB("iiiizzzzllpskklqiiipkgfikllbiiii"),TB("15885bii8iln8knp8inp8kln5bik1588"),0,TB("iiiiklllgiiigiiigiiigiiigiiiiiik"),0,TB("8551855185518551b885fbbbppiipsli")]
B=[0]*128;S=C=E=0;K=[0,0]
N=[-16,16,-1,1];D=[-15,15,-17,17];A=N+D;W=[-33,-31,-18,-14,14,18,31,33]
Q=[i for i in range(128)if not i&0x88];CR={112:2,119:1,0:8,7:4}
ND=0;Ab=Exception;TT={};KL=[[0]for _ in range(200)];BM=0
sqo=lambda x:128-16*int(x[1])+ord(x[0])-97;sv=lambda:(B[:],S,C,E,K[:])
def at(s,y):
 o=y<<3
 for d in W+A:
  t=s+d
  if not t&0x88 and (B[t]==(6-4*(d in W))|o or d in D and (d>0)!=y and B[t]==1|o):return 1
 for d in A:
  t=s+d
  while not t&0x88 and not B[t]:t+=d
  if not t&0x88 and B[t]>>3==y and B[t]&7 in(3+(d in N),5):return 1
 return 0
def gen():
 ms=[];a=ms.append;d=32*S-16
 def pm(s,u):
  for pr in(5,4,3,2):a(s|u<<7|pr<<14)
 for s in Q:
  p=B[s]
  if not p or p>>3!=S:continue
  t=p&7
  if t==1:
   u=s+d
   if not B[u]:
    if u>>4 in(0,7):pm(s,u)
    else:
     a(s|u<<7)
     if s>>4==6-5*S and not B[s+2*d]:a(s|(s+2*d)<<7)
   for dd in(d-1,d+1):
    u=s+dd
    if not u&0x88 and (B[u]and B[u]>>3!=S or u==E):pm(s,u)if u>>4 in(0,7)else a(s|u<<7)
  else:
   for dd in(W,D,N,A,A)[t-2]:
    u=s+dd
    while not u&0x88:
     q=B[u]
     if q:
      if q>>3!=S:a(s|u<<7)
      break
     a(s|u<<7)
     if t in(2,6):break
     u+=dd
 kf=116-112*S
 for bit,sg in((1,1),(2,-1)):
  e1,e2=kf+sg,kf+2*sg
  if C&bit<<2*S and not(B[e1]or B[e2]or sg<0 and B[kf+3*sg])and not any(at(x,1-S)for x in(kf,e1,e2)):a(kf|e2<<7)
 return ms
def make(m):
 global S,C,E
 f=m&127;t=m>>7&127;pr=m>>14&7;p=B[f];ty=p&7
 if ty==1 and t==E:
  cs=t+16-32*S;B[cs]=0
 E=(f+t)//2 if ty==1 and abs(t-f)==32 else -1
 B[t]=pr|S<<3 if pr else p;B[f]=0
 if ty==6:
  K[S]=t
  if abs(t-f)==2:
   rf,rt=(t+1,t-1)if t>f else(t-2,t+1);B[rt]=B[rf];B[rf]=0
  C&=~(3+9*S)
 C&=~(CR.get(f,0)|CR.get(t,0))
 S^=1
def rs(v):
 global S,C,E
 B[:]=v[0];S,C,E=v[1:4];K[:]=v[4]
def ev():
 s=0
 for sq in Q:
  p=B[sq]
  if p:
   ty=p&7;c=p>>3;r,f=sq>>4,sq&7;j=(7-r if c else r)*4+min(f,7-f)
   v=V[ty]+(P[2][j]//2 if ty in(3,5)else P[ty][j]);s+=v-2*v*c
 return s-2*s*S
def search(d,a,b,pl):
 global ND,BM;ND+=1
 if ND>50000:raise Ab
 inc=at(K[S],S^1);tm=0
 if inc:d+=1
 q=d<=0 and not inc;best=-100001
 if q:
  best=ev()
  if best>=b:return b
  a=max(a,best)
 else:
  ky=(bytes(B),S,C,E);e=TT.get(ky)
  if e:
   tm=e[2]
   if e[0]>=d and -99900<e[1]<99900:return e[1]
 a0=a;bm=0;k=KL[pl%200];ms=gen()
 if q:ms=[m for m in ms if B[m>>7&127]or m>>14]
 for m in sorted(ms,key=lambda m:-99999 if m==tm else -10000-V[B[m>>7&127]&7]*10 if B[m>>7&127]else -9000 if m==k[0]else 0):
  t=m>>7&127
  v=sv();make(m)
  if at(K[S^1],S):rs(v);continue
  s=-search(d-1,-b,-a,pl+1);rs(v)
  if s>best:best,bm=s,m
  a=max(a,s)
  if a>=b:
   if not q and not B[t]and not m>>14:k[0]=m
   break
 if best==-100001:return -100000 if inc else 0
 if not q and a0<best<b:TT[ky]=(d,best,bm)
 if pl<1:BM=bm
 return best
def parse(fen):
 global S,C,E
 ps=fen.split();B[:]=[0]*128;sq=0
 for ch in ps[0]:
  if ch=='/':sq+=8
  elif ch.isdigit():sq+=int(ch)
  else:
   p='PNBRQK'.index(ch.upper())+1+8*(ch>'a');B[sq]=p
   if p&7==6:K[p>>3]=sq
   sq+=1
 S=ps[1]!='w';C=0
 for c,b in zip('KQkq',(1,2,4,8)):C|=b*(c in ps[2])
 E=-1 if ps[3]=='-' else sqo(ps[3])
def best():
 global ND,TT,BM;TT={};BM=gen()[0];d=1;ND=0
 while d<64:
  try:search(d,-100000,100000,0)
  except Ab:break
  d+=1
 return BM
post=lambda p,b:json.load(U.urlopen(os.getenv('MAKEFUN_ENV_URL')+p,json.dumps(b).encode()))
def play():
 while 1:
  g=post('/game',{})
  if g['status']=='done':break
  while g['status']=='your_move':
   parse(g['start_fen'])
   for u in g['moves']:make(sqo(u[:2])|sqo(u[2:4])<<7|('nbrq'.index(u[4])+2<<14 if len(u)==5 else 0))
   m=best();f=m&127;t=m>>7&127;pr=m>>14&7
   u=f"{chr(97+(f&7))}{8-f//16}{chr(97+(t&7))}{8-t//16}"+('nbrq'[pr-2]if pr else '')
   if u not in g['legal_moves']:u=g['legal_moves'][0]
   g=post('/move',{'game':g['game'],'move':u})
play()
