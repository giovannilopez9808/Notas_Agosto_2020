!======================================================================
      module coor
       integer, parameter :: n=6  ! debe ser n=4*a*a*a
       real (kind=8) :: x(n), y(n)
       real (kind=8) :: vx(n),vy(n)
       real (kind=8) :: fx(n),fy(n)

      end module coor

      program MD
      use coor            ! Coordenadas de posicion.
      implicit none

      Integer (kind=8) :: npasos
      Integer (kind=8) :: i,k,j,iprint

      real (kind=8) :: pi,dum,random,r,ra
      real (kind=8) :: cut2,cutr2,dt
      real (kind=8) :: ec,u
      real (kind=8) :: epot
      real (kind=8) :: xx,yy,r2
      real (kind=8) :: r1,r6,pot,rr,fxx,fyy
      real (kind=8) :: ekin,en
      real (kind=8) :: vxi,vyi,vxx,vyy
      real (kind=8) :: xi,yi

      character:: path*11,version*1
      path="../Results/"

      open(11,file='../Input/rho.txt',status='unknown')
      read(11,*) version

      open(0,file=path//'0_salida_'//version//'.dat',status='unknown')
      open(2,file=path//'2_velo_'//version//'.dat',status='unknown')
      open(3,file=path//'3_coor_'//version//'.dat',status='unknown')
      open(5,file=path//'5_Cor_in_'//version//'.dat',status='unknown')
      open(8,file=path//'8_T_U_P_'//version//'.dat',status='unknown')
      r=1
      ra=2
      npasos=200000
      iprint = npasos/1000
      dum = 17367d0
      pi = 4d0 * datan(1d0)
!<------------------Definicion de las coordenadas------------------>
      x(1)=0
      y(1)=0
      write(5,*) 1,x(1),y(1)
      do i=2,n
        call RANDOM_NUMBER(random)
        x(i)=x(1)+(random*2-1)*r
        call RANDOM_NUMBER(random)
        y(i)=y(i)+(random*2-1)*r
        write(5,*) i,x(i),y(i)
      end do
      cut2 = (2.5d0)**2
      dt = 0.01d0
      write(0,*) 'N-step=',npasos
      write(0,*) 'N-step=',npasos
      write(0,*) 'corte=',cut2
      write(0,*) 'dt=',dt
      ec = 0
      u = 0
      do k = 1,npasos
!<-------------------Iniciañizacion de las fuerzas-------------->
        do i = 1, n
          fx(i) = 0
          fy(i) = 0
        end do
!<------------Inicializacion de la energia potencial--------------->
        epot=0
        do i=1,n-1
          j=i+1
          xi = x(i)
          yi = y(i)
          xx = xi-x(j)
          yy = yi-y(j)
          r2 = xx**2+yy**2
  !<---------------------Potencial atractivo--------------->
          if (r2.le.ra) then
            r1=(ra/r2)**2
            pot=-r1*log(1-r1)/2
            u=u+pot
            epot=epot+pot
            rr=r1/r2*(log(1-r1)+1/(1/r1-1))
            call moving(fx,fy,rr,xx,yy,i)
          end if
  !<---------------Potencial de Lennard-Jones---------------->
          if (r2 .lt. cut2) then
            r1 = 1/r2
            r6 = r1**3
            pot=4*r6*(r6-1)
            u = u+pot
            epot=epot+pot
            rr = 48*r6*r1*(r6-0.5d0)
            call moving(fx,fy,rr,xx,yy,i)
          end if
        end do
!<----------------Calculo de la energía cinetica------------------->
        ekin=0
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
        if(mod(k,iprint).EQ.0) then
          write(3,*)k
          write(2,*)k
          do i=1,n
            write(3,*)SNGL(x(i)),SNGL(y(i))
            write(2,*)SNGL(vx(i)),SNGL(vy(i))
          end do
          write(8,*)k,ekin/(3*n),epot/(n*n)
        endif
      end do
      Close(0)
      Close(2)
      Close(3)
      Close(5)
      Close(8)
      Close(11)
      end program MD
      
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

      subroutine moving(fx,fy,rr,xx,yy,i)
        real (kind=8) ::fx(n),fy(n)
        real (kind=8) :: xx,yy,rr
        integer*8 i
        j=i+1
        fxx = rr*xx
        fyy = rr*yy
        fx(i) = fx(i)+fxx
        fy(i) = fy(i)+fyy
        fx(j) = fx(j)-fxx
        fy(j) = fy(j)-fyy
      end subroutine