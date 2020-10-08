!======================================================================
      module coor
       integer, parameter :: n=784,ngrx=1000  ! debe ser n=4*a*a*a
       real (kind=8) :: x(n), y(n)
       real (kind=8) :: vx(n),vy(n)
       real (kind=8) :: fx(n),fy(n)
       real (kind=8) :: aL
       real (kind=8) :: gr(ngrx)

      end module coor
!======================================================================
!
!     MD for Lennard-Jones particles
!
      program MD
      use coor            ! Coordenadas de posicion.
      implicit none

      Integer (kind=8) :: npasos
      Integer (kind=8) :: i,k,j,iprint

      real (kind=8) :: r,rho,T,pi,dum
      real (kind=8) :: vr,cost,sint,fi
      real (kind=8) :: aL2,cut2,cutr2,ngr,hgr,dt
      real (kind=8) :: ec,u,ap
      real (kind=8) :: epot
      real (kind=8) :: xx,yy,r2
      real (kind=8) :: r1,r6,pot,rr,fxx,fyy
      real (kind=8) :: ekin,en,temp
      real (kind=8) :: vxi,vyi,vxx,vyy
      real (kind=8) :: area,gdr
      real (kind=8) :: xi,yi
!<------------------Información------------------>
      !Tcons - Temperatura constante de alrededor
      real (kind=8) :: tau,sigma

      character:: path*11,version*8
      path="../Results/"
