import json,os
from urllib.request import*
V=[0,100,320,330,500,900,0];PR=[0,50,19,12,10,0,5,0]
B=[0]*128;S=0;C=0;E=-1;K=[0,0]
N=[-16,16,-1,1];D=[-15,15,-17,17];A=N+D;W=[-33,-31,-18,-14,14,18,31,33]
Q=[i for i in range(128)if not i&0x88];CR={112:2,119:1,0:8,7:4};DS={2:W,3:D,4:N,5:A,6:A}
ND=0;LIM=50000;Ab=Exception;sqo=lambda x:(8-int(x[1]))*16+ord(x[0])-97
def at(s,y):
 o=y<<3
 for d in (15,17):
  t=s+d if y==0 else s-d
  if not t&0x88 and B[t]==1|o:return 1
 for d in W+A:
  t=s+d
  if not t&0x88 and B[t]==((2 if d in W else 6)|o):return 1
 for d in A:
  t=s+d
  while not t&0x88 and not B[t]:t+=d
  if not t&0x88 and B[t]>>3==y and B[t]&7 in((4,5) if d in N else (3,5)):return 1
 return 0
def gen():
 ms=[];a=ms.append;d=-16 if S==0 else 16
 def pm(s,u):
  for pr in (5,4,3,2):a(s|u<<7|pr<<14)
 for s in Q:
  p=B[s]
  if not p or p>>3!=S:continue
  t=p&7
  if t==1:
   u=s+d
   if not B[u]:
    if u>>4 in (0,7):pm(s,u)
    else:
     a(s|u<<7)
     if s>>4==(6 if S==0 else 1) and not B[s+2*d]:a(s|(s+2*d)<<7)
   for dd in (d-1,d+1):
    u=s+dd
    if u&0x88:continue
    q=B[u]
    if q and q>>3!=S:pm(s,u) if u>>4 in (0,7) else a(s|u<<7)
    elif not q and u==E:a(s|u<<7)
  else:
   for dd in DS[t]:
    u=s+dd
    while not u&0x88:
     q=B[u]
     if q:
      if q>>3!=S:a(s|u<<7)
      break
     a(s|u<<7)
     if t in (2,6):break
     u+=dd
 kf=116 if S==0 else 4
 for bit,sg in ((1,1),(2,-1)) if S==0 else ((4,1),(8,-1)):
  e1,e2=kf+sg,kf+2*sg
  if C&bit and not (B[e1] or B[e2] or sg<0 and B[kf+3*sg]) and not any(at(x,1-S) for x in (kf,e1,e2)):a(kf|e2<<7)
 return ms
def make(m):
 global S,C,E
 f=m&127;t=m>>7&127;pr=m>>14&7;p=B[f];ty=p&7
 if ty==1 and t==E and not B[t]:
  cs=t+16 if S==0 else t-16;B[cs]=0
 E=(f+t)//2 if ty==1 and abs(t-f)==32 else -1
 B[t]=pr|S<<3 if pr else p;B[f]=0
 if ty==6:
  K[S]=t
  if abs(t-f)==2:
   rf,rt=(t+1,t-1) if t>f else (t-2,t+1);B[rt]=B[rf];B[rf]=0
  C&=~(3 if S==0 else 12)
 for x in (f,t):C&=~CR.get(x,0)
 S^=1
def rs(v):
 global S,C,E
 B[:]=v[0];S,C,E=v[1:4];K[:]=v[4]
def ev():
 s=0;nb=[0,0]
 for sq in Q:
  p=B[sq]
  if p:
   ty=p&7;c=p>>3;v=V[ty]
   if ty==1:v+=PR[sq>>4 if c==0 else 7-sq>>4]
   if ty==3:nb[c]+=1
   s+=v if c==0 else -v
 s+=25*((nb[0]>1)-(nb[1]>1))
 return s if S==0 else -s
def order(l):return sorted(l,key=lambda m:-V[B[m>>7&127]&7])
def search(d,a,b):
 global ND;ND+=1
 if ND>LIM:raise Ab
 inc=at(K[S],S^1);best=-100001;q=d<=0 and not inc
 if inc:d+=1
 if q:
  best=ev()
  if best>=b:return b
  if best>a:a=best
 for m in order(gen()):
  t=m>>7&127
  if q and not (B[t] or m>>14):continue
  v=B[:],S,C,E,K[:];make(m)
  if at(K[S^1],S):rs(v);continue
  s=-search(d-1,-b,-a);rs(v)
  if s>best:best=s
  if s>a:a=s
  if a>=b:break
 return best if best>-100001 else 0 if d>0 and not inc else -100000
def parse(fen):
 global S,C,E
 ps=fen.split();B[:]=[0]*128;sq=0
 for ch in ps[0]:
  if ch=='/':sq+=8
  elif ch.isdigit():sq+=int(ch)
  else:
   p='PNBRQK'.index(ch.upper())+1+8*ch.islower();B[sq]=p
   if p&7==6:K[p>>3]=sq
   sq+=1
 S=1-(ps[1]=='w');C=0
 for c,b in zip('KQkq',(1,2,4,8)):C|=b*(c in ps[2])
 E=-1 if ps[3]=='-' else sqo(ps[3])
def fromu(u):
 m=sqo(u[:2])|sqo(u[2:4])<<7
 if len(u)==5:m|='nbrq'.index(u[4])+2<<14
 return m
def best():
 global ND;l=[]
 for m in gen():
  v=B[:],S,C,E,K[:];make(m)
  if not at(K[S^1],S):l.append(m)
  rs(v)
 bm=l[0];d=1
 while d<64:
  ND=0;nm=bm
  try:
   a=-100000
   for m in order(l):
    v=B[:],S,C,E,K[:];make(m);s=-search(d-1,-100000,-a);rs(v)
    if s>a:a=s;nm=m
   bm=nm
  except Ab:
   if d==1:bm=nm
   break
  d+=1
 return bm
post=lambda p,b:json.load(urlopen(Request(os.getenv('MAKEFUN_ENV_URL')+p,data=json.dumps(b).encode())))
def play():
 while 1:
  g=post('/game',{})
  if g['status']=='done':break
  while g['status']=='your_move':
   parse(g['start_fen'])
   for u in g['moves']:make(fromu(u))
   m=best();f=m&127;t=m>>7&127;pr=m>>14&7
   u=chr(97+(f&7))+str(8-f//16)+chr(97+(t&7))+str(8-t//16)+('nbrq'[pr-2] if pr else '')
   if u not in g['legal_moves']:u=g['legal_moves'][0]
   g=post('/move',{'game':g['game'],'move':u})
if __name__=='__main__':play()
