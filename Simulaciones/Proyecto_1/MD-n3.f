!======================================================================
      module coor
       integer, parameter :: n=864,ngrx=1000  ! debe ser n=4*a*a*a
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

       Integer (kind=8) :: npasos,dum
       Integer (kind=8) :: i,k,j,iprint

      real (kind=8) :: r,rho,T,pi
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


        open(0, file = '0_salida.dat',status='unknown')
        open(2, file = '2_velo.dat',status='unknown')
        open(3, file = '3_coor.dat',status='unknown')
        open(4, file = '4_hr.dat',status='unknown')
        open(5, file = '5_Cor_in.dat',status='unknown')
        open(6, file = '6_coorpymol.xyz',status='unknown')
        open(7, file = '7_velpymol.xyz',status='unknown')
        open(8, file = '8_T_U_P.dat',status='unknown')


      rho=0.3
      T=0.6
      npasos=200000
      iprint = npasos/1000
      
      dum = 17367d0
      pi = 4d0 * datan(1d0)
!<------------------Definicion de las coordenadas------------------>
         call fcc(n, rho, aL, aL, aL)

         do i=1,n
           vr = dsqrt(3*T)
          call ggub(dum,r)
           cost = 2*r-1
           sint = dsqrt(1-cost**2)
          call ggub(dum,r)
           fi = r*2*pi
            vx(i) = vr*sint*dcos(fi)
            vy(i) = vr*sint*dsin(fi)
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

         do i = 1,ngrx
           gr(i) = 0
         end do

      do k = 1,npasos

         do i = 1, n
           call pbc(x(i),y(i),aL,aL)
         end do

         do i = 1, n
          fx(i) = 0
          fy(i) = 0
         end do

         epot=0

         do i = 1, n-1
          xi = x(i)
          yi = y(i)
           do j = i+1, n
             xx = xi-x(j)
             yy = yi-y(j)
              call mic(xx,yy,aL,aL)
             r2 = xx**2+yy**2+zz**2
!<---------------Potencial de interacción---------------->
             if (r2 .lt. cut2) then
               r1 = 1/r2
               r6 = r1**3
               pot=4*r6*(r6-1)

               u = u+pot
               epot=epot+pot

               rr = 48*r6*r1*(r6-0.5d0)

               fxx = rr*xx
               fyy = rr*yy

               ap = ap+rr*r2

               fx(i) = fx(i)+fxx
               fy(i) = fy(i)+fyy
               fx(j) = fx(j)-fxx
               fy(j) = fy(j)-fyy
             end if
           end do
         end do

         ekin=0
!<----------------Calculo de la energía cinetica------------------->
         do i=1,n
          vxi = vx(i)+dt*fx(i)
          vyi = vy(i)+dt*fy(i)

            vxx = 0.5d0*(vxi+vx(i))
            vyy = 0.5d0*(vyi+vy(i))

            en = vxx**2+vyy**2
            ekin = ekin+en
            ec = ec+en

            vx(i) = vxi
            vy(i) = vyi
!<-----------------Movimiento infinitedecimal------------------------>
            x(i) = x(i)+dt*vx(i)
            y(i) = y(i)+dt*vy(i)
         end do
!<------------Over
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
             write(6,16)n
             write(7,16)n
           do i=1,n
             write(6,15)i,SNGL(x(i)),SNGL(y(i)),22,i
             write(7,15)i,SNGL(vx(i)),SNGL(vy(i)),22,i
           end do
          endif
          
!<-----------------------Histograma----------------------------------------->
         call sgdr(n,aL,aL,hgr)

      end do

        temp =ec/(3*n*npasos)
        u = u/(n*npasos)
        ap = rho*temp+ap/(3*aL**3*npasos)

        write(0,*)
        write(0,*) '==================Salida========================='
        write(0,*) 'temperature=',temp
        write(0,*) 'energy=',u
        write(0,*) 'pressure=',ap

        do k=1,ngrx
         r = (k-1)*hgr+hgr/2d0
         area = pi*((r+hgr/2d0)**2-(r-hgr/2d0)**2)
         gdr = gr(k)/(n*(n-1)/aL**2*npasos*area)
         write(4,*) r,gdr
        end do




15    format(3x,I3,2x,'C',3x,f10.5,2x,f10.5,2x,f10.5,4x,I3,3x,I3)
16    format(2x,I3)



      Close(0)
      Close(2)
      Close(3)
      Close(4)
      Close(5)
      Close(6)
      Close(7)
      Close(8)

          write (*,*) 'Esooo es toooodooo amiiigosss '
          write (0,*) 'Esooo es toooodooo amiiigosss '
      
      end program MD
      
      
      
! **********************************************************************
!     Generation of fcc lattice
! *******************************************************************
       subroutine fcc(lmn, dens, xl, yl)
       use coor

       implicit real*8 (a-h, o-z)

       real (kind=8) :: xl,yl
       Integer (kind=8) :: nn
       dimension sx(4), sy(4)

       data sx /0d0, 0.5d0, 0.5d0, 0d0/
       data sy /0d0, 0.5d0, 0d0, 0.5d0/
       data sz /0d0, 0d0, 0.5d0, 0.5d0/

       data sh /0.01d0/

       a = (4d0/dens)**(1d0/3d0)
       nn = (lmn/4)**(1d0/3d0) + 0.001

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
      real*8 z,d2p31m,d2pn31,dseed
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

       rx=rx-xl*dnint(rx/xl)
       ry=ry-yl*dnint(ry/yl)

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
      