!<-------------------------------Lectura del input------------------>
      open(11,file='../Input/rho.txt',status='unknown')
      read(11,*) rho,version

      open(0,file=path//'0_salida'//version//'.dat',status='unknown')
      open(2,file=path//'2_velo'//version//'.dat',status='unknown')
      open(3,file=path//'3_coor'//version//'.dat',status='unknown')
      open(4,file=path//'4_hr'//version//'.dat',status='unknown')
      open(5,file=path//'5_Cor_in'//version//'.dat',status='unknown')
      open(10,file=path//'6_coorpymol'//version//
     & '.xyz',status='unknown')
      open(7,file=path//'7_velpymol'//version//'.xyz',status='unknown')
      open(8,file=path//'8_T_U_P'//version//'.dat',status='unknown')
      open(12,file=path//"temp"//version//".dat",status="unknown")

      npasos=2000
      iprint = npasos/100
      dum = 17367d0
      pi = 4d0 * datan(1d0)
!<------------------------- Temperatura inicial-------------------------------->
      T=0.6
!<------------------Definicion de las coordenadas------------------>
      call fcc(n, rho, aL, aL)
      do i=1,n
        vr = dsqrt(2*T)
        call ggub(dum,r)
        fi = r*2*pi
        vx(i) = vr*dcos(fi)
        vy(i) = vr*dsin(fi)
      end do
      aL2 = aL/2d0
      cut2 = (2.5d0)**2
      cutr2 = (aL/2)**2
      ngr = 1000
      hgr = aL2/ngr
      dt = 0.01d0
      write(0,*) 'T-ini=',T
      write(0,*) 'N-step=',npasos
      write(0,*) 'Dens=',rho
      write(0,*) 'N-step=',npasos
      write(0,*) 'Lado box=',aL
      write(0,*) 'corte=',cut2
      write(0,*) 'dt=',dt
      ec = 0
      u = 0
      ap = 0
!<---------------Inicializacion del histograma------------------->
      do i = 1,ngrx
        gr(i) = 0
      end do
      do k = 1,npasos
!<--------------------------Condiciones periodicas------------->
        do i = 1, n
          call pbc(x(i),y(i),aL,aL)
        end do
!<-------------------Iniciañizacion de las fuerzas-------------->
        do i = 1, n
          fx(i) = 0
          fy(i) = 0
        end do
!<------------------Movimiento----------------------->
        do i = 1, n
          x(i) = x(i) + dt*vx(i) + dt**2*fx(i)/2
          y(i) = y(i) + dt*vy(i) + dt**2*fy(i)/2
          vx(i) = vx(i) + dt*fx(i)/2
          vy(i) = vy(i) + dt*fy(i)/2
        end do
!<------------Inicializacion de la energia potencial--------------->
        epot=0
        do i = 1, n-1
        xi = x(i)
        yi = y(i)
          do j = i+1, n
            xx = xi-x(j)
            yy = yi-y(j)
            call mic(xx,yy,aL,aL)
            r2 = xx**2+yy**2
!<---------------Potencial de interacción---------------->
            if (r2 .lt. cut2) then
              r1 = 1/r2
              r6 = r1**3
              pot=4*r6*(r6-1)
              rr = 48*r6*r1*(r6-0.5d0)
              u = u+pot
              epot=epot+pot
              fxx = rr*xx
              fyy = rr*yy
              ap = ap+rr*r2
              fx(i) = fx(i)+fxx/r2
              fy(i) = fy(i)+fyy/r2
              fx(j) = fx(j)-fxx/r2
              fy(j) = fy(j)-fyy/r2
            end if
          end do
        end do
!<----------------Calculo de la energía cinetica------------------->
        ekin=0
        do i=1,n
          vx(i)=vx(i)+dt*fx(i)/2
          vy(i)=vy(i)+dt*fy(i)/2
          en=vx(i)**2+vy(i)**2
          ekin=ekin+en
          ec=ec+en
        end do
        tau=ec/(3*n*k)
        write(12,*) k,tau
    !FALRA DEFINIR TEMP,NU,iseed
        sigma=sqrt(temp)
        do i=1,n
          if (RANF(Iseed).lt.nu*dt) then
            vx(i)=GASDEV(Sigma, Iseed)
            vy(i)=GASDEV(Sigma, Iseed)
          end if
        end do
        if(mod(k,iprint).EQ.0) then
            write(3,*)k
            write(2,*)k
          do i=1,n
            write(3,*)SNGL(x(i)),SNGL(y(i))
            write(2,*)SNGL(vx(i)),SNGL(vy(i))
          end do
          write(8,*)k,ekin/(3*n),epot/(n*n),ap/(3*aL**2)
        endif    
        if(mod(k,iprint*2).EQ.0) then
            write(10,16)n
            write(7,16)n
          do i=1,n
            write(10,15)i,SNGL(x(i)),SNGL(y(i)),22,i
            write(7,15)i,SNGL(vx(i)),SNGL(vy(i)),22,i
          end do
        endif 
  !<-----------------------Histograma----------------------------------------->
        call sgdr(n,aL,aL,hgr)
      end do

      temp =ec/(3*n*npasos)
      u = u/(n*npasos)
      ap = rho*temp+ap/(3*aL**2*npasos)

      write(0,*)
      write(0,*) '==================Salida========================='
      write(0,*) 'temperature=',temp
      write(0,*) 'energy=',u
      write(0,*) 'pressure=',ap
!<-----------------Creacion del histograma---------------------------------->
      do k=1,ngrx
        r = (k-1)*hgr+hgr/2d0
        area = pi*((r+hgr/2d0)**2-(r-hgr/2d0)**2)
        gdr = gr(k)/(n*(n-1)/aL**2*npasos*area)
        write(4,*) r,gdr
      end do
!<-----------------------------Formatos de los archivos de salida-------------------->
15    format(3x,I3,2x,'C',3x,f10.5,2x,f10.5,2x,I3,3x,I3)
16    format(2x,I3)



      Close(0)
      Close(2)
      Close(3)
      Close(4)
      Close(5)
      Close(10)
      Close(7)
      Close(8)
      Close(11)
      Close(12)
      
      end program MD
      
      
      
! **********************************************************************
!     Generation of fcc lattice
! *******************************************************************
       subroutine fcc(lmn, dens, xl, yl)
       use coor

       implicit real*8 (a-h, o-z)

       real (kind=8) :: xl,yl,dx,dy
       Integer (kind=8) :: nn
       dimension sx(4), sy(4)

       data sx /0d0, 0.5d0, 0.5d0, 0d0/
       data sy /0d0, 0.5d0, 0d0, 0.5d0/
       data sh /0.01d0/

       a = (4d0/dens)**(1d0/2d0)
       nn = (lmn/4)**(1d0/2d0) + 0.001

       xl = nn*a
       yl = nn*a

       m = 1
       do i = 1, nn
        do j = 1, nn
          do l = 1, 4
            x(m) = (i - 1 + sx(l) + sh) * a - xl/2
            y(m) = (j - 1 + sy(l) + sh) * a - yl/2
           write(5,*) x(m),y(m),m
           m=m+1
          end do
        end do
       end do
      end subroutine
      
! **********************************************************************
!      P1: Random number generator
! **********************************************************************
      subroutine ggub(dseed,r)
      real*8 z,d2p31m,d2pn31,dseed,r
      data d2p31m/2147483647./,d2pn31/2147483648./

       z = dseed
       z = dmod(16807.*z,d2p31m)
       r = z / d2pn31
       dseed = z
      end subroutine


! **********************************************************************
!      Periodic boundary conditions
! **********************************************************************
       subroutine pbc(rx,ry,xl,yl)
       use coor
       implicit none
       real (kind=8) :: rx,ry
       real (kind=8) :: xl,yl
       if (abs(rx).gt.xl) rx=rx-xl*dnint(rx/xl)
       if (abs(ry).gt.yl) ry=ry-yl*dnint(ry/yl)
        end subroutine
        
! **********************************************************************
!      Minimum image convention
! **********************************************************************
       subroutine mic(xx,yy,xl,yl)
       use coor
       implicit none
       real (kind=8) :: xx,yy
       real (kind=8) :: xl,yl

         xx=xx-xl*dnint(xx/xl)
         yy=yy-yl*dnint(yy/yl)
       end subroutine
       
! **********************************************************************
! Histogram for g(r)
! **********************************************************************
      subroutine sgdr(m,xl,yl,hgr)
      use coor

      implicit real*8(A-H,O-Z)
      real (kind=8) :: xl,yl,hgr

       do i = 1, m-1
        do j = i + 1,m
         xx = x(i) - x(j)
         yy = y(i) - y(j)
       call mic (xx,yy,xl,yl)
         r = xx*xx + yy*yy
         rr = dsqrt(r)
         if (rr .lt. xl/2) then
           k = rr/hgr + 1
           gr(k) = gr(k) + 2
         end if
        end do
       end do
      end subroutine
!<--------------------Normal distribution----------------------------->
      DOUBLE PRECISION FUNCTION GASDEV(Sigma, Iseed)
      IMPLICIT NONE
      DOUBLE PRECISION r, v1, v2, fac, gset, RANF
      DOUBLE PRECISION Sigma
      INTEGER iset, Iseed 
      SAVE gset, iset
      DATA iset/0/
 100  IF (iset.EQ.0) THEN
         v1 = 2.D0*RANF(Iseed) - 1.D0
         v2 = 2.D0*RANF(Iseed) - 1.D0
         r = v1**2 + v2**2
         IF (r.GE.1) GOTO 100
         fac = SQRT(-2.D0*LOG(r)/r)
         gset = v1*fac
         GASDEV = v2*fac
         iset = 1
      ELSE
         GASDEV = gset
         iset = 0
      END IF
      GASDEV = GASDEV*Sigma
      RETURN
c-------------------------------------------------------c
      END
**==ranf.spg  processed by SPAG 4.52O  at 18:54 on 27 Mar 1996
      FUNCTION RANF(Idum)
      IMPLICIT NONE
      INTEGER Idum
      DOUBLE PRECISION RANF, RCARRY
      RANF = RCARRY()
      RETURN
C ----------------------------------------------------C
      END
      FUNCTION RCARRY()
C----------------------------------------------------------------------C
C       Random number generator from Marsaglia.
C----------------------------------------------------------------------C
      IMPLICIT NONE
      DOUBLE PRECISION CARRY, RCARRY, SEED, TWOm24, TWOp24, uni
      INTEGER I24, ISEED, J24
      PARAMETER (TWOp24=16777216.D+0, TWOm24=1.D+0/TWOp24)
      COMMON /RANDOM/ SEED(24), CARRY, I24, J24, ISEED
c
c       F. James Comp. Phys. Comm. 60, 329  (1990)
c       algorithm by G. Marsaglia and A. Zaman
c       base b = 2**24  lags r=24 and s=10
c
      uni = SEED(I24) - SEED(J24) - CARRY
      IF (uni.LT.0.D+0) THEN
          uni = uni + 1.D+0
          CARRY = TWOm24
      ELSE
          CARRY = 0.D+0
      END IF
      SEED(I24) = uni
      I24 = I24 - 1
      IF (I24.EQ.0) I24 = 24
      J24 = J24 - 1
      IF (J24.EQ.0) J24 = 24
      RCARRY = uni
  
      RETURN
      END